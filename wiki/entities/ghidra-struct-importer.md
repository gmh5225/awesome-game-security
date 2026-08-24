---
title: ghidra-struct-importer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Katharsas__ghidra-struct-importer.md
updated: 2026-08-24
confidence: medium
---

# ghidra-struct-importer

Ghidra **GhidraScript** that imports **individual C structs** into the type manager even when they depend on previously defined types. Works around limitations of Ghidra's **Parse C Source** flow by parsing targeted structures directly and resolving dependencies in a more practical way for iterative reversing. Written in **Java** as Ghidra scripting code for modern Ghidra versions. Useful when reconstructing data layouts from **SDK leaks** or **decompiled headers** during reverse engineering and game security analysis. (source: wiki/sources/descriptions/Katharsas__ghidra-struct-importer.md)

Complements C++ metadata tooling such as [[ghidra-cpp-class-analyzer]] and manual struct workflows in [[ghidra-scripts]] when the goal is incremental type import rather than bulk header parsing.

## Links

- Repo: https://github.com/Katharsas/ghidra-struct-importer (README tag: Struct Importer)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-cpp-class-analyzer]] · [[ghidra-scripts]] · [[classmaker]]
