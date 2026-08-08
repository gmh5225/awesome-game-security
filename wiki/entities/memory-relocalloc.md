---
title: memory-relocalloc
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__memory-relocalloc.md
updated: 2026-08-08
confidence: medium
---

# memory-relocalloc

Demonstrates **memory relocation/allocation hiding** on Windows or Android: allocates or relocates memory via unconventional paths—using the PE **`.reloc` section** instead of typical `VirtualAlloc` / heap APIs—to evade anti-cheat memory scanners that enumerate standard heap and virtual-memory regions. Aimed at game-security researchers studying memory-hiding techniques and AC memory-scanning evasion. (source: wiki/sources/descriptions/gmh5225__memory-relocalloc.md)

Complements PE relocation research such as [[relocbonus]] and page-protection hiding samples such as [[veh-hide-memory]] / [[shellcode-fluctuation]] when the threat model is **VAS/heap enumeration** rather than VEH or protection fluctuation alone.

## Links

- Repo: https://github.com/gmh5225/memory-relocalloc

## Related

[[relocbonus]] · [[veh-hide-memory]] · [[shellcode-fluctuation]] · [[battleye-region-walking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
