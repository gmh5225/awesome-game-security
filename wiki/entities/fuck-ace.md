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

**fuckAce** (moeskia) — Windows console utility (C, MinGW-w64) that **reduces Tencent ACE (SGuard) CPU overhead** by throttling `SGuard64.exe` and `SGuardSvc64.exe`. Runs locally with administrator privileges and `SeDebugPrivilege`, prints a formatted results table, and automatically retries when ACE self-protection blocks some operations. No network I/O or on-disk modifications. Aimed at researchers and users studying or mitigating anti-cheat resource consumption on Windows. README lane: Cheat / Explore AntiCheat System:ACE. (source: wiki/sources/descriptions/moeskia__fuckAce.md)

## Mechanism

For each matched SGuard process, fuckAce applies three user-mode mitigations:

1. **Idle priority** — lowers scheduling weight so ACE background work yields CPU time.
2. **Last-CPU affinity** — pins the process to the final logical processor, isolating contention from primary game cores.
3. **EcoQoS** — enables `ProcessPowerThrottling` so Windows treats the process as efficiency-class work.

Complements kernel ACE restriction tooling such as [[sguard-limit]] and research-host utilities such as [[anticheattoggle]]; defensive ACE byte-level analysis such as [[ff-ace-anticheat-analysis]] covers a different evidence lane.

## Links

- Repo: https://github.com/moeskia/fuckAce

## Related

[[sguard-limit]] · [[anticheattoggle]] · [[ff-ace-anticheat-analysis]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
