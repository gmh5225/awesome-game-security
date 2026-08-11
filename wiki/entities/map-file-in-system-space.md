---
title: Map file in system space
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Map-file-in-system-space.md
updated: 2026-08-11
confidence: medium
---

# Map file in system space

Kernel-mode research PoC (**MiMapViewInSystemSpace**) that maps a file directly into **system address space** using internal NT memory-manager APIs — notably `MmCreateSection` and related undocumented paths such as `MiMapViewInSystemSpace` — instead of conventional kernel file I/O. File contents land in kernel memory without the usual read/write path, supporting **stealthy unsigned driver load** study when paired with DSE bypass or manual-map entry stubs. (source: wiki/sources/descriptions/gmh5225__Map-file-in-system-space.md)

README lane: MiMapViewInSystemSpace · cheat / windows kernel explorer.

## Links

- Repo: https://github.com/gmh5225/Map-file-in-system-space

## Related

[[saturn-mapper]] · [[nullmap]] · [[kernel-research-kit]] · [[dse-hook]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
