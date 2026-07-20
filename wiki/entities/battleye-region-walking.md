---
title: battleye-region-walking
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/tr1xxx__battleye-region-walking.md
updated: 2026-07-20
confidence: medium
---

# battleye-region-walking

C++ research sample that reconstructs [[battleye]] **VirtualQuery-based memory region walking** used to flag injected code in a process VAS. Enumerates regions and applies BE-style filters on protection flags, region size, memory type (`MEM_PRIVATE` / `MEM_MAPPED`), and address heuristics to classify regions as valid or invalid—targeting shellcode and manual-mapped modules. Useful for AC researchers studying BE’s memory-scanning detection methodology offline. (source: wiki/sources/descriptions/tr1xxx__battleye-region-walking.md)

Complements [[be-shellcode]] (UM shellcode dump/disasm including module walking) and manual-map samples such as [[modexmap]].

## Links

- Repo: https://github.com/tr1xxx/battleye-region-walking

## Related

[[battleye]] · [[be-shellcode]] · [[modexmap]] · [[system-thread-finder]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
