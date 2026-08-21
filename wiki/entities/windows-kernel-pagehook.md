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

Useful for low-level Windows / Linux / mobile researchers in the Some Tricks / Windows Ring0 lane—studying page-table manipulation beside kernel memory and hook research. PTE redirection demos such as [[page-table-hook]] construct/edit paging structures instead of inline code patches. Hidden/shadowed memory region PoCs such as [[yumekage]] extend the same PTE Hook lane with guarded-region concealment tied to context switches.

## Links

- Repo: https://github.com/stdhu/windows-kernel-pagehook (README tag: PTE Hook)

## Related

[[page-table-hook]] · [[yumekage]] · [[fast-pf-hook]] · [[pteditor]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[ntmemory]] · [[pg1903]]

