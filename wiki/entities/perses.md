---
title: perses
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/mike1k__perses.md
updated: 2026-07-30
confidence: medium
---

# perses

**x86 code obfuscation engine** for **Portable Executable** files. Obfuscation replaces a selected instruction with a larger, semantically equivalent instruction sequence—instruction-level expansion rather than whole-function virtualizers or packers. Aimed at anti-cheat engineers and defensive security researchers in the Anti Cheat → Obfuscation Engine lane. (source: wiki/sources/descriptions/mike1k__perses.md)

Useful as a PE instruction-expansion reference alongside post-compile mutators such as [[alcatraz]] and [[binprotect]], and polymorphic shredding tools such as [[shredder-rs]]—not a commercial protector or unpacker.

## Links

- Repo: https://github.com/mike1k/perses

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[alcatraz]] · [[binprotect]] · [[shredder-rs]] · [[beatrice-py]] · [[wprotect]]
