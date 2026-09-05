---
title: eac-analysis
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/19h__eac-analysis.md
updated: 2026-09-05
confidence: medium
---

# eac-analysis

Research project analyzing **Easy Anti-Cheat's Linux userland module** (`eac.elf`). The workflow reconstructs EAC's embedded **VM-based obfuscation**: a `dlopen`/trace harness drives handler tracing, **dispatch table** and **VMTAIL** probe recovery, bytecode lift to IR/CFG, handler ISA documentation, static path replay, and **MBA reducer** passes for control-flow deobfuscation. **GDB-assisted dynamic analysis** complements static recovery of protected code paths. (source: wiki/sources/descriptions/19h__eac-analysis.md)

Complements Windows-centric EAC driver RE such as [[eac-reversal]] and decompile dumps by focusing on the **Linux ELF userland** protection layer used on Proton/native Linux clients.

## Links

- Repo: https://github.com/19h/eac-analysis

## Related

[[easy-anti-cheat]] · [[eac-reversal]] · [[eac-extractor-utility]] · [[vmattack]] · [[mixed-boolean-arithmetic]] · [[chernobog]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]]
