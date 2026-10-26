---
title: HexLab
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/imattas__HexLab.md
  - wiki/sources/README-categories.md
updated: 2026-10-26
confidence: medium
---

# HexLab

**HexLab** (imattas) is an open-source C++20 reverse-engineering workbench with a wxWidgets GUI, headless CLI, and debug server sharing the same analysis engines. (source: wiki/sources/descriptions/imattas__HexLab.md)

## Capabilities

- **Formats:** raw images, PE, ELF, Mach-O, Windows minidumps, firmware, and managed metadata.
- **Architectures:** x86, ARM, AArch64, PowerPC, MIPS, and RISC-V disassembly and decompilation.
- **Views:** synchronized disassembly, bytes, CFGs, and pseudocode; cross-references, strings, types, CFG-aware binary diff, SQLite project persistence, plugin SDK.
- **Debug:** native Win32 and Linux x86-64, GDB Remote Serial Protocol, Python automation.

## Audience

Malware and game binary analysts who want a self-contained desktop RE suite beside [[orress]], [[ceasta]], and [[sako-restudio]]. (source: wiki/sources/descriptions/imattas__HexLab.md)

## Links

- Repo: https://github.com/imattas/HexLab

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[orress]] · [[n0xis]] · [[ceasta]]
