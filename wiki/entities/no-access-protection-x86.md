---
title: no-access-protection-x86
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__no-access-protection-x86.md
updated: 2026-08-08
confidence: medium
---

# no-access-protection-x86

x86 Windows sample demonstrating **PAGE_NOACCESS page guards**: code pages are marked no-access and a **VEH handler** temporarily restores execute/read permission on demand, yielding **on-access decryption** that hinders static analysis and memory dumping. Aimed at software-protection researchers studying page-level access control for anti-tamper and anti-dump defenses. (source: wiki/sources/descriptions/gmh5225__no-access-protection-x86.md)

Pairs with related PAGE_NOACCESS / VEH samples such as [[no-access-protection]] (VEH trampoline + single-step re-protect), [[veh-hide-memory]] (memory-analysis PoC), [[page-no-access]] (lazy decrypt-on-first-access), and [[bincon]] (hardened console).

## Links

- Repo: https://github.com/gmh5225/no-access-protection-x86

## Related

[[no-access-protection]] · [[veh-hide-memory]] · [[page-no-access]] · [[bincon]] · [[voidmaw]] · [[veh-dumper]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
