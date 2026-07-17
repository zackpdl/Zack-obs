#!/usr/bin/env python3
"""Study Reader Server — dyslexia-friendly TTS reader for study guides.
Loads study guides from your vault, serves a beautiful reader with
sentence-by-sentence highlighting and Chatterbox Turbo TTS."""

import http.server
import json
import os
import re
import ssl
import threading
import urllib.request
import urllib.parse
import time
from pathlib import Path

VAULT = os.path.expanduser("~/Documents/Obsidian/Zack-obs")
PORT = 8765

# ─── Guide Registry ─────────────────────────────────────────────
GUIDES = {}

# Auto-discover study guides
pattern = re.compile(r"^00 - .* Study Guide")
for fpath in Path(VAULT).rglob("*.md"):
    if pattern.match(fpath.name):
        # Extract course code from path
        parts = fpath.relative_to(VAULT).parts
        display = " / ".join(parts[:-2]) if len(parts) > 2 else str(list(parts)[-2]) if len(parts) > 1 else str(fpath.parent.name)
        code_match = re.search(r'(ITX\d+|CSX\d+|GE\d+|BG\d+)', str(fpath))
        code = code_match.group(1) if code_match else ""
        name_clean = list(parts)[-1].replace('00 - ', '').replace(' Study Guide.md', '')
        GUIDES[str(fpath.relative_to(VAULT))] = {
            "path": str(fpath.relative_to(VAULT)),
            "display": f"{code} - {name_clean}" if code else name_clean,
            "code": code,
        }


