# MOC - Coding

## Notes
```dataview
LIST
FROM "Atlas/Notes" OR "Efforts/Active" OR "Efforts/Archive"
WHERE contains(lower(file.name), "java") OR contains(lower(file.name), "coding") OR contains(lower(file.name), "programming") OR contains(lower(file.name), "database") OR contains(lower(file.name), "backend") OR contains(lower(file.name), "cloud") OR contains(lower(file.name), "github")
SORT file.name ASC
```
