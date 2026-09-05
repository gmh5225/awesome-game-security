---
title: ghidra-hexeditor
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/sengi12__ghidra-hexEditor.md
updated: 2026-08-21
confidence: medium
---

# ghidra-hexeditor

Dockable hex editor Ghidra script plugin for viewing and patching the raw bytes of a program loaded in Ghidra. Written primarily in Java with a Swing-based UI forked from javadev/hexeditor; opens as a dockable Ghidra window alongside the Listing and Decompiler or falls back to a standalone window when docking is unavailable. Supports in-place byte editing, binary search, saving modified executables through Ghidra's BinaryExporter, and automatically matches Ghidra's look and feel including optional dark mode. Aimed at reverse engineering and game security workflows where researchers need to inspect and patch binaries without leaving the Ghidra environment. (source: wiki/sources/descriptions/sengi12__ghidra-hexEditor.md)

In-Ghidra byte editing complements standalone hex workbenches such as [[imhex]] and [[hexwalk]], and sits beside other Ghidra plugin tooling such as [[scalpel]], [[ghidra-findcrypt]] and [[ghidra-nativeaot]].

## Links

- Repo: https://github.com/sengi12/ghidra-hexEditor

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[scalpel]] · [[imhex]] · [[hexwalk]] · [[ghidra-findcrypt]]
