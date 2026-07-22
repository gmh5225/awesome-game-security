---
title: pdb
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/sonyps5201314__pdb.md
updated: 2026-07-22
confidence: medium
---

# pdb

Windows PDB (Program Database) parsing and manipulation tool in C++ on the Microsoft DIA (Debug Interface Access) SDK. Reads, merges, and analyzes PDB symbol files, with support for older PDB formats and `pdb.cfg` configuration. Aimed at reverse engineers and debugger developers who need programmatic access to Windows debug symbols (README: PDB plugin with enhance and bugfix). (source: wiki/sources/descriptions/sonyps5201314__pdb.md)

Useful when resolving types/names from Microsoft or custom PDBs before deeper IDA/WinDbg work, or when merging/inspecting symbol databases—not a debugger itself.

## Links

- Repo: https://github.com/sonyps5201314/pdb

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[ntsleuth]] · [[totalpe2]] · [[dotniet]] · [[x64dbg]]
