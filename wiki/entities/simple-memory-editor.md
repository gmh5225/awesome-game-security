---
title: SimpleMemoryEditor
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/daveymcq__SimpleMemoryEditor.md
updated: 2026-09-01
confidence: medium
---

# SimpleMemoryEditor

**SimpleMemoryEditor** (daveymcq/SimpleMemoryEditor) is a portable Windows memory scanner and editor built as a full-featured game cheating utility. Written in C with a custom NCRT runtime and a Win32 GUI, it attaches to running processes, enumerates writable memory regions, and scans for integer, float, or double values using equal, increased, or decreased search filters. It supports live value modification, address freezing, and process monitoring, and builds as statically linked 32-bit and 64-bit executables for Windows XP through Windows 10. (source: wiki/sources/descriptions/daveymcq__SimpleMemoryEditor.md)

## Capabilities

- Process attach with writable memory-region enumeration
- Value scans for int, float, and double with equal / increased / decreased filters
- Live memory editing and address freezing
- Process monitoring UI
- Portable static 32-bit and 64-bit Windows builds (XP–Win10)

## Use cases

Useful for game hacking, reverse engineering in-game variables, and studying external memory editing techniques relevant to game security and anti-cheat research. (source: wiki/sources/descriptions/daveymcq__SimpleMemoryEditor.md)

## Links

- Repo: https://github.com/daveymcq/SimpleMemoryEditor

## Related

[[cheat-engine]] · [[pointer-lab]] · [[mhsx]] · [[intro-to-gamehacking]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
