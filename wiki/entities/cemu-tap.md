---
title: CemuTap
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/thatonekidnextdoorlol-hash__CemuTap.md
updated: 2026-11-09
confidence: medium
---

# CemuTap

**CemuTap** (thatonekidnextdoorlol-hash/CemuTap) is a free, open-source memory scanner and live editor aimed at the **Cemu** Wii U emulator—positioned as a Cheat Engine–style alternative for emulated Wii U titles on Windows or Linux. (source: wiki/sources/descriptions/thatonekidnextdoorlol-hash__CemuTap.md)

## Implementation

- Python + **Tkinter** desktop UI; **pymem** attaches to the Cemu host process for read/write, including **MEM2** guest addresses.
- First/next scans across byte widths, floats, doubles, and unknown initial values; filters (changed, increased, etc.).
- Address tables, live edit, value freeze, vector grouping, and pointer scans.
- Custom import/export formats for scan results and named tables; **Plugin API** for Python plugins (memory hooks, scans, custom tabs).

## Use cases

Suited to **reverse engineering**, **game research**, and **offline modding** when locating and manipulating in-game variables under Cemu—not online anti-cheat evasion.

## Positioning

Listed in the **Cheat** lane beside cross-platform Python scanners such as [[pymemory-editor]] and native CE workflows; emulator-specific rather than generic process attach. Complements Wii U static-recomp research such as [[switchwakerhd]] and other console emulator tooling.

## Links

- Repo: https://github.com/thatonekidnextdoorlol-hash/CemuTap

## Related

[[pymemory-editor]] · [[cheat-engine]] · [[ferret]] · [[simple-memory-editor]] · [[pointer-lab]] · [[switchwakerhd]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
