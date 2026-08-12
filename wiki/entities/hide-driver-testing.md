---
title: HideDriverTesting
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__HideDriverTesting.md
updated: 2026-08-12
confidence: medium
---

# HideDriverTesting

Kernel driver-hide implementation that erases loading artifacts from **MmUnloadedDrivers**, **PsLoadedModuleList**, **PiDDBCacheTable**, and driver object lists. Built for Windows 11 21H2 stress testing against the same forensics surfaces anti-rootkit tools and AC drivers use to spot hidden or manually mapped drivers. (source: wiki/sources/descriptions/gmh5225__HideDriverTesting.md)

Broader than Flink/Blink-only unlink samples such as [[hide-driver]] — targets multiple kernel data structures used in PiDDBCache / unload-buffer / module-enumeration forensics. Pairs with defensive inspection via [[openark]] and load-artifact concepts in [[kernel-pool-scanning]].

## Links

- Repo: https://github.com/gmh5225/HideDriverTesting

## Related

[[hide-driver]] · [[hide-file]] · [[nullmap]] · [[kernel-pool-scanning]] · [[openark]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
