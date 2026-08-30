---
title: kdmapper-1909
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Brattlof__kdmapper-1909.md
updated: 2026-08-30
confidence: medium
---

# kdmapper-1909

Windows kernel **driver mapper** fork tailored for **Windows 10 builds 1809, 1903, and 1909**. C++ code loads the vulnerable Intel **`iqvw64e.sys`** interface and uses it for privileged kernel memory operations: manual mapping routines, PE parsing helpers, and service management logic to deploy unsigned drivers from user mode. Used for Windows kernel security research, low-level driver experimentation, and anti-cheat bypass studies. (source: wiki/sources/descriptions/Brattlof__kdmapper-1909.md)

Build-pinned variant in the [[kdmapper]] family alongside the canonical TheCruZ mapper, Rust ports such as [[kdmapper-rs]], and mapper catalogs such as [[known-driver-mappers]].

## Links

- Repo: https://github.com/Brattlof/kdmapper-1909
- Backend: `iqvw64e.sys`

## Related

[[kdmapper]] · [[kdmapper-rs]] · [[cve-2015-2291]] · [[byovd]] · [[known-driver-mappers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
