---
title: fuckAce
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/moeskia__fuckAce.md
  - wiki/sources/README-categories.md
updated: 2026-09-18
confidence: medium
---

# fuckAce

**fuckAce** (moeskia) — Windows console utility (C, MinGW-w64) that **reduces Tencent ACE (SGuard) CPU overhead** by throttling `SGuard64.exe` and `SGuardSvc64.exe`. For each match it applies idle process priority, pins affinity to the last logical CPU, and enables EcoQoS via `ProcessPowerThrottling`. Runs locally with administrator privileges and `SeDebugPrivilege`, prints a formatted results table, and retries when ACE self-protection blocks operations. No network I/O or on-disk modifications. README lane: Cheat / Explore AntiCheat System:ACE. (source: wiki/sources/descriptions/moeskia__fuckAce.md)

Complements ACE restriction tooling such as [[sguard-limit]] and research-host utilities such as [[anticheattoggle]]; defensive ACE byte-level analysis such as [[ff-ace-anticheat-analysis]] covers a different evidence lane.

## Links

- Repo: https://github.com/moeskia/fuckAce

## Related

[[sguard-limit]] · [[anticheattoggle]] · [[ff-ace-anticheat-analysis]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
