---
title: WoWDumpFix
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/adde88__WoWDumpFix.md
updated: 2026-08-19
confidence: medium
---

# WoWDumpFix

[[x64dbg]] plugin (C/C++) that **removes anti-dumping obstacles** from protected Blizzard game processes so reverse engineers can capture and analyze live game binaries. Includes debugger-focused patches such as restoring expected breakpoint behavior during process attach. Designed to pair with **Scylla** for import reconstruction and dump fixing after memory capture. Primary use case is reverse engineering and static analysis of game binaries that employ anti-tamper measures—not a standalone unpacker. (source: wiki/sources/descriptions/adde88__WoWDumpFix.md)

Complements title-specific WoW tooling such as [[dumpwow]] (offline module unpack) and [[wow-iat-fix]] (IAT repair) in the Blizzard client RE lane.

## Links

- Repo: https://github.com/adde88/WoWDumpFix

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[x64dbg]] · [[dumpwow]] · [[wow-iat-fix]]
