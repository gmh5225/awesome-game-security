---
title: microavx
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gaasedelen__microavx.md
updated: 2026-08-15
confidence: medium
---

# microavx

IDA Pro plugin that extends the Hex-Rays decompiler by lifting Intel AVX (Advanced Vector Extensions) instructions into Hex-Rays microcode. Functions that would otherwise show opaque `ext` nodes can decompile into readable pseudocode once AVX opcodes are replaced with equivalent microcode sequences. (source: wiki/sources/descriptions/gaasedelen__microavx.md)

Implementation uses a custom microcode instruction visitor that intercepts `m_ext` opcodes and substitutes matching microcode. A companion scraping script enumerates unsupported instructions across an IDB to map AVX coverage gaps. Cheat / IDA Plugins lane (`[AVX Lifter]`). (source: wiki/sources/descriptions/gaasedelen__microavx.md)

## Links

- Repo: https://github.com/gaasedelen/microavx

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[genmc]] · [[happyida]] · [[qsynthesis]] · [[ida2llvm]]
