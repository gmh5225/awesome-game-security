---
title: pdblister
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/microsoft__pdblister.md
updated: 2026-07-30
confidence: medium
---

# pdblister

Rust command-line tool that generates PDB download manifests by scanning directories for PE files and extracting debug-directory CodeView GUID and age fields. Mimics `symchk /om` but runs significantly faster, constructing Microsoft Symbol Server URLs for batch PDB retrieval with both blocking and async download modes. (source: wiki/sources/descriptions/microsoft__pdblister.md)

Useful when prefetching symbols for a tree of game binaries, drivers, or system DLLs before IDA/WinDbg work—not a PDB parser itself; pair with [[pdb-rs]] (Rust MSF/CodeView read/write), [[pdbr]] (standalone Python extract), or [[pdb]] (DIA SDK) for programmatic analysis, or dbghelp symbol-server loads in debuggers.

## Links

- Repo: https://github.com/microsoft/pdblister

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[pdb-rs]] · [[pdb]] · [[pdbr]] · [[kpdb]] · [[ntsleuth]] · [[totalpe2]] · [[x64dbg]]
