---
title: BinCon
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/saveme712__BinCon.md
updated: 2026-07-23
confidence: medium
---

# BinCon

Example console app hardened with **VEH + `PAGE_NOACCESS`**: protects against memory scans, memory modifications, debuggers, and related tampering. Aimed at anti-cheat engineers and defensive researchers working the page-protection lane. (source: wiki/sources/descriptions/saveme712__BinCon.md)

Pairs with related PAGE_NOACCESS / VEH samples such as [[no-access-protection]] (VEH trampoline + single-step re-protect) and [[voidmaw]] (`PAGE_GUARD` variant); VEH-chain dump tooling such as [[veh-dumper]].

## Links

- Repo: https://github.com/saveme712/BinCon

## Related

[[no-access-protection]] · [[voidmaw]] · [[veh-dumper]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
