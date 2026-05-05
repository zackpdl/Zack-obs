# Vault Dashboard

> [!quote] "The soul becomes dyed with the color of its thoughts." — Marcus Aurelius

## Command Center
| Focus | Link | Use |
| --- | --- | --- |
| Health | [[020 Health/Health & Fitness Hub|Health & Fitness Hub]] | Training, calories, sleep, daily logs |
| University | [[040 University/Uni Progress|Academic Progress]] | Degree tracking and current semester |
| Projects | [[060 Projects/Projects|Active Projects]] | Build and ship work |
| Knowledge | [[050 Knowledge/|Zettelkasten]] | Notes, concepts, references |

## Quick Actions
- [[020 Health/Fitness Tracker|Open Training Dashboard]]
- [[020 Health/Calorie Tracker|Open Macro Tracker]]
- [[020 Health/Sleep & Recovery Tracker|Open Sleep Tracker]]
- [[020 Health/Hybrid Training Log|Open Training Log]]
- [[010 Personal/Daily Routine|Open Daily Routine]]
- [[Bookmarks/bookmark-dashboard|Open Bookmarks]]

## Health Snapshot
- [[020 Health/Health & Fitness Hub|Health Hub]]
- [[020 Health/Hybrid Training Plan|Hybrid Training Plan]]
- [[020 Health/Fitness Tracker|Training & Progress Dashboard]]
- [[020 Health/Calorie Tracker|Macro & Calorie Tracker]]
- [[020 Health/Nutrition|Nutrition Guide]]

## University Snapshot
- [[040 University/Uni Progress|Graduation Progress]]
- [[040 University/024-2 University/|Current Semester Folder]]
- [[040 University/099 University/|University Archive]]

```dataview
TABLE WITHOUT ID file.link as "Current Semester Notes"
FROM "040 University/024-2 University"
SORT file.name ASC
LIMIT 8
```

## Projects & Knowledge
- [[060 Projects/Projects|Active Projects]]
- [[050 Knowledge/|Knowledge Base]]
- [[Brain|Brain]]

```dataview
TABLE WITHOUT ID file.link as "Recent Knowledge Notes"
FROM "050 Knowledge"
SORT file.mtime DESC
LIMIT 8
```

## Daily Notes
```dataview
TABLE WITHOUT ID file.link as "Recent Daily Notes"
FROM "999 Daily Note"
SORT file.name DESC
LIMIT 7
```

## Nutrition Library
```dataview
TABLE WITHOUT ID file.link as "Food", calories as "Kcal", protein as "Protein", carbs as "Carbs", fat as "Fat"
FROM "Nutrition"
SORT file.name ASC
LIMIT 10
```

## Maintenance
- [[Migration Notes|Migration Log]]
- Review broken or unused notes from old structures during weekly cleanup.

Last Updated: 2026-05-05
