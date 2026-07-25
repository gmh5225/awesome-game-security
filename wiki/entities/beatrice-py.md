---
title: Beatrice.py
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/raskolnikov90__Beatrice.py.md
updated: 2026-07-25
confidence: medium
---

# Beatrice.py

Python tool that mutates x86-64 machine code by substituting instructions with semantically equivalent alternative encodings. Replaces original opcodes with functionally identical but byte-different sequences via pattern matching and substitution rules, aimed at studying instruction-level binary mutation for AV / anti-cheat signature evasion and binary diversity. (source: wiki/sources/descriptions/raskolnikov90__Beatrice.py.md)

Useful alongside polymorphic shredders such as [[shredder-rs]] and metamorphic transforms such as [[r2morph]] in the AC obfuscation / signature-mutation research lane—not a game client or AC product itself.

## Links

- Repo: https://github.com/raskolnikov90/Beatrice.py

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[shredder-rs]] · [[r2morph]]
