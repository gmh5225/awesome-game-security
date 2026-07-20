---
title: Rumba
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/thalium__rumba.md
updated: 2026-07-20
confidence: medium
---

# Rumba

Python framework for automated analysis of VMProtect-protected binaries. Uses symbolic execution and execution-trace analysis to identify virtual opcode handlers, extract handler semantics, and reconstruct original control flow / instruction logic from VMProtect virtualized code. Aimed at reverse engineers and malware analysts deobfuscating VMProtect-protected binaries. README tags it under Cracking MBAs / MBA simplification (handler-side MBA adjacent to tools like [[cobra]]). (source: wiki/sources/descriptions/thalium__rumba.md)

Companion surface to other Cheat → Fix VMP research (e.g. [[novmpy]], [[vmdevirt-vtil]]): trace-driven handler recovery rather than a VTIL compile demo or .NET Harmony instrumentation.

## Links

- Repo: https://github.com/thalium/rumba

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[novmpy]] · [[vmdevirt-vtil]] · [[cobra]] · [[symless]]
