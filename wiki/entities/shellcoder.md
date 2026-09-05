---
title: Shellcoder
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/0xricksanchez__Shellcoder.md
updated: 2026-09-05
confidence: medium
---

# Shellcoder

**Binary Ninja plugin** (Python) for **shellcode development and analysis** inside the BN workflow. Provides multi-architecture assembling and disassembling plus conversion between inline hex, spaced hex, Python byte strings, and C-style arrays — aimed at rapid payload iteration during reverse engineering, exploit prototyping, and shellcode-focused security research. (source: wiki/sources/descriptions/0xricksanchez__Shellcoder.md)

Complements standalone shellcode utilities such as [[shellcrypt]] (obfuscation/emit) and [[quickasm]] (Keystone assemble + in-process execute) with in-disassembler format cycling. Pairs with other Binary Ninja plugins such as [[seh-helper]], [[bn]], and [[binary-ninja-mcp]] in protected-binary RE and injection-tradeworkflow lanes.

## Links

- Repo: https://github.com/0xricksanchez/Shellcoder (README: BinaryNinja Shellcoder Plugin)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[shellcrypt]] · [[shellcode-factory]] · [[scfw]] · [[quickasm]] · [[seh-helper]] · [[bn]] · [[binary-ninja-mcp]]
