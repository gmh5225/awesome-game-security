---
title: AtomPePacker
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__AtomPePacker.md
updated: 2026-08-14
confidence: medium
---

# AtomPePacker

Windows PE executable packer that compresses and encrypts PE files with a runtime unpacking stub. Packs original PE sections, encrypts them, and prepends a decompression loader that restores the original binary in memory at runtime. Handles import table reconstruction, relocation fixing, and TLS callback preservation during unpacking. Listed under Anti Cheat → Binary Packer (`[PE X64]`); aimed at software protection researchers studying PE packing techniques rather than shipping as an AC product. (source: wiki/sources/descriptions/gmh5225__AtomPePacker.md)

Useful as an x64 PE packer reference alongside [[pepacker]], [[x64-exe-packer]], and [[packer]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/gmh5225/AtomPePacker

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pepacker]] · [[x64-exe-packer]] · [[packer]] · [[packer-tutorial]] · [[awesome-executable-packing]]
