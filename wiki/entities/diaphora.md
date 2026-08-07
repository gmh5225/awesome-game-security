---
title: Diaphora
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/joxeankoret__diaphora.md
updated: 2026-08-03
confidence: medium
---

# Diaphora

Advanced open-source binary diffing tool implemented as an IDA Pro Python plugin. Compares two binaries at function granularity using control-flow graph matching, basic-block hash comparison, instruction mnemonics, string references, and call-graph topology. Supports partial matching, porting symbols and comments between database versions, and generating detailed diff reports. Aimed at reverse engineers, vulnerability researchers, and patch analysts tracking code changes across software versions—including anti-cheat driver updates and obfuscated client rebuilds. (source: wiki/sources/descriptions/joxeankoret__diaphora.md)

Primary open-source alternative to commercial BinDiff in the IDA workflow; complements Google's protobuf export pipeline via [[binexport]] → BinDiff, curated plugin packs such as [[idaplugins]], [[turbodiff]], and patch-oriented tooling like [[genpatch]].

## Links

- Repo: https://github.com/joxeankoret/diaphora

## Related

[[overviews/reverse-engineering]] · [[binexport]] · [[idaplugins]] · [[turbodiff]] · [[genpatch]] · [[patch-finder]] · [[cognitor]]
