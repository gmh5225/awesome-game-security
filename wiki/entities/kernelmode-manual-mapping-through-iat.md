---
title: Kernelmode Manual Mapping through IAT
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/mactec0__Kernelmode-manual-mapping-through-IAT.md
updated: 2026-07-31
confidence: medium
---

# Kernelmode Manual Mapping through IAT

Kernel-mode **IAT manual map** injector: maps a PE into a target process while resolving imports through the Import Address Table, with control via either an open **process handle** or a companion **kernel driver**. Useful for studying kernel-assisted manual-map injection paths that bypass conventional `LoadLibrary` module lists — a lane anti-cheat scanners and thread/module heuristics often target. (source: wiki/sources/descriptions/mactec0__Kernelmode-manual-mapping-through-IAT.md)

README lane: IAT Manual Map · cheat / injection:windows.

## Links

- Repo: https://github.com/mactec0/Kernelmode-manual-mapping-through-IAT

## Related

[[modexmap]] · [[shtreeba]] · [[kinject]] · [[injdrv]] · [[faultline]] · [[system-thread-finder]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
