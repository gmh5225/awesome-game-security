---
title: veh_hide_memory
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__veh_hide_memory.md
updated: 2026-08-07
confidence: medium
---

# veh_hide_memory

C++/C sample centered on **VEH + `PAGE_NOACCESS`** for memory analysis. Aimed at anti-cheat engineers and defensive security researchers working the page-protection / anti-tamper lane. (source: wiki/sources/descriptions/gmh5225__veh_hide_memory.md)

Pairs with related PAGE_NOACCESS / VEH samples such as [[no-access-protection]] (VEH trampoline + single-step re-protect), [[bincon]] (hardened console), and [[voidmaw]] (`PAGE_GUARD` variant); VEH-chain dump tooling such as [[veh-dumper]].

## Links

- Repo: https://github.com/gmh5225/veh_hide_memory

## Related

[[no-access-protection]] · [[bincon]] · [[voidmaw]] · [[veh-dumper]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
