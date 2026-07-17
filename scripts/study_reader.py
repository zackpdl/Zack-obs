#!/usr/bin/env python3
"""Study Reader Server — dyslexia-friendly TTS reader for study guides.
Loads study guides from your vault, serves a beautiful reader with
sentence-by-sentence highlighting and AI TTS (ElevenLabs premium + Edge fallback)."""

import http.server
import json
import os
import re
import ssl
import threading
import urllib.request
import urllib.parse
import time
import hashlib
from pathlib import Path

VAULT = os.path.expanduser("~/Documents/Obsidian/Zack-obs")
PORT = 8765
ELEVENLABS_API_KEY = "sk_7d864d9b3e803e231afbd0e75c7d60e1d6f691bbc7036ed3"
ELEVENLABS_VOICE = "21m00Tcm4TlvDq8ikWAM"  # Rachel (popular, clear female)
TTS_CACHE_DIR = os.path.join(os.path.dirname(__file__), "tts_cache")
os.makedirs(TTS_CACHE_DIR, exist_ok=True)

# ─── Guide Registry ─────────────────────────────────────────────
GUIDES = {}
pattern = re.compile(r"^00 - .* Study Guide")
for fpath in Path(VAULT).rglob("*.md"):
    if pattern.match(fpath.name):
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
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    sections = []
    lines = text.split('\n')
    current_section = {"heading": "Introduction", "content": []}
    for line in lines:
        h_match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if h_match:
            if current_section["content"]:
                sections.append(current_section)
            current_section = {"heading": h_match.group(2), "content": []}
            if len(h_match.group(1)) <= 2:
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
        sentences = re.split(r'(?<=[.!?])\s+', text)
        for s in sentences:
            if s.strip():
                s_plain = s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                s_html = s
                s_html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s_html)
                s_html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s_html)
                s_html = re.sub(r'`(.+?)`', r'<code>\1</code>', s_html)
                html_parts.append(f'<span class="sentence" data-text="{s_plain}">{s_html}</span> ')
    return '\n'.join(html_parts)

# ─── ElevenLabs TTS (with caching) ──────────────────────────────
def call_elevenlabs(text):
    """Generate TTS via ElevenLabs API with disk caching.
    Same text → same cached file (uses MD5 hash). Never re-bills the same sentence."""
    text_hash = hashlib.md5(text.encode()).hexdigest()[:16]
    cache_path = os.path.join(TTS_CACHE_DIR, f"el_{text_hash}.mp3")

    # ✅ Cache hit — return instantly, no API call
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 500:
        return cache_path

    # ❌ Cache miss — call ElevenLabs API
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE}"
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": ELEVENLABS_API_KEY,
        }
        payload = {
            "text": text,
            "model_id": "eleven_turbo_v2_5",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
            }
        }
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            audio_data = resp.read()

        if len(audio_data) > 500:
            with open(cache_path, "wb") as f:
                f.write(audio_data)
            return cache_path
        return None
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"ElevenLabs HTTP {e.code}: {body[:200]}")
        return None
    except Exception as e:
        print(f"ElevenLabs error: {e}")
        return None

# ─── Edge TTS (Microsoft Neural) — free fallback ────────────────
async def _edge_tts_async(text, output_path):
    import edge_tts
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
    await communicate.save(output_path)

def call_edge_tts(text):
    try:
        import asyncio, uuid
        audio_id = str(uuid.uuid4())[:8]
        output_path = os.path.join(TTS_CACHE_DIR, f"edge_{audio_id}.mp3")
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
        ext = os.path.splitext(path)[1].lower()
        mime = {
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.png': 'image/png',
            '.woff2': 'font/woff2',
            '.mp3': 'audio/mpeg',
            '.wav': 'audio/wav',
        }
        self.send_header("Content-Type", mime.get(ext, "application/octet-stream"))
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
            # Primary: ElevenLabs (premium, cached). Fallback: Edge TTS (free)
            text = parsed.query.split('=')[1] if '=' in parsed.query else ''
            text = urllib.parse.unquote(text)
            if not text or len(text) > 300:
                self._send_json({"error": "Text must be 1-300 chars"}, 400)
                return

            # Try ElevenLabs (cached — won't re-bill)
            audio_path = call_elevenlabs(text)
            if audio_path:
                self._send_json({"audio_url": audio_path, "source": "elevenlabs"})
                return

            # Fallback: Edge TTS (free, always works)
            edge_path = call_edge_tts(text)
            if edge_path:
                self._send_json({"audio_url": edge_path, "source": "edge-tts"})
            else:
                self._send_json({"error": "All TTS backends failed"}, 502)

        elif path == "/api/tts-elevenlabs":
            # Pure ElevenLabs (no fallback)
            text = parsed.query.split('=')[1] if '=' in parsed.query else ''
            text = urllib.parse.unquote(text)
            if not text or len(text) > 300:
                self._send_json({"error": "Text must be 1-300 chars"}, 400)
                return
            audio_path = call_elevenlabs(text)
            if audio_path:
                self._send_json({"audio_url": audio_path})
            else:
                self._send_json({"error": "ElevenLabs failed"}, 502)

        elif path == "/api/tts-edge":
            # Pure Edge TTS
            text = parsed.query.split('=')[1] if '=' in parsed.query else ''
            text = urllib.parse.unquote(text)
            if not text or len(text) > 300:
                self._send_json({"error": "Text must be 1-300 chars"}, 400)
                return
            audio_path = call_edge_tts(text)
            if audio_path:
                self._send_json({"audio_url": audio_path})
            else:
                self._send_json({"error": "Edge TTS failed"}, 502)

        elif path.startswith("/tts_cache/"):
            filepath = os.path.join(os.path.dirname(__file__), path.lstrip('/'))
            if os.path.exists(filepath):
                self._send_file(filepath)
            else:
                self._send_json({"error": "File not found"}, 404)

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
    print(f"\n{'='*60}")
    print(f"  📖 STUDY READER — Dyslexia-Friendly TTS Reader")
    print(f"{'='*60}")
    print(f"\n  🌐 Open: http://localhost:{PORT}")
    print(f"\n  📚 Available Guides:")
    for key, guide in sorted(GUIDES.items()):
        print(f"     • {guide['display']}")
    print(f"\n  🗣️  TTS Engines:")
    print(f"     🤖 ElevenLabs (premium, cached) — uses API credits once per sentence")
    print(f"     🤖 Edge (Microsoft Neural, free fallback)")
    print(f"     🔊 Browser (Web Speech API)")
    print(f"\n  ⏹️  Press Ctrl+C to stop\n{'='*60}\n")

    server = http.server.HTTPServer(("0.0.0.0", PORT), StudyHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.server_close()

if __name__ == "__main__":
    main()
