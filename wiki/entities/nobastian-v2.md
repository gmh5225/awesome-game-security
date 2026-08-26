---
title: NoBastian v2
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/ZoondEngine__NoBastian_v2.md
updated: 2026-08-19
confidence: medium
---

# NoBastian v2

Windows **C++ client/server toolkit** (ZoondEngine) for **process memory interaction over named pipes**. The server exposes structured operations — remote read/write, protection changes, remote allocation, and module-base queries — while the client issues typed requests. Utility code inspects **system handles** and **process access state** to acquire usable handles before performing memory work. Used for low-level game-hacking research and **handle-based anti-cheat evasion** experiments. (source: wiki/sources/descriptions/ZoondEngine__NoBastian_v2.md)

README category: Elevating Handle By LSASS.

## Links

- Repo: https://github.com/ZoondEngine/NoBastian_v2

## Related

[[libelevate]] · [[handle-ripper]] · [[lsass-dump-that-lsass]] · [[lsass-usermode-bypass]] · [[lsass-extend-mapper]] · [[km-um-communication]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
