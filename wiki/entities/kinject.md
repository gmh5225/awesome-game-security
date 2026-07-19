---
title: kinject
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/w1u0u1__kinject.md
updated: 2026-07-19
confidence: medium
---

# kinject

Kernel-oriented Windows injection sample (C/C++) focused on **map + APC** in the cheat / injection:windows lane. Combines mapping with APC delivery so researchers can study how Ring0-originated inject paths differ from classic user-mode CreateRemoteThread / LoadLibrary flows that anti-cheat scanners watch. (source: wiki/sources/descriptions/w1u0u1__kinject.md)

Related kernel APC injectors include [[injdrv]] (process-create notify → user APC → `LdrLoadDll`). Contrasts with user-mode PE manual-map tools such as [[modexmap]] and injection-testing harnesses such as [[injectors]].

## Links

- Repo: https://github.com/w1u0u1/kinject

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[injdrv]] · [[modexmap]] · [[injectors]] · [[kernel-callbacks]]
