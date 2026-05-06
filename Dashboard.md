# Vault Dashboard

> [!quote] "The soul becomes dyed with the color of its thoughts." — Marcus Aurelius

## Command Center
| Focus | Link | Use |
| --- | --- | --- |
| Brain | [[Brain]] | Ideas, terminal, hotkeys, prompts |
| Personal | [[010 Personal/Personal|Personal Info]] | IDs, accounts, addresses |
| University | [[040 University/Uni Progress|Academic Progress]] | Degree tracking and current semester |
| Projects | [[060 Projects/Projects|Active Projects]] | Build and ship work |

## Quick Access
- [[010 Personal/Daily Routine|Daily Routine]]
- [[Bookmarks/bookmark-dashboard|Bookmark Dashboard]]
- [[050 Knowledge/|Knowledge Base]]
- [[010 Personal/Personal|Personal]]
- [[Brain|Brain]]

## Daily Routine
| Time | Activity |
| --- | --- |
| 07:30 | Wake up |
| 07:40 – 09:00 | Run + Yoga + Abs Workout |
| 09:00 – 10:30 | Breakfast + Run Errands |
| 10:30 – 14:30 | Take Care of Restaurant |
| 15:00 – 17:00 | Gym: Weighted Workout |
| 17:00 – 18:00 | Post-Workout Meal + Shower |
| 18:00 – 23:00 | Work at Restaurant |
| 23:00 – 00:00 | Family Time |
| 00:00 | Sleep |

## University Snapshot
- [[040 University/Uni Progress|Graduation Progress]]
- [[040 University/024-2 University/|Current Semester Folder]]

```dataview
TABLE WITHOUT ID file.link as "Current Semester Notes"
FROM "040 University/024-2 University"
SORT file.name ASC
LIMIT 8
```

## Projects & Knowledge
- [[060 Projects/Projects|Active Projects]]
- [[050 Knowledge/|Knowledge Base]]

```dataview
TABLE WITHOUT ID file.link as "Recent Knowledge Notes"
FROM "050 Knowledge"
SORT file.mtime DESC
LIMIT 8
```

## Recent Bookmarks
```dataview
TABLE WITHOUT ID "[" + title + "](" + source + ")" as "Bookmark", saved as "Date"
FROM "Bookmarks"
WHERE title != null
SORT saved DESC
LIMIT 5
```

## Daily Notes
```dataview
TABLE WITHOUT ID file.link as "Recent Daily Notes"
FROM "999 Daily Note"
SORT file.name DESC
LIMIT 7
```

## Maintenance
- [[Migration Notes|Migration Log]]

Last Updated: 2026-05-06
