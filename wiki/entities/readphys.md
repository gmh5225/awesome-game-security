---
title: ReadPhys
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/rogxo__ReadPhys.md
updated: 2026-07-24
confidence: medium
---

# ReadPhys

C/C++ method to **read physical memory by manually mapping PTEs**, without calling conventional kernel R/W APIs such as `MmCopyMemory` / `MmMapIoSpace`. Reversed from `AXE-BASE.sys`; useful for memory-analysis and ACE (Anti Cheat Expert) exploration. (source: wiki/sources/descriptions/rogxo__ReadPhys.md)

## Links

- Repo: https://github.com/rogxo/ReadPhys

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[ntmemory]] · [[windows-kernel-pagehook]]
