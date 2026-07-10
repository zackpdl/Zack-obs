# 🏠 Home

## Quick Capture
- [[00 - Inbox/Capture|📝 Capture]]
- [[Calendar/Daily/2026-07-10|📅 Today's Note]]
- [[Templates/Daily Note|Daily Note Template]]

---

## 🎯 Active Projects
```dataview
TABLE file.name AS "Project", file.mtime AS "Modified"
FROM "10 - Projects"
WHERE file.name != "index.md"
SORT file.mtime DESC
LIMIT 10
```

## 📂 Semester 1-2026
```dataview
TABLE file.name AS "Course", file.mtime AS "Modified"
FROM "10 - Projects/Semester 1-2026"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## 🔄 Areas (Ongoing)
- [[20 - Areas/Health & Fitness/Health Dashboard|🫀 Health Dashboard]]
- [[20 - Areas/Health & Fitness/Habits/Habit Dashboard|🎯 Habit Dashboard]]
- [[20 - Areas/Health & Fitness/Health & Fitness Hub|💪 Health & Fitness Hub]]
- [[20 - Areas/University/Semester 1 2026 - Course Schedule|📚 Course Schedule]]
- [[20 - Areas/Self-Improvement/Daily Routine|🌅 Daily Routine]]

## 📚 Resources
```dataview
LIST
FROM "30 - Resources"
SORT file.name ASC
LIMIT 15
```

## 🗄️ Recent Notes
```dataview
LIST
FROM "30 - Resources/Knowledge" OR "30 - Resources/Media/Sources"
SORT file.mtime DESC
LIMIT 8
```

## 📖 NotebookLM Study Hub
- [[30 - Resources/AI & Tech/NotebookLM Hub|NotebookLM Study Hub]]
- [[30 - Resources/AI & Tech/Study Workflow|Study Workflow Guide]]

---

## Weekly Review
- [[Templates/Weekly Review|Weekly Review Template]]
