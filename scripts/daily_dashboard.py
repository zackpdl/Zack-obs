#!/usr/bin/env python3
"""Daily Mission Control Dashboard updater.
Idempotent — safe to run daily. Replaces date, training, run, and study fields."""

import os, re
from datetime import datetime

VAULT = os.path.expanduser("~/Documents/Obsidian/Zack-obs/")
HOME_PATH = os.path.join(VAULT, "Home.md")

today = datetime.now()
day_name = today.strftime("%A")
date_str = today.strftime("%Y-%m-%d")

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

# Replace date line: > *anything*
content = re.sub(
    r"^> \*[^*]+\*$",
    f"> *{date_str} • {day_name}*",
    content,
    count=1,
    flags=re.MULTILINE,
)

# Replace: **Today's Training:** \n - anything
content = re.sub(
    r"(\*\*Today's Training:\*\*)\n- .*",
    f"\\1\n- {today_training} *(check [[fitness]] for plan)*",
    content,
)

# Replace: **Running:** \n - anything
content = re.sub(
    r"(\*\*Running:\*\*)\n- .*",
    f"\\1\n- {today_run} *(check [[running]] for schedule)*",
    content,
)

# Replace: **Subject:** anything
content = re.sub(
    r"(\*\*Subject:\*\*) .*",
    f"\\1 {today_study}",
    content,
)

with open(HOME_PATH, "w") as f:
    f.write(content)

print(f"✅ DASHBOARD UPDATED: {date_str} ({day_name})")
print(f"   Training: {today_training}")
print(f"   Run: {today_run}")
print(f"   Study: {today_study}")
