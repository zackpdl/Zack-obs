# Home

## Habit Tracker
- [[Habits/Habit Dashboard|🎯 Habit Dashboard]]

## Quick Capture
- [[Inbox/Capture|Capture]]
- [[Calendar/Daily/2026-05-16|Today]]
- [[Templates/Daily Note|Daily Note Template]]

## Current Efforts
```dataview
LIST
FROM "Efforts/Active"
SORT file.mtime DESC
LIMIT 10
```

## Today
```dataview
LIST
FROM "Calendar/Daily"
SORT file.name DESC
LIMIT 1
```

## Recent Notes
```dataview
LIST
FROM "Atlas/Notes" OR "Atlas/Sources"
SORT file.mtime DESC
LIMIT 12
```

## Atlas Entry Points
- [[Brain]]
- [[Personal]]
- [[Atlas/Maps/MOC - Atlas]]
- [[Atlas/Maps/MOC - Health]]
- [[Atlas/Maps/MOC - University]]
- [[Atlas/Maps/MOC - Coding]]
- [[Atlas/Maps/MOC - Self Improvement]]
- [[Atlas/Maps/MOC - Sources]]

## Weekly Review
- [[Templates/Weekly Review|Weekly Review Template]]
- [[Calendar/Weekly]]

## Key Maps of Content
```dataview
LIST
FROM "Atlas/Maps"
WHERE startswith(file.name, "MOC - ")
SORT file.name ASC
```
