---
title: Overwatch IAT Fixer
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__overwatch-iat-fixer.md
updated: 2026-08-08
confidence: medium
---

# Overwatch IAT Fixer

**Import Address Table (IAT) fixer** for Overwatch game binaries (gmh5225). Reconstructs the import table of Overwatch's protected executable by resolving obfuscated or encrypted import entries back to their original function names and addresses, enabling proper analysis in disassemblers. Aimed at game reverse engineers studying Overwatch binary protection and import obfuscation—not a general-purpose PE unpacker. (source: wiki/sources/descriptions/gmh5225__overwatch-iat-fixer.md)

Complements title-agnostic import recovery such as [[vmpimportfixer]] and cross-platform hook libraries such as [[plthook]]; pairs with Blizzard WoW IAT repair tooling such as [[wow-iat-fix]] in the same title-specific import-obfuscation lane.

## Links

- Repo: https://github.com/gmh5225/overwatch-iat-fixer

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[wow-iat-fix]] · [[vmpimportfixer]] · [[plthook]] · [[pine]]
