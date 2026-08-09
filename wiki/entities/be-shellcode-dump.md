---
title: BE Shellcode Dump
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__be_shellcode_dump.md
updated: 2026-08-09
confidence: medium
---

# BE Shellcode Dump

Tool (gmh5225) for dumping [[battleye]] **runtime shellcode scanning modules** from protected game processes. Intercepts the shellcode payloads BattlEye streams and executes in-process for cheat detection, saving them for offline reverse engineering of BE detection signatures and scanning logic. README category: Reversed BE Shellcode. (source: wiki/sources/descriptions/gmh5225__be_shellcode_dump.md)

Complements [[battleye-shellcode-dumper]] (lguilhermee; pre-execution capture of server-streamed modules + decryption keys) and [[be-shellcode]] (weak1337; offline reimplementation/disasm of known BE detection lanes).

## Links

- Repo: https://github.com/gmh5225/be_shellcode_dump

## Related

[[battleye]] · [[battleye-shellcode-dumper]] · [[be-shellcode]] · [[battleye-region-walking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
