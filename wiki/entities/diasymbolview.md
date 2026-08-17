---
title: DiaSymbolView
kind: entity
topics: [reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/diversenok__DiaSymbolView.md
updated: 2026-08-16
confidence: medium
---

# DiaSymbolView

Delphi-based GUI for visually inspecting debug symbols and their 200+ properties stored in Windows PDB files via the Microsoft MSDIA (Debug Interface Access) API. Presents a navigable hierarchy of symbol types, functions, variables, and compilation units with full property enumeration and register-name resolution. (source: wiki/sources/descriptions/diversenok__DiaSymbolView.md)

Mainly useful for reverse engineers and security researchers examining PDB debug-information structure and symbol metadata for Windows binaries—not a debugger or disassembler; pair with [[pdb]] (DIA SDK parse/merge), [[pdb-rs]] (Rust MSF/CodeView read/write), [[pdbr]] (standalone Python extract), or [[pdblister]] (Symbol Server manifest batch download) when moving from inspection to automation.

## Links

- Repo: https://github.com/diversenok/DiaSymbolView

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[pdb]] · [[pdb-rs]] · [[pdblister]] · [[pdbr]] · [[fakepdb]] · [[ntsleuth]] · [[kpdb]] · [[x64dbg]]
