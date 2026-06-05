# Fix Spec — Resolution log should show record titles, not filenames

**Spec for:** [BUG] Resolution log shows filenames instead of record titles  
**Date:** 2026-06-04  
**Status:** Ready for implementation

---

## What needs to happen

Each card in `/resolutions` must show the human-readable title from inside
the record file — not a label derived from the filename.

Read `docs/task-problem.md` for the full description and acceptance criteria.

Look at `src/pages/resolutions/index.astro` to see how record titles are
currently displayed. Then look at `src/pages/report.astro` — it already
solves the same problem of extracting a title from raw markdown content.
Apply the same pattern here.

---

## Acceptance criteria

- [ ] Cards in `/resolutions` show the title from inside the record file
- [ ] Falls back to slug-derived label if the record has no title
- [ ] No other visible elements on the page change
- [ ] `npm run build` completes with no errors

---

## After the fix

Once verified in the browser, write a resolution record at
`docs/resolutions/RES-002-resolution-log-titles.md` following the agent
instructions in `README.md`.
