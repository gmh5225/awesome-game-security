---
title: pdbr
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/cansarigol__pdbr.md
updated: 2026-08-17
confidence: medium
---

# pdbr

Standalone Python tool for extracting symbol information from Microsoft PDB (Program Database) debug files. Parses PDB streams to recover function names, type definitions, global variables, and source file references, outputting results in a readable Rich-formatted display. Runs without Visual Studio or the DIA SDK—aimed at reverse engineers and security researchers who need debug symbol data from PDB files for binary analysis. (source: wiki/sources/descriptions/cansarigol__pdbr.md)

Useful for quick headless PDB triage before importing symbols into IDA, x64dbg, or WinDbg. Pair with [[pdblister]] for Symbol Server prefetch, [[pdb-rs]] for programmatic Rust read/write, or [[pdb]] / [[diasymbolview]] when a DIA SDK stack is available.

## Links

- Repo: https://github.com/cansarigol/pdbr

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[pdb]] · [[pdb-rs]] · [[pdblister]] · [[diasymbolview]] · [[fakepdb]] · [[ntsleuth]] · [[kpdb]] · [[x64dbg]]
