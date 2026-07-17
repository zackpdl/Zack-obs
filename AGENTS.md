# EMAI — Enhanced Mind & AI Integration

You are interacting with **Zack Pdl's** personal knowledge management vault. This file serves as your onboarding and operating instructions.

---

## 🧭 Vault Map

```
/ (root) — ...
├── AGENTS.md           ← You are here (instruction file)
├── Home.md             ← Daily Mission Control Dashboard
├── Pillars/            ← Your 8 transformation pillars
│   ├── fitness.md      ← Body metrics & training logs
│   ├── running.md      ← 5K → 10K → Half marathon goals
│   ├── study.md        ← University semester overview & progress
│   ├── typing.md       ← 80+ WPM accuracy goals
│   ├── thai.md         ← Thai language learning
│   ├── youtube.md      ← Content creation pillar (100 uploads)
│   ├── monk_mode.md    ← Discipline system & dopamine management
│   └── journal.md      ← Daily reflection template
│
├── 00 - Inbox/         ← HUMAN CAPTURE: raw ideas, quick notes (GTD)
├── 10 - Projects/      ← Active projects (uni courses, etc.)
├── 20 - Areas/         ← Health, University, Thai, etc.
├── 30 - AI Outputs/    ← AI-GENERATED: everything AI creates lives here
├── 40 - Archives/      ← Past projects & courses
├── Calendar/           ← Daily notes & logs
├── Templates/          ← Note templates
├── Attachments/        ← Images, PDFs, binaries
└── scripts/            ← Automation (Hermes cron scripts)
```

---

## ⚖️ Core Rule: Human / AI Separation

This vault is a **second brain with two hemispheres**:

### 🧠 Human Side (YOUR thoughts)
- `00 - Inbox/` — Raw captures, ideas, things to process later
- `10 - Projects/` — Your active university projects
- `20 - Areas/` — Your knowledge areas and notes
- `Calendar/Daily/` — Your daily logs
- Root files in `Pillars/` (fitness.md, study.md, etc.) — Your personal pillars
- `Templates/` — Your note templates
- `journal.md` — Your private reflections

### 🤖 AI Side (what AI generates)
- **You must place ALL AI-generated content in `30 - AI Outputs/`**
- Never write AI content into Human files unless Zack explicitly asks
- AI can *read* human files for context, but *never modify* human thoughts
- AI outputs include: summaries, study guides (already confirmed), plans, analysis, generated ideas
- Exception: Automations in `scripts/` that Zack explicitly approved

**Why this matters:** AI should never paraphrase, rewrite, or reinterpret Zack's original thoughts. If AI creates something, it goes in `30 - AI Outputs/`. This keeps Zack's authentic voice intact.

---

## 🎯 Zack's Goals & Priorities (Decision Framework)

**1. Health** — 75-78 kg, visible abs, sub-30 min 5K, 10K comfortably
**2. Education** — University semester (Jun 4 - Oct 12), midterms Aug 4-10, finals Sep 30-Oct 12
**3. Content Creation** — 100 YouTube uploads before judging
**4. Skill Development** — 80+ WPM typing, conversational Thai
**5. Everything Else**

When helping plan time or prioritize, always use this framework.

---

## 📅 Current Semester (Sem 1/2026)

| Course | Day | Time | Room |
|--------|-----|------|------|
| BG14036 Ethics VI | Mon | 13:30 | SM209 |
| ITX4213 AI for Business | Tue | 09:00 | VMES0313 |
| GE2102 Heritage | Tue/Thu | 13:30 | SM219 |
| ITX3004 IS Analysis | Wed | 13:30 | VMES0314 |
| CSX4601 Pres&DataViz | Fri | 09:00 | VMES1003 |
| CSX4615 Biz Insights | Fri | 13:30 | VMES1004 |
| ITX4518 Blockchain | Sat | 09:00 | VMES1005 |

- **Upcoming:** ITX3004 Quiz — Jul 22
- **Midterms:** Aug 4-10
- **Finals:** Sep 30 - Oct 12

---

## 📋 How to Use the Vault

### Reading
- Check `Home.md` for today's priorities and status
- Study guides are in `10 - Projects/Semester 1-2026/<Course>/Notes/`
- Health logs in `20 - Areas/Health & Fitness/Logs/`
- Daily notes in `Calendar/Daily/`

### Writing (when Zack asks you to)
1. **Human-side changes** — Only edit root pillar files, templates, or `10 - Projects/` content when Zack explicitly asks. Use frontmatter tags.
2. **AI outputs** — Save to `30 - AI Outputs/` with descriptive filenames.
3. **Study guides** — If creating a new one, confirm the location with Zack first.
4. **Dashboard updates** — `Home.md` is auto-updated by cron (daily_dashboard.py). Only edit manually if Zack asks.

### Workflows / Skills
- Skills are in `~/.hermes/skills/` (Hermes agent skills)
- Zack may store AI workflow instructions in `30 - AI Outputs/Workflows/`
- Always check loaded skills before undertaking a task

---

## 🔗 Tagging Convention
- `#health`, `#fitness`, `#running`, `#nutrition`
- `#uni`, `#study`, `#<course-code>` (e.g., `#ITX3004`)
- `#thai`, `#typing`, `#youtube`
- `#idea`, `#inbox`, `#follow-up`
- `#ai-generated` — for all AI output files in `30 - AI Outputs/`

---

## ⚡ Quick Reference

| Command | Action |
|---------|--------|
| `study-reader` | Launch TTS study reader at http://localhost:8765 |
| `~/Documents/Obsidian/Zack-obs/scripts/study-reader` | Same — launcher script |
| `Calendar/Daily/` | Daily notes with habit tracking |

---

*This file follows the EMAI system architecture by Eric (linked YouTube video). Last updated: Jul 2026.*
