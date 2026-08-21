---
title: hyperion-disassembler
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/Sidenai__hyperion-disassembler.md
updated: 2026-08-21
confidence: medium
---

# hyperion-disassembler

Native C++ disassembler and decompiler with multi-architecture support (x86/x64/ARM/AArch64, plus MIPS/PPC per README). Loads PE, ELF, Mach-O, and .NET binaries; provides CFG analysis, FLIRT signature matching, PDB loading, BinDiff comparison, RTTI recovery, packer detection, Lua scripting, and an ImGui-based UI. The SSA decompiler lifts machine code to structured pseudocode for protected-game and malware RE workflows. (source: wiki/sources/descriptions/Sidenai__hyperion-disassembler.md)

Complements graph-based diffing via [[binexport]] and library-ID tooling such as [[sig-database]] when comparing builds or identifying statically linked functions. Packer-detection and unpack lanes such as [[unpacker]] overlap on heuristic packer ID; distinct from Roblox Byfron/Hyperion anti-tamper PE dump tooling such as [[vulkan]] and [[page-no-access-not-byfron]] despite the shared "Hyperion" name.

## Links

- Repo: https://github.com/Sidenai/hyperion-disassembler

## Related

[[overviews/reverse-engineering]] · [[binexport]] · [[sig-database]] · [[unpacker]] · [[retdec]] · [[ghidra]] · [[xdv]]
