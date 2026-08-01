---
title: Battleye Shellcode Dumper
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/lguilhermee__Battleye-Shellcode-Dumper.md
updated: 2026-08-01
confidence: medium
---

# Battleye Shellcode Dumper

Tool for dumping [[battleye]] **runtime shellcode modules** streamed from the BattlEye server and executed inside the protected game process. Intercepts and saves scanning modules **before they execute**, capturing shellcode payloads and their decryption keys for offline analysis of BE’s dynamic scanning-module architecture and detection signatures. README category: BEClient2.dll Dumper. (source: wiki/sources/descriptions/lguilhermee__Battleye-Shellcode-Dumper.md)

Complements [[be-shellcode]] (offline reimplementation/disasm of known BE detection lanes) and [[battleye-region-walking]] (VirtualQuery region-walk heuristics).

## Links

- Repo: https://github.com/lguilhermee/Battleye-Shellcode-Dumper

## Related

[[battleye]] · [[be-shellcode]] · [[battleye-region-walking]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
