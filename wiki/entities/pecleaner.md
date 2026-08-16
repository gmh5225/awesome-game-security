---
title: PECleaner
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/colinsenner__PECleaner.md
updated: 2026-08-16
confidence: medium
---

# PECleaner

C# Windows utility that **sanitizes PE (Portable Executable) binaries** by zeroing or removing compilation artifacts used for attribution and fingerprinting: **Rich header** data, debug directories, PDB paths, linker version strings, and compiler timestamps on **x86/x64** images. README lane: strips Rich header information from PE files; aimed at red-team operators, malware researchers, and developers who want to ship stripped executables without toolchain-identifying metadata. (source: wiki/sources/descriptions/colinsenner__PECleaner.md)

Complements MSVC Rich Header **read** tooling such as [[compiler-binary-richprint]] from the opposite direction, and extends debug-only strippers such as [[debug-remover]] to timestamps and Rich-header compiler IDs. Pairs with PE viewers/editors ([[pe-bear]], [[totalpe2]], [[kitsupe]]) for verifying what metadata remains after cleanup.

## Links

- Repo: https://github.com/colinsenner/PECleaner

## Related

[[compiler-binary-richprint]] · [[debug-remover]] · [[pe-bear]] · [[totalpe2]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
