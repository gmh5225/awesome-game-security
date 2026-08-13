---
title: EAC-shellcode-1
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__EAC-shellcode-1.md
updated: 2026-08-13
confidence: medium
---

# EAC-shellcode-1

Archived dump of [[easy-anti-cheat]] **user-mode shellcode** recovered from a protected game around March 2023 (gmh5225). The repository holds a raw memory image (`shellcode_size0x82C000.mem`, ~8.5 MB) plus a short README from a protected-game dumper identifying it as anti-cheat shellcode—not a reusable implementation. (source: wiki/sources/descriptions/gmh5225__EAC-shellcode-1.md)

The README records two execution entry points exposed through the protected game's inline hook at **base+0x79204** and **base+0x79304**, useful anchors when mapping hook-driven execution flow and shellcode layout offline. Best treated as sample material for reverse engineering EAC shellcode structure, paralleling BattlEye shellcode RE corpora such as [[be-shellcode]] and [[be-shellcode-dump]]. README category: Shellcode.

## Links

- Repo: https://github.com/gmh5225/EAC-shellcode-1

## Related

[[easy-anti-cheat]] · [[eac]] · [[easyanticheat-reversing]] · [[be-shellcode]] · [[be-shellcode-dump]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
