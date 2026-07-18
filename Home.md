# 🏠 Mission Control

> *Week 29 · Saturday · 2026-07-18*
> *"University is non-negotiable. Consistency creates identity."*

---
## 🚀 Nav
[[Kanban/Mission Control|🎯 Mission]] · [[Kanban/Semester 1-2026|📚 Semester]] · [[00 - Inbox/Capture|📥 Inbox]] · [[30 - AI Outputs/README|🤖 AI]] · [[Pillars/fitness|🏋️]] [[Pillars/study|📖]] [[Pillars/youtube|🎬]] · [📖 Reader](http://localhost:8765)

---
## ⚠️ Deadlines
| When | What | Priority | Left |
|------|------|----------|------|
| Jul 22 | **ITX3004 Quiz 1 (5%)** | 🟠 HIGH | 5d |
| Aug 04 | **Midterms (Aug 4-10)** | 🔵 Exam | 18d |
| Sep 30 | **Finals (Sep 30 - Oct 12)** | ⏳ Soon | 75d |

---
## 🎯 Today's Top 3

| # | Action | Priority |
|---|--------|----------|
| 1 | 📚 Study: Info Systems deep-dive (ITX3004) | High |
| 2 | 🏋️ Train: Accessories / Weak point | Medium |
| 3 | 🏃 Run: Long run 5-8km | Medium |

> *"What are the 3 highest-leverage actions I can take today?"*

---
## 📊 7-Day Correlation

```dataview
TABLE
  workout AS "💪",
  run_km AS "🏃km",
  study_hours AS "📚h",
  discipline_score AS "🎯",
  energy AS "⚡",
  mood AS "😊",
  sleep_hours AS "😴",
  protein_g AS "🥩g",
  youtube_work AS "🎬",
  thai_practice AS "🇹🇭",
  typing_practice AS "⌨️"
FROM "Calendar/Daily"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

> *Find the 20% of actions driving 80% of your results. When you sleep 7+ hours, is your discipline score higher? When you train, do you study better?*

---
## 🗺️ Pillars
| 🏋️ [[Pillars/fitness|Fitness]] | 🏃 [[Pillars/running|Running]] | 📚 [[Pillars/study|Study]] | 🇹🇭 [[Pillars/thai|Thai]] |
|:---:|:---:|:---:|:---:|
| ⏳ | ⏳ | ⏳ | ⏳ |
| ⌨️ [[Pillars/typing|Typing]] | 🎬 [[Pillars/youtube|YouTube]] | 🧘 [[Pillars/monk_mode|Monk Mode]] | 📓 [[Pillars/journal|Journal]] |
|:---:|:---:|:---:|:---:|
| ⏳ | ⏳ | ⏳ | ⏳ |

---
## 📥 Inbox
```dataview
TABLE file.mtime AS "When"
FROM "00 - Inbox"
WHERE file.name != "Capture.md"
SORT file.mtime DESC
LIMIT 4
```

---
## 🤖 AI Hemisphere
| Task | Status |
|------|--------|
| 4 Study Guides | ✅ |
| TTS Reader | ✅ localhost:8765 |
| ITX3004 Quiz Prep | 🟠 |
| Vault Upgrades | 🟠 |

---
## 📂 Active
```dataview
TABLE file.mtime AS "Modified"
FROM "10 - Projects"
WHERE file.name != "index.md"
SORT file.mtime DESC
LIMIT 4
```

---
> *💡 Tip: Create today's note from "Daily Note" template → frontmatter populates the correlation table above.*
