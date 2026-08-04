---
title: TinyLoad
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/iamsopotatoe-coder__TinyLoad.md
updated: 2026-08-04
confidence: medium
---

# TinyLoad

Minimal Windows **PE loader** that manually maps executables into memory, resolves imports, applies relocations, and runs the entry point **without** the standard Windows loader APIs. README lane: simple PE **packer/crypter** that compresses and encrypts payloads via a custom VM into a self-extracting stub. Useful for studying manual-map PE loading, stub-based packing, and how anti-cheat / AV scanners fingerprint non-standard load paths. (source: wiki/sources/descriptions/iamsopotatoe-coder__TinyLoad.md)

## Links

- Repo: https://github.com/iamsopotatoe-coder/TinyLoad

## Related

[[modexmap]] · [[packer]] · [[x64-exe-packer]] · [[xorpacker]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
