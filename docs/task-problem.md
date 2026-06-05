# [BUG] Resolution log shows filenames instead of record titles

**Priority:** Medium  
**Type:** UX Bug  
**Reported:** 2026-06-04  
**Page:** `/resolutions` (resolution log)  
**Section:** Record list

---

## Description

The resolution log lists every record by deriving a display name from the
filename — replacing dashes with spaces. So instead of showing the actual
title written inside the record, it shows something like:

> RES 001 hero ghost button visibility

The real title, written at the top of that same file, is:

> Hero "View resolution log" button made visible

For engineers this is tolerable. For a designer, product manager, or anyone
outside the team, the filename-derived label is meaningless noise. The log
was built to be readable by everyone — and right now it isn't.

---

## Steps to reproduce

1. Run `npm run dev` or `bun dev`
2. Open `http://localhost:4321/resolutions`
3. Look at the record title shown in the card
4. Compare it to the actual title inside `docs/resolutions/RES-001-hero-ghost-button-visibility.md`

---

## Expected behaviour

The resolution log should display the human-readable title from the first
heading inside each record file — the same title a reader would see when
they open the record.

---

## Actual behaviour

The log derives a label from the filename by replacing dashes with spaces.
This exposes internal naming conventions (reference numbers, slug patterns)
to readers who have no context for them.

---

## Acceptance criteria

- [ ] Each card in `/resolutions` shows the title from inside the record, not the filename
- [ ] If a record has no title, it falls back to the slug-derived label
- [ ] The `/resolutions/[slug]` detail page is not affected
- [ ] No other visible elements change
