# MOC - Meals

Reusable food and meal notes.

```dataview
LIST
FROM "Atlas/Notes"
WHERE contains(file.name, "Oat") OR contains(file.name, "Protein") OR contains(file.name, "Rice") OR contains(file.name, "Buns") OR contains(file.name, "Sammich") OR contains(file.name, "Milk")
SORT file.name ASC
```
