# 🏠 Mission Control

> *Week {{date:ww}} · {{date:dddd}} · {{date:YYYY-MM-DD}}*

---

## 🚀 Quick Actions
[[Brain]] [[Personal]]

| [[Kanban/Mission Control\|🎯 Mission Ctrl]] | [[Kanban/Semester 1-2026\|📚 Semester]] | [⏹ Close Day](https:///) | [📖 Study Reader](http://localhost:8765) | [📥 Inbox](00-Inbox/Capture.md) |
|---|---|---|---|---|

---

## 🔴 CRITICAL — No Items

> *No assignments due within 3 days.* ✅

## 🟠 HIGH PRIORITY

| Item | Days Left |
|------|-----------|
| ⚠️ **ITX3004 Quiz 1 (5%)** — Jul 22 | 5 |
| 🟠 Midterms — Aug 4-10 | 18 |

## 🟡 UPCOMING (14 days)

| Exam | Date | Priority |
|------|------|----------|
| ITX3004 Quiz | Jul 22 | 🟠 HIGH |
| Midterms | Aug 4-10 | 🔵 Exam |

---

## 🎯 Today's Top 3

```dataview
TABLE WITHOUT ID
  choice(study_hours > 0, "📚 Study: " + study_courses, "") AS "Priority 1",
  choice(workout != "", "🏋️ " + workout, "") AS "Priority 2",
  choice(youtube_work, "🎬 Content work", "") AS "Priority 3"
FROM "Calendar/Daily"
WHERE date = date(today)
```

> *If empty, create today's note using the "Daily Note" template and fill in your priorities.*

---

## 📊 Kanban Boards — Active Status

| Board | To Do | In Progress | Done |
|-------|-------|-------------|------|
| [[Kanban/Mission Control\|🎯 Mission Control]] | ⬜ Check it | 🔄 Check it | ✅ Check it |
| [[Kanban/Semester 1-2026\|📚 Semester]] | ⬜ Check it | 🔄 Check it | ✅ Check it |

> [!tip] Open [[Kanban/Mission Control]] to see every active card organized by lane

---

## 📈 Correlation Intelligence — Last 7 Days

```dataview
TABLE
  workout AS "💪",
  run_km AS "🏃 km",
  study_hours AS "📚 hrs",
  study_courses AS "📖",
  discipline_score AS "🎯",
  energy AS "⚡",
  mood AS "😊",
  stress AS "😰",
  sleep_hours AS "😴",
  sleep_quality AS "💤",
  protein_g AS "🥩",
  calories AS "🔥",
  youtube_work AS "🎬",
  thai_practice AS "🇹🇭",
  typing_practice AS "⌨️"
FROM "Calendar/Daily"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

> *Track these daily → find the 20% that drives 80% of your results.*

**💡 Insights:** *(AI-generated weekly)*
> *Look at the past 7 days. On days you exercised, did you study better? On days you slept 7+ hours, was your discipline score higher? Find patterns.*

---

## 📅 Deadlines

| Date | Event | Priority | Days Left |
|------|-------|----------|-----------|
| Jul 22 | **ITX3004 Quiz 1 (5%)** | 🟠 HIGH | 5 |
| Aug 04 | **Midterms (Aug 4-10)** | 🔵 Exam | 18 |
| Sep 30 | **Finals (Sep 30 - Oct 12)** | ⏳ Soon | 75 |

---

## 📥 Inbox

```dataview
TABLE file.name AS "Item", file.mtime AS "When"
FROM "00 - Inbox"
WHERE file.name != "Capture.md"
SORT file.mtime DESC
LIMIT 5
```

> [!tip] [[00 - Inbox/Capture|➕ Capture something]] — then process during review

---

## 🤖 AI Hemisphere

| Task | Status |
|------|--------|
| Study guides (4 created) | ✅ Done |
| TTS Study Reader | ✅ Active at localhost:8765 |
| ITX3004 Quiz prep | 🟠 In progress |
| Kanban boards | 🆕 Active |
| Daily note template | ✅ Updated |
| Vault upgrades | 🟠 In progress |

> [!info] AI lives in [[30 - AI Outputs/README|30 - AI Outputs]] — always separate from your thoughts

---

## 🗺️ Pillars

| Pillar | Status | Pillar | Status |
|--------|--------|--------|--------|
| 🏋️ [[Pillars/fitness\|Fitness]] | ⏳ | 🇹🇭 [[Pillars/thai\|Thai]] | ⏳ |
| 🏃 [[Pillars/running\|Running]] | ⏳ | ⌨️ [[Pillars/typing\|Typing]] | ⏳ |
| 📚 [[Pillars/study\|Study]] | ⏳ | 🎬 [[Pillars/youtube\|YouTube]] | ⏳ |
| 🧘 [[Pillars/monk_mode\|Monk Mode]] | ⏳ | 📓 [[Pillars/journal\|Journal]] | ⏳ |

---

## 📂 Active Projects

```dataview
TABLE file.name AS "Project", file.mtime AS "Modified"
FROM "10 - Projects"
WHERE file.name != "index.md"
SORT file.mtime DESC
LIMIT 6
```

---

## 📝 Latest Notes

```dataview
TABLE file.ctime AS "Created"
FROM ""
WHERE file.ctime >= date(today) - dur(3 days)
SORT file.ctime DESC
LIMIT 5
```

---

## 🔗 Weekly Review

```dataview
CALENDAR
FROM "Calendar/Daily"
WHERE date >= date(today) - dur(14 days)
```

> [!info] Run the weekly review every Sunday to analyze correlations.

> *"What are the 3 highest-leverage actions Zack can take today to improve his degree, health, and future?"*
>
> *University is non-negotiable. Consistency creates identity.*
