---
title: ida-search
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/milankovo__ida-search.md
updated: 2026-07-30
confidence: medium
---

# ida-search

IDA Pro 9.x plugin that brings 010 Editor–style type-aware binary search into IDA. The `ida-plugin.json` manifest loads `plugin.py` on startup. Aimed at game-security researchers and reverse engineers in the cheat / IDA Plugins lane who need structured byte-pattern queries beyond IDA’s default search. (source: wiki/sources/descriptions/milankovo__ida-search.md)

Complements signature and pattern tooling such as [[ida-fusion]] (unique sig scan/create) and [[yarascan-ida]] (Yara file scan), and Hex-Rays workflow helpers from the same author such as [[ida-enums-helper]].

## Links

- Repo: https://github.com/milankovo/ida-search

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-fusion]] · [[yarascan-ida]] · [[ida-enums-helper]] · [[idaplugins]]
