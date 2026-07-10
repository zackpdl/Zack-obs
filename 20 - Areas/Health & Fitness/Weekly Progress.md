# 📊 Weekly Nutrition Summary

This page uses Dataview to pull data from your `020 Health/Fitness` logs.

## 📈 Last 7 Days
```dataview
TABLE Calories, Protein, Carbs, Fat, Weight
FROM "Calendar/Logs"
WHERE type = "nutrition-log"
SORT date DESC
LIMIT 7
```

---

## 📉 Weekly Averages
```dataview
TABLE WITHOUT ID
    round(average(rows.Calories), 0) as "Avg Calories",
    round(average(rows.Protein), 0) as "Avg Protein",
    round(average(rows.Carbs), 0) as "Avg Carbs",
    round(average(rows.Fat), 0) as "Avg Fat",
    round(average(rows.Weight), 1) as "Avg Weight"
FROM "Calendar/Logs"
WHERE date >= date(today) - dur(7 days) AND type = "nutrition-log"
GROUP BY true
```

---

## 📝 Manual Entry Table (Optional)
*If you prefer not to use Dataview, use this table:*

| Date | Calories | Protein | Weight |
|------|----------|---------|--------|
| Mon  |          |         |        |
| Tue  |          |         |        |
| Wed  |          |         |        |
| Thu  |          |         |        |
| Fri  |          |         |        |
| Sat  |          |         |        |
| Sun  |          |         |        |

---
[[20 - Areas/Health & Fitness/Nutrition/Calorie Tracker|Back to Tracker Dashboard]]
