#!/usr/bin/env python3
"""Daily Mission Control Dashboard updater — EMAI format.
Idempotent. Replaces: header (week/day/date), training, run, study."""

import re
from datetime import datetime

HOME_PATH = "/Users/zackpdl/Documents/Obsidian/Zack-obs/Home.md"

today = datetime.now()
dow = today.strftime("%A")
datestr = today.strftime("%Y-%m-%d")
wk = today.isocalendar()[1]

training = {"Monday":"Upper A (Chest focus)","Tuesday":"Lower A (Quad focus)",
            "Wednesday":"Rest / Active recovery","Thursday":"Upper B (Back focus)",
            "Friday":"Lower B (Posterior chain)","Saturday":"Accessories / Weak point",
            "Sunday":"Rest"}.get(dow,"Rest")

run = {"Monday":"Easy / Recovery 2-3km","Wednesday":"Speed / Tempo 3-5km",
       "Friday":"Easy / Recovery 2-3km","Saturday":"Long run 5-8km"}.get(dow,"Rest day")

study = {"Monday":"Blockchain (ITX4518)","Tuesday":"Data Viz (CSX4601)",
         "Wednesday":"Info Systems (ITX3004)","Thursday":"Data Viz + Info Systems",
         "Friday":"Heritage + Data Viz","Saturday":"Info Systems deep-dive (ITX3004)",
         "Sunday":"Catch-up / Review"}.get(dow,"Review")

with open(HOME_PATH,"r") as f: content = f.read()

# 1. Header: > *Week N • Day • YYYY-MM-DD*
content = re.sub(r'^> \*Week \d+ • [^*]+ • [^*]+\*$',
                 f'> *Week {wk} • {dow} • {datestr}*',
                 content, count=1, flags=re.MULTILINE)

# 2. Training
content = re.sub(r'(\[\[Pillars/fitness\\\|)[^]]*(\]\])',
                 rf'\1{training}\2', content)

# 3. Run
content = re.sub(r'(\[\[Pillars/running\\\|)[^]]*(\]\])',
                 rf'\1{run}\2', content)

# 4. Study
content = re.sub(r'(\[\[Pillars/study\\\|)[^]]*(\]\])',
                 rf'\1{study}\2', content)

with open(HOME_PATH,"w") as f: f.write(content)

print(f"✅ DASHBOARD UPDATED: {datestr} ({dow} — Week {wk})")
print(f"   Training: {training}")
print(f"   Run: {run}")
print(f"   Study: {study}")
