---
tags:
  - dashboard
  - health
created: 2026-06-08
---

# 🫀 Health Dashboard

[[Home]] · [[20 - Areas/Health & Fitness/Habits/Habit Dashboard|Habit Dashboard]] · [Maps/MOC - Health|Health MOC]]

> Health metrics from Apple Health exported via Health.md app.
> Metrics are in frontmatter — ready for heatmap-tracker and dataview queries.

---

## 📊 Daily Steps

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Steps",
    heatmapSubtitle: "Daily step count",
    colorScheme: { paletteName: "default", customColors: [] },
    intensityScaleStart: 0,
    intensityScaleEnd: 15000,
    showCurrentDayBorder: true,
    excludeFalsy: true,
};

for (let page of dv.pages('"Health"').where(p => p.steps).sort(p => p.file.name)) {
    const [bYear, month, day] = page.file.name.split('-');
    const gregYear = parseInt(bYear) - 543;
    trackerData.entries.push({
        date: `${gregYear}-${month}-${day}`,
        filePath: page.file.path,
        intensity: Math.min(page.steps / 1000, 15),
        content: `${page.steps.toLocaleString()} steps`,
    });
}

trackerData.basePath = "Health";
renderHeatmapTracker(this.container, trackerData);
```

---

## 🏋️ Workout Minutes

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Workouts",
    heatmapSubtitle: "Minutes of exercise per day",
    colorScheme: { paletteName: "default", customColors: [] },
    intensityScaleStart: 0,
    intensityScaleEnd: 120,
    showCurrentDayBorder: true,
    excludeFalsy: true,
};

for (let page of dv.pages('"Health"').where(p => p.workout_minutes).sort(p => p.file.name)) {
    const [bYear, month, day] = page.file.name.split('-');
    const gregYear = parseInt(bYear) - 543;
    trackerData.entries.push({
        date: `${gregYear}-${month}-${day}`,
        filePath: page.file.path,
        intensity: Math.min(page.workout_minutes / 10, 12),
        content: `${page.workout_minutes} min workout`,
    });
}

trackerData.basePath = "Health";
renderHeatmapTracker(this.container, trackerData);
```

---

## 😴 Sleep Duration

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Sleep",
    heatmapSubtitle: "Total sleep in hours",
    colorScheme: { paletteName: "default", customColors: [] },
    intensityScaleStart: 0,
    intensityScaleEnd: 600,
    showCurrentDayBorder: true,
    excludeFalsy: true,
};

for (let page of dv.pages('"Health"').where(p => p.sleep_minutes).sort(p => p.file.name)) {
    const [bYear, month, day] = page.file.name.split('-');
    const gregYear = parseInt(bYear) - 543;
    const hours = (page.sleep_minutes / 60).toFixed(1);
    trackerData.entries.push({
        date: `${gregYear}-${month}-${day}`,
        filePath: page.file.path,
        intensity: page.sleep_minutes,
        content: `${hours}h sleep`,
    });
}

trackerData.basePath = "Health";
renderHeatmapTracker(this.container, trackerData);
```

---

## 💚 Heart Rate Variability (HRV)

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "HRV",
    heatmapSubtitle: "Heart rate variability (ms)",
    colorScheme: { paletteName: "default", customColors: [] },
    intensityScaleStart: 0,
    intensityScaleEnd: 100,
    showCurrentDayBorder: true,
    excludeFalsy: true,
};

for (let page of dv.pages('"Health"').where(p => p.hrv).sort(p => p.file.name)) {
    const [bYear, month, day] = page.file.name.split('-');
    const gregYear = parseInt(bYear) - 543;
    trackerData.entries.push({
        date: `${gregYear}-${month}-${day}`,
        filePath: page.file.path,
        intensity: page.hrv,
        content: `${page.hrv} ms HRV`,
    });
}

trackerData.basePath = "Health";
renderHeatmapTracker(this.container, trackerData);
```

---

## ❤️ Resting Heart Rate

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Resting HR",
    heatmapSubtitle: "Resting heart rate (bpm) — lower is fitter",
    colorScheme: { paletteName: "default", customColors: [] },
    intensityScaleStart: 40,
    intensityScaleEnd: 80,
    showCurrentDayBorder: true,
    excludeFalsy: true,
};

for (let page of dv.pages('"Health"').where(p => p.resting_hr).sort(p => p.file.name)) {
    const [bYear, month, day] = page.file.name.split('-');
    const gregYear = parseInt(bYear) - 543;
    trackerData.entries.push({
        date: `${gregYear}-${month}-${day}`,
        filePath: page.file.path,
        intensity: 120 - page.resting_hr, // inverted: lower HR = higher intensity
        content: `${page.resting_hr} bpm resting HR`,
    });
}

trackerData.basePath = "Health";
renderHeatmapTracker(this.container, trackerData);
```

---

## 🔗 Quick Links

| Note | Description |
|------|-------------|
| [[20 - Areas/Health & Fitness/Habits/Habit Dashboard\|🎯 Habit Dashboard]] | Gym, Running, Study, Meditation, Thai, Reading, Typing |
| [[20 - Areas/Health & Fitness/Habits/Gym\|🏋️ Gym]] | Strength training tracker |
| [[20 - Areas/Health & Fitness/Habits/Running\|🏃 Running]] | Running progress |
| [[20 - Areas/Health & Fitness/Habits/Study Session\|📚 Study]] | Study habit tracker |
| [[20 - Areas/Health & Fitness/Workout Plans/Hybrid Training Plan\|Hybrid Training Plan]] | Full training plan |
| [Maps/MOC - Health\|Health MOC]] | All health-related notes |

---

## 📈 Weekly Summary (current week)

```dataview
TABLE WITHOUT ID
    dateformat(date(file.name, "yyyy-MM-dd"), "EEE") AS Day,
    steps AS Steps,
    round(sleep_minutes / 60) + "h " + (sleep_minutes % 60) + "m" AS Sleep,
    workout_minutes + "m" AS Workout,
    hrv + "ms" AS HRV,
    resting_hr + "bpm" AS "Rest HR"
FROM "Health"
WHERE date(file.name, "yyyy-MM-dd") >= date(today) - dur(7 days)
  AND date(file.name, "yyyy-MM-dd") <= date(today)
SORT file.name ASC
```
