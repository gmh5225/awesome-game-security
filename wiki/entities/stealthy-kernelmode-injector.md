---
title: Stealthy-Kernelmode-Injector
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/charliewolfe__Stealthy-Kernelmode-Injector.md
updated: 2026-08-17
confidence: medium
---

# Stealthy-Kernelmode-Injector

Windows **kernel-mode DLL injector** (C driver) that injects into target processes from ring 0 using stealth-oriented delivery paths—**APC injection**, **thread hijacking**, and **image load callbacks**—while applying anti-detection cleanup such as removing injection traces from **PEB module lists** and scrubbing **allocated memory metadata**. The sample demonstrates manual mapping via **PTE/VAD manipulation** and is framed for evading anti-cheat detection in research settings. Primarily aimed at kernel researchers studying stealthy injection tradecraft and the detection vectors those paths expose. (source: wiki/sources/descriptions/charliewolfe__Stealthy-Kernelmode-Injector.md)

README lane: PTE/VAD Manipulation Manual Map.

## Links

- Repo: https://github.com/charliewolfe/Stealthy-Kernelmode-Injector

## Related

[[kernel-vad-injector]] · [[page-table-injector]] · [[kernelmode-manual-mapping-through-iat]] · [[kinject]] · [[injdrv]] · [[stealth-apc-dispatcher]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
