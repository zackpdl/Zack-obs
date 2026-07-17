# 🏠 Mission Control

> *2026-07-17 • Friday — Week 29*

> *"Mission over mood. Consistency creates identity."*

---

## 🧠 Two Hemispheres

| Hemisphere | Location | Status |
|-----------|----------|--------|
| 🧑 Human | Inbox, Projects, Areas, Pillars, Daily Notes | 🟢 |
| 🤖 AI | [[30 - AI Outputs/README\|30 - AI Outputs]] | 🟢 Active |

---

## 🎯 Daily Focus

| # | Priority | Status |
|---| -------- | ------ |
| 1 | — | ⬜ |
| 2 | — | ⬜ |
| 3 | — | ⬜ |

### ⚡ Critical
- [ ] —

---

## 🏋️ Fitness

\1 Lower B (Posterior chain) *([[fitness]])**
\1 Easy / Recovery 2-3km *([[running]])**
**Nutrition:** 🥩 Protein — / 160g • 🔥 Calories — / 3,000

---

## 📚 Study

\1 Heritage + Data Viz *([[study]])**
**ITX3004 Quiz:** Jul 22 ← **5 days**
**Midterms:** Aug 4-10

---

## 📥 Inbox

```dataview
TABLE rows.file.link AS "Items"
FROM "00 - Inbox"
WHERE file.name != "Capture.md"
SORT file.mtime DESC
LIMIT 8
```

> [!tip] Capture anything here → [[00 - Inbox/Capture|Inbox Capture]]

---

## 📊 Correlation Intelligence

```dataview
TABLE
  workout AS "💪 Workout",
  study_hours AS "📚 Study",
  run_km AS "🏃 Run (km)",
  discipline_score AS "🎯 Disc.",
  energy AS "⚡",
  mood AS "😊",
  youtube_work AS "🎬"
FROM "Calendar/Daily"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

> *"Identify the 20% of actions that give 80% of results." — Eric*

---

## ✅ Daily Habits

| Habit | Today | Streak |
| ----- | ----- | ------ |
| 🏋️ Train | ⬜ | — |
| 🥩 Protein 160g | ⬜ | — |
| 📚 Study 45min | ⬜ | — |
| 🎬 Content 30min | ⬜ | — |
| 🇹🇭 Thai 15min | ⬜ | — |
| ⌨️ Typing 10min | ⬜ | — |
| 😴 Sleep by midnight | ⬜ | — |
| 🧘 No dopamine escape | ⬜ | — |

**Completion:** 0/8 (0%)

---

## 🤖 AI Hemisphere

| Task | Status |
|-----|--------|
| Study guides | ✅ 4 guides created |
| TTS Reader | ✅ Active at [[../scripts/study_reader\|localhost:8765]] |
| Upcoming | — |

> [!info] AI outputs are in [[30 - AI Outputs/README\|30 - AI Outputs]] — kept separate from your thoughts.

---

## 🗺️ Pillars

| Area | File | Status |
|------|------|--------|
| 🏋️ Fitness | [[fitness]] | ⏳ |
| 🏃 Running | [[running]] | ⏳ |
| 📚 Study | [[study]] | ⏳ |
| 🇹🇭 Thai | [[thai]] | ⏳ |
| ⌨️ Typing | [[typing]] | ⏳ |
| 🎬 YouTube | [[youtube]] | ⏳ |
| 🧘 Monk Mode | [[monk_mode]] | ⏳ |
| 📓 Journal | [[journal]] | ⏳ |

---

## 📂 Active Projects

```dataview
TABLE file.name AS "Project", file.mtime AS "Modified"
FROM "10 - Projects"
WHERE file.name != "index.md"
SORT file.mtime DESC
LIMIT 8
```

---

## 📖 Study Reader

🎧 **TTS Reader** → `study-reader` in terminal or http://localhost:8765
- Toggle between 🔊 Browser TTS and 🤖 Chatterbox Turbo
- Sentence / word highlighting with dyslexia-friendly design

---

*Last auto-updated: {{date:YYYY-MM-DD HH:mm}}*
