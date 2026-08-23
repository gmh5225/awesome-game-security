---
title: GhidrOrean
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Marisa-Chan__GhidrOrean.md
updated: 2026-08-23
confidence: medium
---

# GhidrOrean

Ghidra Python reimplementation of Deathway's Oreans Unvirtualizer for analyzing and recovering code protected by Oreans virtualization (Themida, WinLicense, Code Virtualizer). Ports and extends unvirtualizer logic into Ghidra so researchers can inspect, improve, and run the tooling in a modern RE environment. Includes assembler and instruction configuration for Oreans VM families CISC, RISC, FISH, and TIGER — CISC marked complete and TIGER largely finished. Entry is through the main Orean Ghidra script, loading configs from a configurable working directory. Aimed at reverse engineers and game-security researchers working on Oreans-protected binaries. (source: wiki/sources/descriptions/Marisa-Chan__GhidrOrean.md)

Companion surface to Cheat → Fix Themida work ([[tde]] IDA devirt, [[themida-unmutate]] static mutation deobf, [[themida-research]] VM internals): **Ghidra-native Oreans VM unvirtualization** rather than IDA-only plugins or live unpack automation.

## Links

- Repo: https://github.com/Marisa-Chan/GhidrOrean

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[tde]] · [[themida-unmutate]] · [[themida-research]] · [[themida-spotter-bn]] · [[bobalkkagi]] · [[unlicense]]
