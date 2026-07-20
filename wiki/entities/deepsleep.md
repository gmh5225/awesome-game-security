---
title: DeepSleep
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/thefLink__DeepSleep.md
updated: 2026-07-20
confidence: medium
---

# DeepSleep

x64 Gargoyle variant that hides memory artifacts using **ROP-only** chains and **PIC** (position-independent code). Unlike classic Gargoyle, it avoids APCs and is implemented fully as PIC. Aimed at anti-cheat engineers and defensive researchers studying the page-protection / sleep-hide lane. (source: wiki/sources/descriptions/thefLink__DeepSleep.md)

Pairs with VEH page-protection samples such as [[no-access-protection]] (`PAGE_NOACCESS`) and [[voidmaw]] (`PAGE_GUARD`) as alternate artifact-hiding strategies for AC memory-integrity research.

## Links

- Repo: https://github.com/thefLink/DeepSleep

## Related

[[no-access-protection]] · [[voidmaw]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
