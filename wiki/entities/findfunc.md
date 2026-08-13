---
title: FindFunc
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__FindFunc.md
updated: 2026-08-13
confidence: medium
---

# FindFunc

IDA Pro plugin that searches for functions matching specific byte-pattern criteria or other characteristics. Filters functions by instruction sequences, operand types, cross-references, and related properties to quickly locate target functions during reverse engineering—useful when hunting game logic, anti-cheat checks, or obfuscated handlers by recognizable prologues or instruction shapes rather than names. (source: wiki/sources/descriptions/gmh5225__FindFunc.md)

Function-level pattern search inside IDA—not a byte-level YARA scanner or signature maker.

Complements signature tooling such as [[ida-fusion]], [[ida-sigmaker]], [[sigmakerex]], and [[ida-pro-sigmaker]] (unique byte-pattern generation) and library-ID plugins such as [[idenlib]]. For raw-byte YARA scans see [[findyara-ida]] and [[findcrypt-yara]].

## Links

- Repo: https://github.com/gmh5225/FindFunc

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-fusion]] · [[ida-sigmaker]] · [[idenlib]] · [[findyara-ida]] · [[findcrypt-yara]] · [[idaplugins]]
