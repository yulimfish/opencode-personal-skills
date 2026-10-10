---
name: ui-preview-first
description: Use before any edit or file creation that touches UI layout, component hierarchy, or visual structure. Applies to .tsx/.jsx/.vue/.svelte/.astro/.html/.css files and anything under components/ui/views/pages/screens directories. Skip only for pure logic changes (handlers, hooks, values) that don't move DOM nodes.
---

# UI Preview First

You will change UI. Do this **before** touching a file.

## Steps

1. **State intent in one line.** "Adding a settings panel with a sidebar tab list on the left, form on the right."
2. **Draw ASCII wireframe of the after-state.** Use box-drawing characters. Show container boundaries, key labels, approximate proportions. Do NOT reproduce pixel widths — show hierarchy.
3. **If changing existing UI**, also draw the current state above it, labeled `BEFORE`.
4. **List the deltas** in ≤ 4 bullets: what moves, what appears, what disappears, what merges.
5. **Ask for one-line confirmation.** "OK 就动手 / 改这里 / 换别的方案?"
6. Wait for confirmation. Then execute.

## Wireframe conventions

- Outer container: `┌─┐│└─┘`
- Section dividers: `├─┤`
- Interactive element: `[ Button ]`, `<Input______>`, `( ) Radio`, `[✓] Check`
- Fixed sidebar: label with `SIDEBAR (fixed 240px)`
- Scroll region: label with `↕ scroll`

## Example

```
BEFORE                                AFTER
┌────────── Header ──────────┐        ┌────────── Header ──────────┐
│                            │        ├──── SIDEBAR ────┬──────────┤
│      Content (single)      │        │ • General       │  Content │
│                            │        │ • Account       │  (form)  │
│                            │        │ • Notifications │          │
└────────────────────────────┘        └─────────────────┴──────────┘
```

Deltas: (1) add left sidebar 240px, (2) tab list replaces nothing (new), (3) content shrinks to fill remaining.

## Skip conditions

- Renaming a handler.
- Changing a color token, spacing value, or copy string that doesn't rewrap.
- Adding a `console.log` / analytics call.
- Fixing a bug where the visual output doesn't change.

If in doubt: draw the wireframe. Cheap insurance.
