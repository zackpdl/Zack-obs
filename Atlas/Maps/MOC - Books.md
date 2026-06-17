# MOC - Books

Book notes, reading tracking, and literary references.

---

## 📖 All Books

```dataview
LIST
FROM "Atlas/Sources/Books"
SORT file.mtime DESC
```

---

## 📋 By Status

### 🟢 To Read
```dataview
LIST
FROM "Atlas/Sources/Books"
WHERE contains(Status, "🟢")
```

### 🟡 Reading
```dataview
LIST
FROM "Atlas/Sources/Books"
WHERE contains(Status, "🟡")
```

### ✅ Finished
```dataview
LIST
FROM "Atlas/Sources/Books"
WHERE contains(Status, "✅")
```

---

## 📊 Stats
- **Total:** `= length(list("Atlas/Sources/Books", (x) => true))`
- **Finished:** `= length(filter(list("Atlas/Sources/Books"), (x) => contains(x.Status, "✅")))`
- **Reading:** `= length(filter(list("Atlas/Sources/Books"), (x) => contains(x.Status, "🟡")))`
- **To Read:** `= length(filter(list("Atlas/Sources/Books"), (x) => contains(x.Status, "🟢")))`

---

## 🔗 Quick Links
- [[Templates/Book.md|New Book Note]]