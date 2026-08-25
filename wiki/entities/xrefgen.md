---
title: XrefGen
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/seifreed__xrefgen.md
  - wiki/sources/README-categories.md
updated: 2026-08-25
confidence: medium
---

# XrefGen

IDA Pro plugin (Python) that generates high-confidence cross-references and indirect control-flow references that standard IDA analysis may miss, designed to extend Mandiant XRefer workflows. Modular analyzers cover data-flow taint tracking, call-graph analysis, obfuscation detection (control-flow flattening, opaque predicates), and cross-architecture register resolution across x86, x64, ARM, ARM64, MIPS, and experimental WebAssembly. Exports validated control-flow candidates in XRefer-compatible format with confidence scoring, evidence tracking, and incremental cached re-analysis. (source: wiki/sources/descriptions/seifreed__xrefgen.md)

Targets reverse engineers and malware researchers analyzing modern compiled languages, packed binaries, and heavily obfuscated game clients and anti-cheat modules. Cheat / IDA Plugins lane.

## Links

- Repo: https://github.com/seifreed/xrefgen

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[find-xrefs]] · [[xrefsext]] · [[control-flow-flattening]] · [[ida-plugins]]
