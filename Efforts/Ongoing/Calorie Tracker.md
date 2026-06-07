---
type: dashboard
area: nutrition
---
# Macro & Calorie Tracker

This is the main calorie dashboard. Log meals in today's daily fitness note and this page will update from that log.

## Daily Workflow
1. Open [[Templates/Daily Nutrition Log|Daily Nutrition Log Template]] (Manual) or [[Templates/Daily Fitness Log|Daily Fitness Log Template]] (Auto).
2. Create or update today's note in `Calendar/Logs/YYYY-MM-DD Fitness Log.md`.
3. Add meals (use [[Atlas/Maps/MOC - Meals|Reusable Meals]] for speed).
4. Update frontmatter totals at the end of the day.
5. Review this page or [[Efforts/Ongoing/Weekly Progress|Weekly Progress]] for trends.

## Navigation
- [[Efforts/Ongoing/Weekly Progress|📊 Weekly Progress Summary]]
- [[Atlas/Maps/MOC - Meals|🍱 Reusable Meals Library]]
- [[Atlas/Notes/Nutrition|📖 Nutrition Guide & Food DB]]

## Targets
- Calories: 3000 kcal
- Protein: 160 g
- Carbs: 400 g
- Fat: 80 g

## Today's Macros
```macros
id: today
```

### Today's Pie Chart
```macrospc
id: today
```

## Today's Log
```dataview
TABLE WITHOUT ID
    file.link as "Log",
    Calories,
    Protein,
    Carbs,
    Fat,
    Weight,
    SleepHours,
    Workout,
    Run,
    Notes
FROM "Calendar/Logs"
WHERE date = date(today)
SORT date DESC
LIMIT 1
```

## Last 7 Days
```dataview
TABLE date as "Date", Calories, Protein, Carbs, Fat, Weight
FROM "Calendar/Logs"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

## Weekly Averages
```dataview
TABLE WITHOUT ID
    round(average(rows.Calories), 0) as "Avg Calories",
    round(average(rows.Protein), 0) as "Avg Protein",
    round(average(rows.Carbs), 0) as "Avg Carbs",
    round(average(rows.Fat), 0) as "Avg Fat",
    round(average(rows.Weight), 1) as "Avg Weight"
FROM "Calendar/Logs"
WHERE date >= date(today) - dur(7 days)
GROUP BY true
```

## Graphs
```tracker
searchType: frontmatter
searchTarget: Calories
folder: 020 Health/Fitness
startDate: 2026-05-01
endDate: 2026-05-31
line:
    title: Daily Calories
    yAxisLabel: kcal
    lineColor: "#4da6ff"
```

```tracker
searchType: frontmatter
searchTarget: Protein
folder: 020 Health/Fitness
startDate: 2026-05-01
endDate: 2026-05-31
line:
    title: Protein Intake
    yAxisLabel: grams
    lineColor: "#ffd11a"
```

```tracker
searchType: frontmatter
searchTarget: Carbs
folder: 020 Health/Fitness
startDate: 2026-05-01
endDate: 2026-05-31
line:
    title: Carb Intake
    yAxisLabel: grams
    lineColor: "#33cc99"
```

```tracker
searchType: frontmatter
searchTarget: Fat
folder: 020 Health/Fitness
startDate: 2026-05-01
endDate: 2026-05-31
line:
    title: Fat Intake
    yAxisLabel: grams
    lineColor: "#ff884d"
```

## Food Library
```dataview
TABLE WITHOUT ID file.link as "Food", calories as "Kcal", protein as "Protein", carbs as "Carbs", fat as "Fat"
FROM "Atlas/Notes"
SORT file.name ASC
LIMIT 12
```

## Notes
- `macros` and `macrospc` above track today's daily log through `id: today`.
- Keep the actual meal entries in the daily fitness note, not in this dashboard.
- Food names in the `macros` block must exactly match note titles in `Nutrition/`.
