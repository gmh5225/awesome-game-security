---
title: DWARFHelper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/CynicRus__DWARFHelper.md
updated: 2026-08-26
confidence: medium
---

# DWARFHelper

[[x64dbg]] plugin that parses **DWARF debug information** from ELF and PE binaries using **libdwarf**, importing function names, variable types, and source line mappings into the debugger as labels, functions, and file:line comments. Supports x86 and x64 targets. (source: wiki/sources/descriptions/CynicRus__DWARFHelper.md)

Complements Windows PDB-based symbol recovery ([[pdb]], [[pdblister]]) and linker `.MAP` import via [[x64dbg-mapldr]] when binaries embed DWARF sections (common in GCC/Clang/MinGW builds and some cross-platform game clients). Static DWARF browsing for ELF is also available via [[dwex]].

## Links

- Repo: https://github.com/CynicRus/DWARFHelper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[x64dbg-mapldr]] · [[pdb]] · [[dwex]]
