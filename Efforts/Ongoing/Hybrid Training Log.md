---
type: log
area: training
---
# Hybrid Training Log

## Weekly Default Split
- Monday: Upper lift
- Tuesday: Quality run
- Wednesday: Lower lift
- Thursday: Recovery run or walk
- Friday: Upper or full-body lift
- Saturday: Long run
- Sunday: Full rest

## Intensity Rules
- Poor sleep: recovery only
- Heavy class day: shorten the session
- Lower-body soreness: do not force intervals

## Recent Training Entries
```dataview
TABLE date as "Date", Workout, Run, Steps, Notes
FROM "Calendar/Logs"
WHERE Workout OR Run
SORT date DESC
LIMIT 14
```

## Weekly Review
- Strength progress:
- Running progress:
- Recovery trend:
- What to change next week:

---
[[Efforts/Ongoing/Health & Fitness Hub|Back to Hub]]
