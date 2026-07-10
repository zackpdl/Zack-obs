#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional


ROOT = Path(__file__).resolve().parent
DASHBOARD = ROOT / "bookmark-dashboard.md"


@dataclass
class Bookmark:
    title: str
    url: str
    saved: str
    tags: List[str]


def _parse_frontmatter(text: str) -> dict:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}
    fm_lines = lines[1:end]
    data: dict = {}
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i].strip()
        if not line:
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"')
        if value == "":
            if key == "tags":
                tags: List[str] = []
                i += 1
                while i < len(fm_lines):
                    tline = fm_lines[i].strip()
                    if not tline.startswith("-"):
                        break
                    tags.append(tline.lstrip("-").strip().strip('"'))
                    i += 1
                data[key] = tags
                continue
        if key == "tags":
            if value in ("[]", "[ ]"):
                data[key] = []
            else:
                data[key] = [value]
        else:
            data[key] = value
        i += 1
    return data


def _parse_title_and_url(text: str) -> tuple[Optional[str], Optional[str]]:
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            match = re.match(r"#\s+\[(.+?)\]\((.+?)\)", line)
            if match:
                return match.group(1), match.group(2)
    return None, None


def _parse_bookmark(path: Path) -> Optional[Bookmark]:
    text = path.read_text(encoding="utf-8")
    fm = _parse_frontmatter(text)
    title = fm.get("title")
    url = fm.get("source")
    if not title or not url:
        alt_title, alt_url = _parse_title_and_url(text)
        title = title or alt_title
        url = url or alt_url
    saved = fm.get("saved")
    if not title or not url or not saved:
        return None
    tags = fm.get("tags")
    if tags is None:
        tags = []
    return Bookmark(title=title, url=url, saved=saved, tags=tags)


def _iter_bookmarks() -> Iterable[Bookmark]:
    for path in sorted(ROOT.glob("*.md")):
        if path == DASHBOARD:
            continue
        bm = _parse_bookmark(path)
        if bm:
            yield bm


def _sort_key(bm: Bookmark):
    try:
        return datetime.strptime(bm.saved, "%Y-%m-%d")
    except ValueError:
        return datetime.min


def _render(bookmarks: List[Bookmark]) -> str:
    lines: List[str] = []
    lines.append("# Bookmark Dashboard")
    lines.append("")
    lines.append("All bookmarks appear below. Click any title to open the page.")
    lines.append("")
    lines.append("## All Bookmarks")
    lines.append("")
    lines.append("| Date Added | Title | Tags |")
    lines.append("| --- | --- | --- |")
    for bm in bookmarks:
        tags = bm.tags if bm.tags else ["Untagged"]
        tag_str = ", ".join(f"`{t}`" for t in tags)
        lines.append(f"| {bm.saved} | [{bm.title}]({bm.url}) | {tag_str} |")
    lines.append("")
    lines.append("## By Tag")
    lines.append("")
    tags_map: dict[str, List[Bookmark]] = {}
    for bm in bookmarks:
        tags = bm.tags if bm.tags else ["Untagged"]
        for t in tags:
            tags_map.setdefault(t, []).append(bm)
    for tag in sorted(tags_map.keys(), key=str.lower):
        lines.append(f"### {tag}")
        for bm in tags_map[tag]:
            lines.append(f"- {bm.saved}: [{bm.title}]({bm.url})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    bookmarks = list(_iter_bookmarks())
    bookmarks.sort(key=_sort_key, reverse=True)
    output = _render(bookmarks)
    DASHBOARD.write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
