---
title: opaque-predicates-detective
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md
updated: 2026-07-17
confidence: medium
---

# opaque-predicates-detective

Binary Ninja–oriented research on detecting opaque predicates. Prior generic approaches identify whether a conditional branch contains an invariant expression; damage from such predicates is localized at the basic-block (or function) level regardless of how the invariant is constructed. Useful for RE / cheat-side Binary Ninja plugin study of obfuscation. (source: wiki/sources/descriptions/yellowbyte__opaque-predicates-detective.md)

Not a full deobfuscator—scoped to opaque-predicate detection rather than wholesale unpacking.

## Links

- Repo: https://github.com/yellowbyte/opaque-predicates-detective

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[deobf]] · [[idadeflat]] · [[mutaben]]
