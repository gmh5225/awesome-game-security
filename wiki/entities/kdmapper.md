---
title: kdmapper
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/TheCruZ__kdmapper.md
  - wiki/sources/descriptions/eddeeh__kdmapper.md
  - wiki/sources/descriptions/Brattlof__kdmapper-1909.md
updated: 2026-08-30
confidence: medium
---

# kdmapper

Windows kernel **driver mapper** that loads unsigned drivers by exploiting Intel **`iqvw64e.sys`**, a vulnerable signed driver. Uses that driver's arbitrary physical memory read/write IOCTL to manually map unsigned PE drivers: kernel pool allocation, section copy, import resolution against `ntoskrnl`, relocations, and driver entry. Offers **multiple mapping options**, **trace-reduction** for common kernel bookkeeping structures, and compatibility across many modern Windows builds. C++ codebase with helper projects for symbol/offset handling and **PDB-driven workflows**. Widely used in kernel research, driver testing, and anti-cheat bypass experimentation. (source: wiki/sources/descriptions/TheCruZ__kdmapper.md)

Canonical reference implementation in the kdmapper-family lane alongside build-pinned forks such as [[kdmapper-1909]] (Brattlof; Win10 1809/1903/1909), Rust ports such as [[kdmapper-rs]], Saturn-style mappers such as [[saturn-mapper]], signed-driver section overlay mappers such as [[sinmapper]], multi-provider [[kdu]], and the underlying [[cve-2015-2291]] / [[byovd]] primitive.

## Links

- Repo: https://github.com/TheCruZ/kdmapper
- Backend: `iqvw64e.sys`

## Related

[[kdmapper-1909]] · [[kdmapper-rs]] · [[saturn-mapper]] · [[sinmapper]] · [[kdu]] · [[cve-2015-2291]] · [[byovd]] · [[known-driver-mappers]] · [[revert-mapper]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[kernel-callbacks]]
