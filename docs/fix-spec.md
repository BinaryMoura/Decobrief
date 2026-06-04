# Fix Spec — Align feature card CTA buttons using flex column layout

**Spec for:** [BUG] Feature card CTA buttons are misaligned on the home page  
**Spec author:** engineering  
**Date:** 2026-06-04  
**Status:** Ready for implementation

---

## Proposed fix

Apply `display: flex; flex-direction: column` to `.feature-card` and `margin-top: auto`
to `.btn-card`. This causes the button to absorb any remaining vertical space at the
bottom of each card, regardless of how much content is above it.

### CSS changes (inside `src/pages/index.astro`)

```css
/* BEFORE */
.feature-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem;
}

.btn-card {
  display: inline-block;
  margin-top: 1.5rem;
  padding: 0.6rem 1.4rem;
  ...
}

/* AFTER */
.feature-card {
  display: flex;
  flex-direction: column;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 2rem;
}

.btn-card {
  display: inline-block;
  margin-top: auto;          /* ← replaces the fixed 1.5rem */
  padding-top: 1.5rem;       /* ← preserves minimum gap above button */
  padding: 0.6rem 1.4rem;
  ...
}
```

---

## Why this approach

- **CSS-only, zero markup change.** No HTML restructuring needed — the three cards already
  have the right DOM order (icon → heading → description → button).
- **Resilient.** `margin-top: auto` on a flex child distributes the entire remaining space,
  so it works for any description length and any card height set by the grid.
- **Industry standard.** This is the canonical pattern for "sticky footer inside a card" —
  well understood, has no browser compatibility issues.

---

## What NOT to do

| Approach | Why not |
|---|---|
| Set equal `min-height` on `<p>` | Breaks on different viewports; content-length coupling |
| Truncate descriptions with `overflow: hidden` | Hides real content |
| Use `position: absolute` on the button | Requires explicit card height; fragile |
| Rewrite card markup | Unnecessary — the fix is two CSS declarations |

---

## Testing

After applying the fix, verify:

1. `npm run dev` / `bun dev` — inspect the three cards in the browser
2. All three "Get started" buttons are at the same vertical position
3. Resize the browser window — alignment must hold at all widths where the three-column
   grid is active (> 768 px)
4. `npm run build` / `bun run build` — static build must complete with no errors

---

## Resolution record

After the fix is applied and verified, produce a resolution record at
`docs/resolutions/RES-002-feature-card-button-alignment.md` following the agent
instructions in `README.md`.

### Tone guidance

Write every section as if explaining to someone who was not in the room — a designer,
a product manager, or a new team member who does not read CSS. Describe the visible
problem and its real-world effect, not the mechanism used to fix it.

**Wrong tone (technical):**
> Added `display: flex; flex-direction: column` to `.feature-card` and `margin-top: auto`
> to `.btn-card` to correct vertical alignment across grid columns.

**Right tone (plain language):**
> The three "Get started" buttons on the home page were sitting at different heights —
> the card with the least text had its button near the middle of the card, while the
> card with the most text had it near the bottom. The page looked unfinished and
> inconsistent. The fix makes all three buttons sit flush at the bottom of their cards,
> regardless of how much text is above them.
