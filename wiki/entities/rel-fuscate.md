---
title: rel-fuscate
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/caprinux__rel-fuscate.md
updated: 2026-08-17
confidence: medium
---

# rel-fuscate

Python-based toolchain that **obfuscates ELF binaries** by patching **JMPREL** relocation entries: it manipulates `jmprel_entry->r_offset` so imported function names resolve to incorrect GOT slots in static disassemblers and decompilers, while the program still runs correctly at runtime. Includes scripts for import extraction, obfuscation-header generation, and ELF patching with **partial RELRO** lazy binding. Mainly useful for binary-protection researchers studying ELF relocation-based obfuscation and anti-disassembly. (source: wiki/sources/descriptions/caprinux__rel-fuscate.md)

Useful as an **ELF relocation / GOT misdirection** reference alongside PE reloc research such as [[relocbonus]] and import-table obfuscators such as [[call-obfuscator]].

## Links

- Repo: https://github.com/caprinux/rel-fuscate

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[relocbonus]] · [[call-obfuscator]] · [[covirt]] · [[the-poor-mans-obfuscator]] · [[embuche]]
