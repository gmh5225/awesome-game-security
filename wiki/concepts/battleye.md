---
title: BattlEye
kind: concept
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/zouxianyu__BlindEye.md
updated: 2026-07-16
confidence: medium
---

# BattlEye

Kernel driver plus service and game module coordination. Emphasizes handle protection, process monitoring, memory scanning, and visibility into injected code / runtime tampering. Used by PUBG, Rainbow Six Siege, DayZ, and others. (source: wiki/sources/skills/anti-cheat.md)

## Research angles

Object callbacks and handle stripping, injected-module detection, pool/driver forensics, and comparison with boot-start models like [[vanguard]].

[[blindeye]] shows an offensive research angle: hook BE’s imported pool allocators and drop allocations for the kernel “report” path. (source: wiki/sources/descriptions/zouxianyu__BlindEye.md)

## Related

[[easy-anti-cheat]] · [[vanguard]] · [[blindeye]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
