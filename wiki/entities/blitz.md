---
title: blitz
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/emlinhax__blitz.md
updated: 2026-08-15
confidence: medium
---

# blitz

Header-only C++ library that **dynamically resolves Windows modules and exports at runtime** and supports **calling resolved exports directly**—a user-mode lazy-import pattern that avoids a static IAT and reduces import-table fingerprints AC and EDR scanners target. Listed under Anti Cheat → Lazy Importer; also cited for reverse engineering, modding, and SDK-generation workflows. (source: wiki/sources/descriptions/emlinhax__blitz.md)

Complements kernel-mode lazy import via [[kli]] / [[kli-ex]], compile-time direct-syscall stubs such as [[syscalls-cpp]], and sibling emlinhax in-process value hiding via [[xv]]. Defensive analysts should treat hash-walk / manual `GetProcAddress`-style resolution in `.text` as potential lazy-import usage alongside classic IAT gaps.

## Links

- Repo: https://github.com/emlinhax/blitz

## Related

[[kli]] · [[kli-ex]] · [[syscalls-cpp]] · [[xv]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
