---
title: lsass-extend-mapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/zorftw__lsass-extend-mapper.md
updated: 2026-07-17
confidence: medium
---

# lsass-extend-mapper

Windows research mapper that loads unsigned kernel drivers by **extending lsass.exe’s address space** and using that process context for kernel operations. It leans on lsass’s trusted status to map driver code while avoiding standard driver-load traces (PiDDB / MmUnloadedDrivers-style paths). C++ demo of process-context-based kernel execution for researchers studying trusted-process mapping. (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md)

Companion research lane to post-map cleanup tools such as [[revert-mapper]]—here the focus is *how* the map is hosted (lsass extend), not artifact reversion.

## Links

- Repo: https://github.com/zorftw/lsass-extend-mapper

## Related

[[revert-mapper]] · [[byovd]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
