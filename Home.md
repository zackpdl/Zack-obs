# 🏠 Mission Control

> *Week 29 • Friday • 2026-07-17*

---

## 🚀 Quick Actions

| [▶ Start Day](https:///) | [⏹ Close Day](https:///) | [🔬 Research Task](https:///) | [📋 Plan Something](https:///) | [📖 TTS Study Reader](http://localhost:8765) |
|---|---|---|---|---|

---

## 🎯 Today's Focus

| # | Priority | ⏱ |
|---|---|---|
| 1 | — | — |
| 2 | — | — |
| 3 | — | — |

### ⚡ One Critical Task
- [ ] —

---

## 📊 Key Metrics

| 🏋️ Training | 🏃 Run | 📚 Study Focus | 🎯 Discipline | ✅ Habits |
|---|---|---|---|---|
| [[Pillars/fitness\|Lower B (Posterior chain)]] | [[Pillars/running\|Easy / Recovery 2-3km]] | [[Pillars/study\|Heritage + Data Viz]] | — / 10 | ▰▰▰▰▰▰▰▰▰▰ 0% |

---

## 📈 Last 7 Days — Correlation Intelligence

```dataview
TABLE
  workout AS "💪",
  run_km AS "🏃 km",
  study_hours AS "📚 h",
  discipline_score AS "🎯",
  energy AS "⚡",
  mood AS "😊",
  sleep_hours AS "😴",
  protein_g AS "🥩"
FROM "Calendar/Daily"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

> *Track these daily → find the 20% that drives 80% of your results.*

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
|---|---|
| Study guides | ✅ 4 |
| TTS Reader | ✅ Active |
| — | ⬜ |

> [!info] AI lives in [[30 - AI Outputs/README\|30 - AI Outputs]] — always separate from your thoughts

---

## 🗺️ Pillars

| Pillar | Status | Pillar | Status |
|---|---|---|---|
| 🏋️ [[Pillars/fitness\|Lower B (Posterior chain)]] | ⏳ | 🇹🇭 [[Pillars/thai\|Thai]] | ⏳ |
| 🏃 [[Pillars/running\|Easy / Recovery 2-3km]] | ⏳ | ⌨️ [[Pillars/typing\|Typing]] | ⏳ |
| 📚 [[Pillars/study\|Heritage + Data Viz]] | ⏳ | 🎬 [[Pillars/youtube\|YouTube]] | ⏳ |
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

## 📅 Deadlines

| Date | Event |
|---|---|
| Jul 22 | ITX3004 Quiz 1 (5%) |
| Aug 4-10 | Midterms |
| Sep 30 - Oct 12 | Finals |

---

> *Mission over mood. Consistency creates identity.*
