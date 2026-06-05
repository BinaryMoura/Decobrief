---
work_item: ""
pr: ""
status: confirmed
author: Leo Moura
date: 2026-06-04
---

# Hero "View resolution log" button made visible

## What changed

The `.btn-ghost` rule in `src/pages/index.astro` — one property added
(`border: 1px solid var(--border-2)`) and the `transition` extended to include
`border-color`. The hover rule gained `border-color: var(--border)` so the
border brightens slightly on interaction.

## How it was done

A single `border` declaration was added to the existing `.btn-ghost` rule. The
colour `var(--border-2)` was chosen because it is already used for card outlines
elsewhere on the page — the button picks up the same visual language without
introducing anything new. The transition extension ensures the border shift on
hover is smooth and consistent with the colour transition already there.

## Technical result

The element now has a visible 1px outline at rest. Static build completes
with no errors.

## Why / what-for

The "View resolution log" button on the home page was invisible — it had no
outline or background, so it looked like a line of grey text rather than
something you could click. Anyone landing on the home page would see the purple
"How it works" button and miss the resolution log entirely. The fix gives the
button a subtle border so both options in the hero are clearly recognisable as
interactive, while the resolution log link stays visually quieter than the
primary action beside it.
