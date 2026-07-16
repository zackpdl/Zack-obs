# 🎬 YouTube Mission Control

> Document the transformation honestly. 100 uploads before judging results.

---

## 🎯 Channel Status

| Metric | Current | Target |
|--------|---------|--------|
| **Uploads** | — | 100 |
| **Subscribers** | — | — |
| **Total Views** | — | — |
| **Avg View Duration** | — | — |

---

## 🗓️ Publishing Schedule

| Status | Frequency |
|--------|-----------|
| 🎯 **Target** | 1 video / week |
| 📅 **Current** | — |

---

## 📝 Content Pipeline

### Ideas

```dataview
TABLE status AS "Status", created AS "Created"
FROM "youtube"
WHERE status AND contains(file.path, "Ideas")
SORT created DESC
LIMIT 10
```

### Scripts In Progress

```dataview
TABLE status AS "Status", modified AS "Last Edit"
FROM "youtube"
WHERE status = "scripting" OR status = "draft"
SORT modified DESC
LIMIT 10
```

### Published

```dataview
TABLE published AS "Published", views AS "Views"
FROM "youtube"
WHERE published
SORT published DESC
LIMIT 20
```

---

## 🎬 Content Pillars

| Pillar | Topics |
|--------|--------|
| **Monk Mode** | Discipline, dopamine, lifestyle design |
| **Fitness** | Training, nutrition, physique transformation |
| **Running** | 5K, 10K, half marathon journey |
| **Thailand Life** | Daily life, cultural observations |
| **University** | CS student experience, study vlogs |
| **Personal Growth** | Mindset, habits, lessons learned |

---

## 📈 Content Guidelines

1. **Honesty over perfection** — real struggles, real progress
2. **Consistency over quality** — volume creates skill
3. **100 uploads minimum** — judge after the volume
4. **Document, don't perform** — the camera is a diary

---

## 🔗 Quick Links

- [[home|🏠 Home]]
- [[monk_mode|🧘 Monk Mode]]
- [[journal|📓 Journal]]

*Last updated: {{date}}*
