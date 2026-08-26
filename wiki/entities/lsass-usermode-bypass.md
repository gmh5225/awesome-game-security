---
title: LSASS Usermode Bypass
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/ContionMig__LSASS-Usermode-Bypass.md
updated: 2026-08-26
confidence: medium
---

# LSASS Usermode Bypass

**C++ user-mode bypass demonstration** (ContionMig) that **reuses LSASS process handles** for cross-process memory access workflows instead of loading a kernel driver. Presented as an alternative to kernel-driver loading for certain **anti-cheat evasion** scenarios, with explicit emphasis on **practical constraints** and **stability risks** when interacting with sensitive system processes. Primary use case is studying **user-mode tradeoffs** in game anti-cheat bypass research. (source: wiki/sources/descriptions/ContionMig__LSASS-Usermode-Bypass.md)

README category: Elevating Handle By LSASS.

## Links

- Repo: https://github.com/ContionMig/LSASS-Usermode-Bypass

## Related

[[dumpy]] · [[lsass-dump-that-lsass]] · [[nobastian-v2]] · [[handle-ripper]] · [[libelevate]] · [[lsass-extend-mapper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
