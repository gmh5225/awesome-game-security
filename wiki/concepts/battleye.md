---
title: BattlEye
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zouxianyu__BlindEye.md
  - wiki/sources/descriptions/weak1337__SystemThreadFinder.md
updated: 2026-07-18
confidence: medium
---

# BattlEye

Kernel driver plus service and game module coordination. Emphasizes handle protection, process monitoring, memory scanning, and visibility into injected code / runtime tampering. Used by PUBG, Rainbow Six Siege, DayZ, and others. (source: wiki/sources/skills/anti-cheat.md)

## Research angles

Object callbacks and handle stripping, injected-module detection, pool/driver forensics, and comparison with boot-start models like [[vanguard]].

[[blindeye]] shows an offensive research angle: hook BE’s imported pool allocators and drop allocations for the kernel “report” path. (source: wiki/sources/descriptions/zouxianyu__BlindEye.md)

Thread-start heuristics (system threads whose start address is outside any loaded driver image) are reconstructed in tools such as [[system-thread-finder]], derived from BE’s thread-detection logic. (source: wiki/sources/descriptions/weak1337__SystemThreadFinder.md)

## Related

[[easy-anti-cheat]] · [[vanguard]] · [[blindeye]] · [[system-thread-finder]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
