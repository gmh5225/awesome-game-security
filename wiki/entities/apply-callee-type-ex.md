---
title: ApplyCalleeTypeEx
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/Dump-GUY__ApplyCalleeTypeEx.md
updated: 2026-08-26
confidence: medium
---

# ApplyCalleeTypeEx

IDA Pro plugin (Dump-GUY; cheat / IDA Plugins) that extends Hex-Rays' built-in **Apply callee type** workflow. Python IDAPython script applies function prototypes to **indirect CALL** sites so decompiler output and disassembly show correct argument types and calling conventions. Ships with test binaries and an `ida-plugin.json` manifest for IDA 8.x–9.3+. Targets reverse engineers who need stronger **type propagation** and callee resolution on complex binaries—common when triaging obfuscated game clients or anti-cheat modules where vtables, function pointers, and indirect calls hide prototypes. (source: wiki/sources/descriptions/Dump-GUY__ApplyCalleeTypeEx.md)

Call-site prototype application—not bulk Windows SDK type import ([[ida-phnt-types]]) or pseudocode annotation plugins such as [[ntrays]].

## Links

- Repo: https://github.com/Dump-GUY/ApplyCalleeTypeEx

## Related

[[overviews/reverse-engineering]] · [[ida-phnt-types]] · [[ntrays]] · [[list-of-ida-plugins]]
