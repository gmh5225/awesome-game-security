---
title: HexWalk
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gcarmix__HexWalk.md
updated: 2026-08-15
confidence: medium
---

# HexWalk

Qt-based cross-platform **hex editor and binary analysis workbench** that combines editing, disassembly, entropy visualization, signature scanning, diffing, and format-aware overlays in one GUI. Integrates Capstone disassembly, binwalk signature scanning, file diffing, byte-map visualization, string extraction, and cryptographic hashing. YAML-defined file-format patterns (ELF, PE, JPEG, PDF, WAV) drive structured overlay highlighting; a QHexEdit widget provides undo/redo, search, and color-tagged region annotations. (source: wiki/sources/descriptions/gcarmix__HexWalk.md)

Useful for static triage of game binaries, packed assets, and firmware blobs before deeper IDA/Ghidra work—complements PE-focused viewers such as [[pe-bear]] and [[totalpe2]], standalone string tools such as [[strings2]], and bundled lab installs such as [[retoolkit]].

## Links

- Repo: https://github.com/gcarmix/HexWalk

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[pe-bear]] · [[totalpe2]] · [[strings2]] · [[retoolkit]]
