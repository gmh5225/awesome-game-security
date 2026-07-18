---
title: BE-Shellcode
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/weak1337__BE-Shellcode.md
updated: 2026-07-18
confidence: medium
---

# BE-Shellcode

Research tool for analyzing [[battleye]] **user-mode shellcode**: dump, disassemble, and document the detection modules BE injects into protected game processes. Reimplements key shellcode lanes—system thread scanning (`systhreadfinder.cpp` / `thread_scan.cpp`), VEH handler enumeration (`veh.cpp`), module walking (`modules.cpp`), plus signature-based integrity checks—so researchers can study BE’s in-process detection architecture offline. (source: wiki/sources/descriptions/weak1337__BE-Shellcode.md)

Overlaps the standalone [[system-thread-finder]] sample (same author; BE-derived thread heuristics) and complements kernel-side BE research such as [[blindeye]].

## Links

- Repo: https://github.com/weak1337/BE-Shellcode

## Related

[[battleye]] · [[system-thread-finder]] · [[blindeye]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[veh-dumper]] · [[present-hook-detection]]
