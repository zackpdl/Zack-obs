# Bookmark Dashboard

This page is live via Dataview and updates as bookmarks are added.

## All Bookmarks

```dataviewjs
const pages = dv.pages()
  .where(p => p.saved && p.source && p.file.name !== "bookmark-dashboard")
  .sort(p => p.saved, 'desc');

dv.table(
  ["Date Added", "Title", "Tags"],
  pages.map(p => [
    p.saved,
    p.file.link,
    (p.tags && p.tags.length) ? p.tags : ["Untagged"],
  ])
);
```

## By Tag

```dataviewjs
const pages = dv.pages()
  .where(p => p.saved && p.source && p.file.name !== "bookmark-dashboard")
  .sort(p => p.saved, 'desc');

const groups = {};
for (const p of pages) {
  const tags = (p.tags && p.tags.length) ? p.tags : ["Untagged"];
  for (const tag of tags) {
    if (!groups[tag]) groups[tag] = [];
    groups[tag].push(p);
  }
}

const tagsSorted = Object.keys(groups)
  .sort((a, b) => a.localeCompare(b, undefined, { sensitivity: "base" }));

for (const tag of tagsSorted) {
  dv.header(3, tag);
  const rows = groups[tag].map(p => `${p.saved}: ${p.file.link}`);
  dv.list(rows);
}
```
