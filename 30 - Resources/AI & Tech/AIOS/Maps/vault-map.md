# Vault Map

This vault uses ACE. Do not redesign the core structure. AI should build on top of it.

## Core Structure
- Atlas: knowledge, ideas, references, learning, synthesis.
- Calendar: time-bound context, daily notes, weekly notes, meetings, logs.
- Efforts: action, projects, goals, outcomes, active work.
- Inbox: fast capture before processing.
- Templates: reusable note structures.
- Attachments: files, images, PDFs, and assets.
- AIOS: portable AI layer for identity, skills, prompts, agents, and templates.

## Atlas
Use Atlas for durable knowledge.

Put here:
- Evergreen notes
- Concepts and ideas
- Learning notes
- Research summaries
- Source notes
- People notes
- Maps of Content

Main folders:
- `Atlas/Maps`: Maps of Content. Use names like `MOC - Coding`.
- `Atlas/Notes`: atomic or evergreen notes.
- `Atlas/Sources`: books, articles, videos, bookmarks, external summaries.
- `Atlas/People`: people, contacts, identity, relationship context.
- `Atlas/Utilities`: vault reports, helper scripts, system notes.

## Calendar
Use Calendar for time-bound context.

Put here:
- Daily notes
- Weekly notes
- Monthly notes
- Meetings
- Logs
- Reflections tied to a date

Calendar is not long-term storage. If an idea becomes durable, link it to Atlas or move it into Atlas.

## Efforts
Use Efforts for outcome-oriented work.

Put here:
- Projects
- Goals
- Launches
- University deliverables
- Fitness plans
- Business ideas
- Coding builds
- Recurring systems

Main folders:
- `Efforts/Active`: current focus.
- `Efforts/Ongoing`: recurring systems, habits, trackers.
- `Efforts/Someday`: not active, retained for later.
- `Efforts/Archive`: completed or inactive work.

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
- Decide whether the note belongs in Atlas, Calendar, Efforts, Inbox, or AIOS.
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
- `Atlas/Maps`
- `Efforts/Active`
- `Efforts/Ongoing`
- `Calendar/Daily`
- `Atlas/Notes`
- `Atlas/Sources`
- `Inbox/Capture.md`

## Efficient AI Navigation
- Start with MOCs, not the entire vault.
- Use filenames and links to narrow context.
- Read the smallest useful set of notes.
- Summarize uncertainty instead of guessing.
- Preserve existing links and note intent.