# ─── Markdown Parser ────────────────────────────────────────────
def parse_markdown(filepath):
    """Parse markdown into structured sections."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove YAML frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)

    sections = []
    lines = text.split('\n')
    current_section = {"heading": "Introduction", "content": []}

    for line in lines:
        # Detect headings
        h_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if h_match:
            if current_section["content"]:
                sections.append(current_section)
            current_section = {"heading": h_match.group(2), "content": []}

            # Determine level
            level = len(h_match.group(1))
            if level <= 2:
                current_section["section_header"] = True
        else:
            current_section["content"].append(line)

    if current_section["content"]:
        sections.append(current_section)

    return sections


def sections_to_html(sections):
    """Convert parsed sections to HTML with sentence spans."""
    html_parts = []
    for sec in sections:
        heading_tag = "h2" if sec.get("section_header") else "h3"
        html_parts.append(f'<{heading_tag} class="section-heading">{sec["heading"]}</{heading_tag}>')

        text = '\n'.join(sec["content"]).strip()
        if not text:
            continue

        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for s in sentences:
            if s.strip():
                # Plain text version (for TTS)
                s_plain = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                # HTML formatted version
                s_html = s
                s_html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s_html)
                s_html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s_html)
                s_html = re.sub(r'`(.+?)`', r'<code>\1</code>', s_html)
                html_parts.append(f'<span class="sentence" data-text="{s_plain}">{s_html}</span> ')

    return '\n'.join(html_parts)


# ─── Gradio API caller ──────────────────────────────────────────
CHATTERBOX_API = "https://resembleai-chatterbox-turbo-demo.hf.space/gradio_api/call/generate"
# Default reference audio from the demo app
DEFAULT_REF_AUDIO = None  # Space uses its own default reference voice

def call_chatterbox_tts(text):
    """Call Chatterbox Turbo via Gradio SSE API. Returns audio URL."""
    # Step 1: POST to start generation, get event_id
    payload = {
        "data": [
            text,                                               # text
            DEFAULT_REF_AUDIO,                                   # reference audio (None = use default)
            0.8,                                                 # temperature
            0,                                                   # seed (0 = random)
            0.0,                                                 # min_p
            0.95,                                                # top_p
            1000,                                                # top_k
            1.2,                                                 # repetition_penalty
            True                                                 # normalize_loudness
        ],
        "event_data": None
    }

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        CHATTERBOX_API,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
        result = json.loads(resp.read())

    event_id = result.get("event_id")
    if not event_id:
        return None

    # Step 2: Stream SSE events until we get the complete event
    # ZERO GPU cold start can take 30-60s, so use a long timeout
    event_url = f"https://resembleai-chatterbox-turbo-demo.hf.space/gradio_api/call/generate/{event_id}"
    req2 = urllib.request.Request(event_url)

    with urllib.request.urlopen(req2, timeout=180, context=ctx) as resp2:
        buffer = b""
        while True:
            chunk = resp2.read(4096)
            if not chunk:
                break
            buffer += chunk
            data_str = buffer.decode('utf-8', errors='replace')

            # Look for the complete event with audio URL
            if 'event: complete' in data_str:
                # Response format: event: complete\ndata: [{"path":"...","url":"..."}]
                try:
                    # Extract JSON from the 'data:' line
                    json_match = re.search(r'data:\s*(\[.*?\])', data_str, re.DOTALL)
                    if json_match:
                        items = json.loads(json_match.group(1))
                        if items and isinstance(items, list) and len(items) > 0:
                            audio_url = items[0].get("url", "")
                            if audio_url:
                                return audio_url.replace('\\/', '/')
                except (json.JSONDecodeError, KeyError, IndexError):
                    pass
                break

            # Check for error
            if 'event: error' in data_str and len(data_str) < 200:
                # Could be a transient cold-start error, wait and retry
                pass

    return None


# ─── gTTS (Google TTS) — reliable fallback ─────────────────
def call_gtts(text):
    """Generate TTS audio via Google TTS. Returns a local WAV URL."""
    try:
        from gtts import gTTS
        import io, base64, uuid
        
        # Generate unique filename
        audio_id = str(uuid.uuid4())[:8]
        output_dir = os.path.join(os.path.dirname(__file__), "tts_cache")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"tts_{audio_id}.mp3")
        
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_path)
        
        return output_path
    except Exception as e:
        print(f"gTTS error: {e}")
        return None


# ─── Edge TTS (Microsoft Neural) — premium, free, always works ──
async def _edge_tts_async(text, output_path):
    """Async helper to generate Edge TTS audio."""
    import edge_tts
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
    await communicate.save(output_path)


def call_edge_tts(text):
    """Generate TTS audio via Microsoft Edge Neural TTS. Returns local path."""
    try:
        import asyncio, uuid
        audio_id = str(uuid.uuid4())[:8]
        output_dir = os.path.join(os.path.dirname(__file__), "tts_cache")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"edge_{audio_id}.mp3")
        
        asyncio.run(_edge_tts_async(text, output_path))
        
        if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
            return output_path
        return None
    except Exception as e:
        print(f"Edge TTS error: {e}")
        return None


# ─── HTTP Server ────────────────────────────────────────────────
HTML_PAGE = None

def get_html_page():
    global HTML_PAGE
    if HTML_PAGE:
        return HTML_PAGE

    with open(__file__.replace('.py', '.html'), 'r') as f:
        HTML_PAGE = f.read()
    return HTML_PAGE


class StudyHandler(http.server.BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _send_html(self, html):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())

    def _send_file(self, path):
        self.send_response(200)
        if path.endswith('.css'):
            self.send_header("Content-Type", "text/css")
        elif path.endswith('.js'):
            self.send_header("Content-Type", "application/javascript")
        elif path.endswith('.png'):
            self.send_header("Content-Type", "image/png")
        elif path.endswith('.woff2'):
            self.send_header("Content-Type", "font/woff2")
        else:
            self.send_header("Content-Type", "application/octet-stream")
        self.end_headers()
        with open(path, 'rb') as f:
            self.wfile.write(f.read())

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/":
            self._send_html(get_html_page())

        elif path == "/api/guides":
            self._send_json(list(GUIDES.values()))

        elif path.startswith("/api/guide/"):
            guide_path = urllib.parse.unquote(path[11:])
            guide_path = os.path.join(VAULT, guide_path)
            if os.path.exists(guide_path):
                sections = parse_markdown(guide_path)
                html = sections_to_html(sections)
                with open(guide_path, 'r', encoding='utf-8') as f:
                    raw = f.read()
                self._send_json({
                    "html": html,
                    "sections": sections,
                    "raw": raw,
                    "title": os.path.basename(guide_path).replace('.md', ''),
                })
            else:
                self._send_json({"error": "Guide not found"}, 404)

        elif path == "/api/tts":
            # Try Chatterbox first, fall back to gTTS
            text = parsed.query.split('=')[1] if '=' in parsed.query else ''
            text = urllib.parse.unquote(text)
            if not text or len(text) > 300:
                self._send_json({"error": "Text must be 1-300 chars"}, 400)
                return

            try:
                audio_url = call_chatterbox_tts(text)
                if audio_url:
                    self._send_json({"audio_url": audio_url, "source": "chatterbox"})
                    return
            except Exception as e:
                print(f"Chatterbox failed: {e}")

            # Fallback 1: Edge TTS (premium, always works)
            edge_path = call_edge_tts(text)
            if edge_path:
                self._send_json({"audio_url": edge_path, "source": "edge-tts"})
                return

            # Fallback 2: gTTS 
            audio_path = call_gtts(text)
            if audio_path:
                self._send_json({"audio_url": audio_path, "source": "gtts"})
            else:
                self._send_json({"error": "All TTS backends failed"}, 502)

        elif path == "/api/tts-chatterbox":
            # Pure Chatterbox (no fallback)
            text = parsed.query.split('=')[1] if '=' in parsed.query else ''
            text = urllib.parse.unquote(text)
            if not text or len(text) > 300:
                self._send_json({"error": "Text must be 1-300 chars"}, 400)
                return
            try:
                audio_url = call_chatterbox_tts(text)
                if audio_url:
                    self._send_json({"audio_url": audio_url})
                else:
                    self._send_json({"error": "Chatterbox returned no audio"}, 502)
            except Exception as e:
                self._send_json({"error": str(e)}, 502)

        elif path == "/api/tts-gtts":
            # Pure gTTS (Google TTS)
            text = parsed.query.split('=')[1] if '=' in parsed.query else ''
            text = urllib.parse.unquote(text)
            if not text or len(text) > 300:
                self._send_json({"error": "Text must be 1-300 chars"}, 400)
                return
            try:
                audio_path = call_gtts(text)
                if audio_path:
                    self._send_json({"audio_url": audio_path})
                else:
                    self._send_json({"error": "gTTS failed"}, 502)
            except Exception as e:
                self._send_json({"error": str(e)}, 502)

        elif path == "/api/tts-edge":
            # Pure Edge TTS (Microsoft Neural)
            text = parsed.query.split('=')[1] if '=' in parsed.query else ''
            text = urllib.parse.unquote(text)
            if not text or len(text) > 300:
                self._send_json({"error": "Text must be 1-300 chars"}, 400)
                return
            try:
                audio_path = call_edge_tts(text)
                if audio_path:
                    self._send_json({"audio_url": audio_path})
                else:
                    self._send_json({"error": "Edge TTS failed"}, 502)
            except Exception as e:
                self._send_json({"error": str(e)}, 502)

        elif path.startswith("/tts_cache/"):
            # Serve locally-generated TTS files (gTTS)
            filepath = os.path.join(os.path.dirname(__file__), path.lstrip('/'))
            if os.path.exists(filepath):
                self._send_file(filepath)
            else:
                self._send_json({"error": "File not found"}, 404)

        elif path.startswith("/gradio_api/file/"):
            # Proxy static audio files from Gradio
            gradio_url = f"https://resembleai-chatterbox-turbo-demo.hf.space{path}"
            try:
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
                req = urllib.request.Request(gradio_url)
                with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                    self.send_response(200)
                    self.send_header("Content-Type", resp.headers.get("Content-Type", "audio/wav"))
                    self.end_headers()
                    self.wfile.write(resp.read())
            except Exception as e:
                self._send_json({"error": str(e)}, 502)

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


def main():
    # Check Chatterbox availability
    chatterbox_ok = False
    try:
        test_url = "https://resembleai-chatterbox-turbo-demo.hf.space/gradio_api/info"
        req = urllib.request.Request(test_url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                chatterbox_ok = True
    except:
        pass

    print(f"\n{'='*60}")
    print(f"  📖 STUDY READER — Dyslexia-Friendly TTS Reader")
    print(f"{'='*60}")
    print(f"\n  🌐 Open: http://localhost:{PORT}")
    print(f"\n  📚 Available Guides:")
    for key, guide in sorted(GUIDES.items()):
        print(f"     • {guide['display']}")
    if chatterbox_ok:
        print(f"\n  🗣️  TTS: Chatterbox Turbo (AI voice)")
    else:
        print(f"\n  🗣️  TTS: Browser Speech API (Chatterbox server unavailable)")
    print(f"     Fallback: Browser Speech API")
    print(f"\n  ⏹️  Press Ctrl+C to stop\n{'='*60}\n")

    server = http.server.HTTPServer(("0.0.0.0", PORT), StudyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.server_close()


if __name__ == "__main__":
    main()
