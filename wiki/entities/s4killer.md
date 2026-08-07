---
title: s4killer
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__s4killer.md
updated: 2026-08-07
confidence: medium
---

# s4killer

BYOVD research PoC exploiting the Samsung **S4** vulnerable kernel driver **`probmon.sys`**. Crafted IOCTLs to the signed Samsung driver yield arbitrary physical or virtual kernel read/write—primitives commonly used to load unsigned drivers, patch kernel structures, or bypass anti-cheat protections. Aimed at BYOVD researchers studying Samsung driver vulnerabilities for kernel access. (source: wiki/sources/descriptions/gmh5225__s4killer.md)

## Links

- Repo: https://github.com/gmh5225/s4killer

## Related

[[byovd]] · [[vdk]] · [[zam64-zemina]] · [[loldrivers]] · [[physmem-drivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
