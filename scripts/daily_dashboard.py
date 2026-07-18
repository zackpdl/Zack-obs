#!/usr/bin/env python3
"""Daily Mission Control Dashboard updater — EMAI compact format."""
import os, re
from datetime import datetime

VAULT = os.path.expanduser("~/Documents/Obsidian/Zack-obs/")
HOME_PATH = os.path.join(VAULT, "Home.md")

today = datetime.now()
day_name = today.strftime("%A")
date_str = today.strftime("%Y-%m-%d")
week_num = today.isocalendar()[1]

training_map = {
    "Monday":    "Upper A (Chest focus)",
    "Tuesday":   "Lower A (Quad focus)",
    "Wednesday": "Rest / Active recovery",
    "Thursday":  "Upper B (Back focus)",
    "Friday":    "Lower B (Posterior chain)",
    "Saturday":  "Accessories / Weak point",
    "Sunday":    "Rest",
}
run_map = {
    "Monday":    "Easy / Recovery 2-3km",
    "Wednesday": "Speed / Tempo 3-5km",
    "Friday":    "Easy / Recovery 2-3km",
    "Saturday":  "Long run 5-8km",
}
study_map = {
    "Monday":    "Blockchain (ITX4518)",
    "Tuesday":   "Data Viz (CSX4601)",
    "Wednesday": "Info Systems (ITX3004)",
    "Thursday":  "Data Viz + Info Systems",
    "Friday":    "Heritage + Data Viz",
    "Saturday":  "Info Systems deep-dive (ITX3004)",
    "Sunday":    "Catch-up / Review",
}

today_training = training_map.get(day_name, "Rest")
today_run = run_map.get(day_name, "Rest day")
today_study = study_map.get(day_name, "Review")

with open(HOME_PATH, "r") as f:
    content = f.read()

# Update header line
content = re.sub(
    r'^> \*Week .*?\*$',
    f"> *Week {week_num} · {day_name} · {date_str}*",
    content,
    count=1,
    flags=re.MULTILINE,
)

# Update Today's Top 3 rows — simple line-by-line replacement
lines = content.split('\n')
for i, line in enumerate(lines):
    # Study row: | 1 | 📚 Study: SOMETHING | High |
    if re.match(r'^\| 1 \| 📚 Study: ', line):
        lines[i] = f"| 1 | 📚 Study: {today_study} | High |"
    # Training row: | 2 | 🏋️ Train: SOMETHING | Medium |
    elif re.match(r'^\| 2 \| 🏋️ Train: ', line):
        lines[i] = f"| 2 | 🏋️ Train: {today_training} | Medium |"
    # Run row: | 3 | 🏃 Run: SOMETHING | Medium |
    elif re.match(r'^\| 3 \| 🏃 Run: ', line):
        lines[i] = f"| 3 | 🏃 Run: {today_run} | Medium |"

content = '\n'.join(lines)

with open(HOME_PATH, "w") as f:
    f.write(content)

print(f"✅ DASHBOARD: {date_str} ({day_name} — W{week_num})")
print(f"   📚 {today_study}")
print(f"   🏋️ {today_training}")
print(f"   🏃 {today_run}")
