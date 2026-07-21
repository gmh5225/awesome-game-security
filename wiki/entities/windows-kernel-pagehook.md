---
title: windows-kernel-pagehook
kind: entity
topics: [windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/stdhu__windows-kernel-pagehook.md
updated: 2026-07-21
confidence: medium
---

# windows-kernel-pagehook

Windows kernel research sample focused on PTE (page-table entry) hooks. Kernel virtual addresses are shared across processes, but each process has a distinct CR3 (page-table root), so PTE-level hooks can be scoped per address space rather than globally. (source: wiki/sources/descriptions/stdhu__windows-kernel-pagehook.md)

Useful for low-level Windows / Linux / mobile researchers in the Some Tricks / Windows Ring0 lane—studying page-table manipulation beside kernel memory and hook research.

## Links

- Repo: https://github.com/stdhu/windows-kernel-pagehook (README tag: PTE Hook)

## Related

[[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[ntmemory]] · [[pg1903]]
