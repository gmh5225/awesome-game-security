---
title: Finger
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/aliyunav__Finger.md
updated: 2026-08-18
confidence: medium
---

# Finger

**Cloud-backed function symbol recognition** for binary analysis: identifies unknown library or routine names by matching extracted function features against a remote recognition backend. Ships as a **Python SDK** and an **IDA Pro plugin** (IDA 7+; Python 2.7 and 3) that extract features from the current database, submit them for matching, then **rename or highlight** recognized functions in IDA. Targets reverse engineers accelerating binary triage and function recovery in malware or game-related samples. README category: Recognizing Function By Cloud. (source: wiki/sources/descriptions/aliyunav__Finger.md)

Complements local signature-based renaming ([[renamaida]]), linker `.MAP` import ([[ida-pro-loadmap]]), and pattern-based discovery ([[findfunc]]) when stripped binaries lack debug symbols or MAP files.

## Links

- Repo: https://github.com/aliyunav/Finger

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[renamaida]] · [[ida-pro-loadmap]] · [[findfunc]] · [[ida-map-symbol-parser]] · [[ida-names]]
