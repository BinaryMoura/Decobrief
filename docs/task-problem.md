# [BUG] Feature card CTA buttons are misaligned on the home page

**Priority:** Medium  
**Type:** Visual / UI Bug  
**Reported:** 2026-06-04  
**Page:** `/` (home)  
**Section:** "Everything your team needs" — feature cards grid

---

## Description

The three feature cards in the "Everything your team needs" section each end with a
"Get started" button. Because the three card descriptions have different lengths, the
buttons appear at different vertical positions — the card with the shortest description
has its button sitting near the middle of the card area, while the card with the longest
description has its button near the actual bottom edge.

This breaks the visual rhythm of the row and makes the section look unfinished, as if
the layout was not reviewed before shipping.

---

## Steps to reproduce

1. Run `npm run dev` or `bun dev`
2. Open `http://localhost:4321`
3. Scroll down to the "Everything your team needs" section
4. Compare the vertical position of the three "Get started" buttons across the cards

---

## Expected behaviour

All three "Get started" buttons should sit flush at the bottom of their respective
cards, regardless of how much text is in the description above them. The visual result
should be a clean horizontal row of buttons at the same height.

---

## Actual behaviour

The buttons follow the content — each one sits immediately below its description text.
Shorter descriptions mean a higher button; longer descriptions mean a lower one. In a
three-column grid with equal-height rows, this creates obvious vertical misalignment.

---

## Root cause

The `.feature-card` elements are rendered as standard block containers. There is no
mechanism to push the button to the bottom edge of the card when the description is
shorter than its neighbours.

The standard fix is to make each card a flex column and give the button `margin-top: auto`,
which distributes the remaining vertical space above the button.

---

## Acceptance criteria

- [ ] All three "Get started" buttons sit at the same vertical position within the card row
- [ ] The fix is resilient: changing any description to any length must not break alignment
- [ ] No other visible elements on the page are affected by the change

---

## Files to change

- `src/pages/index.astro` — the `<style>` block inside the home page (the bug is in `.feature-card` and `.btn-card`)

---

## Do not do

- Do not change description text to force equal lengths — that is a content workaround, not a layout fix
- Do not add a fixed `min-height` to the description `<p>` — heights will differ across viewports
