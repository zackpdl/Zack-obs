---
type: guide
area: nutrition
---
# Nutrition Guide

The `Nutrition/` folder is your food database for the Obsidian `macros` plugin.

## How To Add Foods
1. Create a note in `Nutrition/`.
2. Add frontmatter with `calories`, `protein`, `fat`, `carbs`, and `serving_size`.
3. Use the exact note title inside your daily `macros` block.

## Current Macro Targets
- Calories: 3000 kcal
- Protein: 160 g
- Carbs: 400 g
- Fat: 80 g

## ⚡ Fast Logging Format (for API results)

When you search from FatSecret or anywhere, paste like this:

```md
- Thai Pork Bun  
  Calories: 180 kcal  
  Protein: 6g  
  Carbs: 28g  
  Fat: 5g  
```

Then drop it into a table row in your Daily Log.

## Current Food Notes
```dataview
TABLE calories, protein, carbs, fat, serving_size
FROM "Nutrition"
SORT file.name ASC
```

## Rule
If a food is used often, add it to `Nutrition/` once instead of manually estimating it every day.

---
[[020 Health/Calorie Tracker|Back to Macro Tracker]]
