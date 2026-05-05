---
type: dashboard
area: nutrition
---
# Macro & Calorie Tracker

This is the nutrition control center. Log meals in the daily note template, use the `macros` block for food entries, and use this page to review totals.

## Daily Workflow
1. Create a new daily log from [[Templates/Daily Fitness Log]].
2. Add meals inside the `macros` block using food names from the `Nutrition/` folder.
3. Update the frontmatter totals at the end of the day so Dataview and Tracker stay accurate.
4. Review this page once per day, not after every meal.

## Targets
- Calories: 3000 kcal
- Protein: 160 g
- Carbs: 400 g
- Fat: 80 g

## Today's Entry
```dataview
TABLE WITHOUT ID
    Calories,
    Protein,
    Carbs,
    Fat,
    Weight,
    Notes
FROM "020 Health/Fitness"
WHERE date = date(today)
SORT date DESC
LIMIT 1
```

## Macro Split Today
```macrospc
id: today
```

## Recent Nutrition Logs
```dataview
TABLE date as "Date", Calories, Protein, Carbs, Fat, Weight
FROM "020 Health/Fitness"
SORT date DESC
LIMIT 14
```

## Weekly Average
```dataview
TABLE WITHOUT ID
    round(average(rows.Calories), 0) as "Avg Calories",
    round(average(rows.Protein), 0) as "Avg Protein",
    round(average(rows.Carbs), 0) as "Avg Carbs",
    round(average(rows.Fat), 0) as "Avg Fat"
FROM "020 Health/Fitness"
WHERE date >= date(today) - dur(7 days)
GROUP BY true
```

## Food Library
- [[Nutrition/Impact Whey Protein]]
- [[Nutrition/Oat Milk]]
- [[Nutrition/PB + J Sammich]]
- [[Nutrition/Rolled Oats]]
- [[Nutrition/Steamed Pork Buns]]
- [[020 Health/Nutrition|Nutrition Guide]]

## Notes
- Use exact food note titles inside the `macros` block or the plugin will not match them.
- For meals not in the library yet, create a new note in `Nutrition/` with calories, protein, carbs, fat, and serving size in frontmatter.
