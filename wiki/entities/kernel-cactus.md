---
title: Kernel Cactus
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Kernel-Cactus.md
updated: 2026-08-12
confidence: medium
---

# Kernel Cactus

User-mode offensive toolkit that uses Dell's vulnerable **`dbutil_2_3.sys`** driver as its kernel read/write backend. `KernelOps.cpp` opens `\\.\DBUtil_2_3` and builds primitives on IOCTLs `0x9B0C1EC4` and `0x9B0C1EC8`, then layers higher-level post-exploitation actions: ETW disabling, PPL toggling, protected-process termination, token copying, and file deletion. The command set also includes shellcode-based remote thread injection and thread hijacking aimed at processes that resist ordinary user-mode tooling. Better described as a multifunction BYOVD post-exploitation console than a simple note about loading **`dbutil_2_3.sys`**. (source: wiki/sources/descriptions/gmh5225__Kernel-Cactus.md)

## Links

- Repo: https://github.com/gmh5225/Kernel-Cactus

## Related

[[byovd]] · [[ts-fucker]] · [[pplkiller]] · [[killer]] · [[process-killer-byovd]] · [[edrsandblast]] · [[etw-threat-intelligence]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
