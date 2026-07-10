# Vault Map

This vault uses ACE. Do not redesign the core structure. AI should build on top of it.

## Core Structure (PARA Method)
- `00 - Inbox/`: fast capture before processing.
- `10 - Projects/`: short-term outcomes with deadlines (e.g., courses this semester).
- `20 - Areas/`: ongoing responsibilities (health, fitness, relationships, finance).
- `30 - Resources/`: topics of interest (coding, AI, media, knowledge notes).
- `40 - Archives/`: completed or inactive items (past courses, old projects).
- `Calendar/`: time-bound context, daily notes, weekly notes, logs.
- `Templates/`: reusable note structures.
- `Attachments/`: files, images, PDFs, and assets.

## 10 - Projects
Use Projects for outcome-oriented work with deadlines.

Course structure per semester folder:
- `{Course Code} {Name}/`
  - `Notes/` — study guides, lecture notes, summaries
  - `Materials/` — lecture PDFs, slides, syllabi
  - `Assignments/` — deliverables (optional)
  - `index.md` — course overview, schedule, links

## 20 - Areas
Use Areas for ongoing responsibilities that never end.

Main folders:
- `Health & Fitness/`: workout plans, habits, health logs, nutrition, dashboard
  - `Habits/` — habit tracker files (Gym, Running, Study, etc.)
  - `Logs/` — daily Apple Health data export
  - `Nutrition/` — meal plans, calorie tracking
  - `Workout Plans/` — training programs
- `Relationships/`: people notes, contacts, birthdays
- `Self-Improvement/`: routines, discipline, mindset
- `University/`: general university resources, course schedule
- `Finance/`: budgeting, expenses (if applicable)

## 30 - Resources
Use Resources for durable reference knowledge.

Main folders:
- `Coding/`: programming notes, concepts, language references
- `AI & Tech/`: AI tools, AIOS system, NotebookLM Hub, study workflows
- `Knowledge/`: atomic and evergreen notes (from old Atlas/Notes)
- `Media/`: bookmarks, book PDFs, source summaries
  - `Bookmarks/` — YouTube bookmarks, links
  - `Books/` — book PDFs
  - `Sources/` — external content summaries

## 40 - Archives
Use Archives for inactive items from Projects/Areas/Resources.

Main folders:
- `Past Courses/`: completed course notes from previous semesters
- `Old Projects/`: finished active projects
- `Old Health/`: old health data (pre-2568)

## Calendar
Keep for time-bound context only — daily notes, logs.

## Naming Conventions
- Use clean human-readable names.
- Avoid dates except in Calendar.
- Avoid version numbers unless necessary.
- Prefix Maps of Content with `MOC - `.
- Prefer specific names over vague names like `Untitled`.
- Rename only when it improves retrieval and does not break meaning.

## Linking Rules
- Prefer contextual links over tags.
- Link notes where the relationship is useful for retrieval or thinking.
- Daily notes should link to active efforts and relevant Atlas notes.
- Effort notes should link to supporting Atlas notes and related source notes.
- Source notes should link to the concepts they inform.
- MOCs should provide navigation, not duplicate content.

## How AI Should Create Notes
Before creating a note:
- Search for an existing note with the same or similar name.
- Check relevant MOCs.
- Decide whether the note belongs in 00 - Inbox, 10 - Projects, 20 - Areas, 30 - Resources, 40 - Archives, Calendar, or AIOS.
- Use plain markdown only.
- Keep metadata minimal.
- Add useful links to existing notes.

When creating a note:
- Use a clear title.
- Start with the useful content, not administrative metadata.
- Add a short `Related` section if links are helpful.
- Do not create folders beyond the existing ACE and AIOS structure unless explicitly asked.

## Avoiding Duplicates
- Reuse existing notes when possible.
- If a note already exists, update or link to it instead of creating a near-copy.
- If two notes overlap, suggest a merge instead of silently duplicating.
- If unsure, place rough capture in `Inbox/Capture` and flag it for review.

## Maps of Content
MOCs are navigation pages.

Use MOCs to:
- Group related notes.
- Provide entry points into clusters.
- Surface active areas.
- Help AI retrieve context quickly.

Do not use MOCs as dumping grounds. They should stay short and navigable.

## Project and Effort Rules
Every active effort should clarify:
- Outcome
- Current status
- Next actions
- Related notes
- Supporting sources

AI should help turn vague goals into concrete efforts, but should not create a project unless there is a real outcome.

## High-Priority Folders For AI
When retrieving context, check in this order:
- `AIOS/Maps/me.md`
- `AIOS/Maps/vault-map.md`
- `Home.md`
- `10 - Projects/Semester 1-2026/`
- `20 - Areas/`
- `30 - Resources/`
- `40 - Archives/`
- `Calendar/Daily`
- `00 - Inbox/Capture.md`

## Efficient AI Navigation
- Start with MOCs, not the entire vault.
- Use filenames and links to narrow context.
- Read the smallest useful set of notes.
- Summarize uncertainty instead of guessing.
- Preserve existing links and note intent.
