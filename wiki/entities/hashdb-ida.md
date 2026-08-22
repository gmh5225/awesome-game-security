---
title: HashDB IDA
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/OALabs__hashdb-ida.md
updated: 2026-08-22
confidence: medium
---

# HashDB IDA

Python **IDA Pro** plugin that resolves **hashed API and string constants** through the **HashDB** lookup service. Context-menu integration supports single lookups, bulk module imports, and optional **XOR-aware** matching. Can hunt likely hash algorithms and annotate matches as enums directly in disassembly. Targets reverse-engineering workflows where hash-based obfuscation hides imports and string literals—common in malware, shellcode, and protected game clients. (source: wiki/sources/descriptions/OALabs__hashdb-ida.md)

Complements hash-resolution tooling on the offensive side ([[rs-ldr]], [[tabby]]) and import-reconstruction work ([[augur-riot]], [[call-obfuscator]]). Pairs with string-deobfuscation IDA plugins such as [[anti-xorstr]] and symbol-recovery helpers like [[auto-re]].

## Links

- Repo: https://github.com/OALabs/hashdb-ida

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[rs-ldr]] · [[tabby]] · [[augur-riot]] · [[call-obfuscator]] · [[anti-xorstr]] · [[auto-re]]
