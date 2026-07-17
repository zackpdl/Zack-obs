#!/usr/bin/env python3
"""Deadline Monitor — checks assignment/exam dates and updates Home.md priority sections.
Runs daily at 7AM alongside daily_dashboard.py.

Rules:
- Due within 3 days  → CRITICAL section
- Due within 7 days  → HIGH PRIORITY section  
- Due within 14 days → UPCOMING section
- Due within 30 days → exam countdown
"""

import re
from datetime import datetime, date

HOME_PATH = "/Users/zackpdl/Documents/Obsidian/Zack-obs/Home.md"

# ── Define all known deadlines ──
DEADLINES = [
    {"name": "ITX3004 Quiz 1 (5%)", "due": date(2026, 7, 22), "type": "quiz"},
    {"name": "Midterms (Aug 4-10)", "due": date(2026, 8, 4), "type": "exam"},
    {"name": "Finals (Sep 30 - Oct 12)", "due": date(2026, 9, 30), "type": "exam"},
]

today = date.today()

# ── Categorize ──
critical = []   # ≤ 3 days
high = []       # 4-7 days
upcoming = []   # 8-14 days
exam_soon = []  # ≤ 30 days (exams only)

for d in DEADLINES:
    delta = (d["due"] - today).days
    if delta < 0:
        continue  # past due, skip
    if delta <= 3:
        critical.append(d)
    elif delta <= 7:
        high.append(d)
    elif delta <= 14:
        upcoming.append(d)
    if d["type"] == "exam" and delta <= 30:
        exam_soon.append(d)

# ── Read current Home.md ──
with open(HOME_PATH, "r") as f:
    content = f.read()

# ── Update 🔴 CRITICAL section ──
if critical:
    items = "\n".join(f"> **⛔ {d['name']} — Due in {(d['due']-today).days} days. Drop everything.**" for d in critical)
    study_block = []
    for d in critical:
        days_left = (d["due"] - today).days
        study_block.append(f"### Critical: {d['name']} (Due in {days_left} days)")
        study_block.append("```")
        study_block.append("Recommended completion plan:")
        days = max(days_left, 1)
        for i in range(days):
            day_str = f"Day {i+1} ({(today + __import__('datetime').timedelta(days=i)).strftime('%a %b %d')})"
            study_block.append(f"  {day_str}: Dedicate 2+ hours to focused study")
        study_block.append("```")
    critical_block = "\n".join(study_block)
else:
    critical_block = "> *No assignments due within 3 days.* ✅"

# Replace CRITICAL section (between headers)
content = re.sub(
    r"## 🔴 CRITICAL.*?(?=## 🟠|## 🎯)",
    f"## 🔴 CRITICAL — {'⚠️ ' + critical[0]['name'] + ' — URGENT' if critical else 'No Items'}\n\n{critical_block}\n\n",
    content,
    count=1,
    flags=re.DOTALL,
)

# ── Update 🟠 HIGH PRIORITY section ──
if high:
    items = []
    for d in high:
        days_left = (d["due"] - today).days
        items.append(f"- **⚠️ {d['name']}** — Due in {days_left} days. Elevate to Critical if not started.")
    high_block = "\n".join(items)
else:
    high_block = "> *No assignments due within 7 days.* ✅"

content = re.sub(
    r"## 🟠 HIGH PRIORITY.*?(?=## 🔴|## 🎯)",
    f"## 🟠 HIGH PRIORITY\n\n{high_block}\n\n",
    content,
    count=1,
    flags=re.DOTALL,
)

# ── Update 📅 Deadlines table ──
# Find the deadlines table section and rebuild it
table_rows = []
for d in DEADLINES:
    delta = (d["due"] - today).days
    if delta < 0:
        continue
    if delta <= 3:
        priority = "🔴 CRITICAL"
    elif delta <= 7:
        priority = "🟠 HIGH"
    elif delta <= 14:
        priority = "🟡 Upcoming"
    elif d["type"] == "exam" and delta <= 30:
        priority = "🔵 Exam soon"
    else:
        priority = "—"
    table_rows.append(f"| {d['due'].strftime('%b %d')} | **{d['name']}** | {priority} | {delta} |")

new_table = "| Date | Event | Priority | Days Left |\n|---|---|---|---|\n" + "\n".join(table_rows) + "\n"

content = re.sub(
    r"\| Date \| Event \| Priority \| Days Left \|.*?(?=---\n\n## 📥)",
    new_table,
    content,
    count=1,
    flags=re.DOTALL,
)

with open(HOME_PATH, "w") as f:
    f.write(content)

print(f"✅ DEADLINES UPDATED ({today})")
print(f"   Critical: {[d['name'] for d in critical] or 'None'}")
print(f"   High priority: {[d['name'] for d in high] or 'None'}")
print(f"   Upcoming: {[d['name'] for d in upcoming] or 'None'}")
