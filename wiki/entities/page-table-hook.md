---
title: PageTableHook
kind: entity
topics: [windows-kernel, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Rythorndoran__PageTableHook.md
updated: 2026-08-21
confidence: medium
---

# PageTableHook

Windows kernel hooking demonstration (Rythorndoran) that modifies **page-table mappings** instead of directly patching executable code. The C++ driver constructs and edits paging structures to redirect execution to hook handlers while preserving access to original routines. The sample intercepts system paths such as `NtCreateFile` and is framed around avoiding typical [[patchguard]]-triggering inline-patch approaches—intended for advanced kernel security research and anti-cheat bypass technique study. (source: wiki/sources/descriptions/Rythorndoran__PageTableHook.md)

Sits in the Some Tricks / **PTE Hook** lane beside per-process PTE samples such as [[windows-kernel-pagehook]], guarded-region concealment in [[yumekage]], and cross-platform page-table editors such as [[pteditor]]. Same author's PFN-backed CR3 enumeration PoC [[enum-real-dirbase]] complements paging research with physical directory-base recovery.

## Links

- Repo: https://github.com/Rythorndoran/PageTableHook (README tag: PTE Hook)

## Related

[[windows-kernel-pagehook]] · [[yumekage]] · [[pteditor]] · [[fast-pf-hook]] · [[page-table-injector]] · [[enum-real-dirbase]] · [[patchguard]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
