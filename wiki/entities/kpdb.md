---
title: KPDB
kind: entity
topics: [windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/rbmm__KPDB.md
updated: 2026-07-25
confidence: medium
---

# KPDB

C++ / C/C++ project focused on **parsing PDB in a driver** (kernel-mode symbol resolution). Aimed at low-level Windows researchers in the Some Tricks → Windows Ring0 lane—driver development and modding where usermode DIA/PDB tooling is unavailable. (source: wiki/sources/descriptions/rbmm__KPDB.md)

Complements usermode PDB parse/merge tools such as [[pdb]] and syscall/PDB extractors such as [[ntsleuth]] when the research target is resolving symbols from ring 0 rather than from a debugger host.

## Links

- Repo: https://github.com/rbmm/KPDB

## Related

[[pdb]] · [[ntsleuth]] · [[ida-kmdf]] · [[overviews/windows-kernel]] · [[overviews/reverse-engineering]]
