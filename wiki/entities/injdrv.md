---
title: injdrv
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wbenny__injdrv.md
updated: 2026-07-18
confidence: medium
---

# injdrv

Windows kernel-mode DLL injector driver (C) that delivers injection via **APC** from Ring0. Registers a process-creation callback to catch target startup, then queues a user-mode APC that loads the DLL through `LdrLoadDll`. Kernel-originated APC injection avoids many user-mode inject APIs and hooks that anti-cheat scanners watch; useful for researchers studying kernel injection primitives and how AC detects them. (source: wiki/sources/descriptions/wbenny__injdrv.md)

Contrasts with user-mode manual-map injectors such as [[modexmap]] and injection-testing harnesses such as [[injectors]].

## Links

- Repo: https://github.com/wbenny/injdrv

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[kernel-callbacks]] · [[modexmap]] · [[injectors]] · [[scfw]]
