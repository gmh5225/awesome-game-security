---
title: FakePDB
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__FakePDB.md
updated: 2026-08-13
confidence: medium
---

# FakePDB

Tool that **generates fake PDB** (Program Database) files for executables lacking debug symbols. Exports synthetic symbol information derived from IDA analysis results so PDB-consuming debuggers and analyzers can resolve function names, types, and addresses for source-level debugging on stripped binaries. README category: PDB Generation From IDA. (source: wiki/sources/descriptions/gmh5225__FakePDB.md)

Complements official symbol recovery ([[pdb]], [[pdb-rs]], [[pdblister]]) and linker `.MAP` import workflows ([[ida-pro-loadmap]], [[x64dbg-mapldr]]): when no build-time PDB or MAP exists, FakePDB bridges IDA static analysis into WinDbg/x64dbg/Visual Studio symbol pipelines.

## Links

- Repo: https://github.com/gmh5225/FakePDB

## Related

[[overviews/reverse-engineering]] · [[pdb]] · [[pdb-rs]] · [[pdblister]] · [[unreal-engine-5-pdb]] · [[ida-pro-loadmap]] · [[x64dbg-mapldr]] · [[x64dbg]]
