---
title: ghidra-orbis
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/astrelsky__GhidraOrbis.md
updated: 2026-08-18
confidence: medium
---

# ghidra-orbis

Ghidra extension for **PlayStation 4 Orbis** binaries and related firmware artifacts. Provides loaders, analyzers, scripts, syscall data, and NID mapping resources to improve symbol recovery and platform-specific analysis. Java/Gradle-based; integrates with Ghidra's extension model and can pair with optional C++ class-analysis tooling. Primary use case is console reverse engineering and game-security research on PS4 software. (source: wiki/sources/descriptions/astrelsky__GhidraOrbis.md)

Ghidra-side peer to IDA's [[ida-ps4-helper]] for PlayStation static RE; complements platform-specific Ghidra loaders such as [[gba-ghidra-loader]]. Gradle-based builds may use the archived [[ghidra-gradle-plugin]] from the same maintainer for extension packaging.

## Links

- Repo: https://github.com/astrelsky/GhidraOrbis (README tag: Orbis OS specific software and file formats)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ida-ps4-helper]] · [[ida-ps5-elf-plugin]] · [[cssfontface-exploit]] · [[gba-ghidra-loader]]
