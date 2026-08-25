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

IDA Pro plugin (Python) that generates high-confidence cross-references and indirect control-flow references that standard IDA analysis may miss, designed to extend Mandiant **XRefer** workflows. (source: wiki/sources/descriptions/seifreed__xrefgen.md)

Targets reverse engineers and malware researchers analyzing modern compiled languages, packed binaries, and heavily obfuscated game clients and anti-cheat modules. Cheat / IDA Plugins lane.

## Capabilities

- **Data-flow taint tracking** — follow register/memory flows to recover indirect targets standard xrefs miss.
- **Call-graph analysis** — propagate control-flow edges through complex calling patterns.
- **Obfuscation detection** — flags [[control-flow-flattening]] and opaque predicates during xref recovery.
- **Cross-architecture register resolution** — x86, x64, ARM, ARM64, MIPS, experimental WebAssembly.
- **XRefer-compatible export** — validated control-flow candidates with confidence scoring, evidence tracking, and incremental cached re-analysis.

Complements [[find-xrefs]] (materialize missing string/data pointer xrefs) and [[xrefsext]] (extended xref navigation) on large game clients and AC modules.

## Links

- Repo: https://github.com/seifreed/xrefgen

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[find-xrefs]] · [[xrefsext]] · [[control-flow-flattening]] · [[obfuscation-detection]] · [[opaque-predicates-detective]] · [[dragonhook]] · [[ida-plugins]]
