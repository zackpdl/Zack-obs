---
type: dashboard
area: health
---
# Training & Progress Dashboard

This note is the review layer for your daily logs in [020 Health/Fitness](/Users/zackpdl/Documents/Obsidian/Zack-obs%202/020%20Health/Fitness).

## Quick Links
- [[20 - Areas/Health & Fitness/Health & Fitness Hub|Health & Fitness Hub]]
- [[20 - Areas/Health & Fitness/Nutrition/Calorie Tracker|Macro & Calorie Tracker]]
- [[20 - Areas/Health & Fitness/Hybrid Training Log|Training Log]]
- [[20 - Areas/Health & Fitness/Sleep & Recovery Tracker|Sleep & Recovery]]
- [[Templates/Daily Fitness Log|Daily Fitness Log Template]]

## Today's Numbers
```dataview
TABLE WITHOUT ID
    Weight,
    Calories,
    Protein,
    Carbs,
    Fat,
    Steps,
    Workout,
    Run
FROM "Calendar/Logs"
WHERE date = date(today)
SORT date DESC
LIMIT 1
```

## Last 7 Days
```dataview
TABLE date as "Date", Weight, Calories, Protein, Carbs, Fat, Workout, Run
FROM "Calendar/Logs"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

## Weekly Averages
```dataview
TABLE WITHOUT ID
    round(average(rows.Weight), 1) as "Avg Weight",
    round(average(rows.Calories), 0) as "Avg Calories",
    round(average(rows.Protein), 0) as "Avg Protein",
    round(average(rows.Carbs), 0) as "Avg Carbs",
    round(average(rows.Fat), 0) as "Avg Fat"
FROM "Calendar/Logs"
WHERE date >= date(today) - dur(7 days)
GROUP BY true
```

## Macro Split Today
```macrospc
id: today
```

## Graphs
```tracker
searchType: frontmatter
searchTarget: Weight
folder: 020 Health/Fitness
line:
    title: Weight Progress
    yAxisLabel: kg
    lineColor: "#ff4d4d"
```

```tracker
searchType: frontmatter
searchTarget: Calories
folder: 020 Health/Fitness
line:
    title: Daily Calories
    yAxisLabel: kcal
    lineColor: "#4da6ff"
```

```tracker
searchType: frontmatter
searchTarget: Protein
folder: 020 Health/Fitness
line:
    title: Protein Intake
    yAxisLabel: grams
    lineColor: "#ffd11a"
```

## Review Rule
- If sleep is low, lower intensity before you lower consistency.
- If calories are low for multiple days, expect weaker runs and worse gym performance.
- If both sleep and calories are bad, recovery is the bottleneck, not motivation.
