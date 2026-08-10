---
title: VMAttack
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__VMAttack.md
updated: 2026-08-10
confidence: medium
---

# VMAttack

**IDA Pro plugin** (Python) for analyzing and attacking **VM-based code obfuscation**. Identifies virtual machine dispatcher loops, extracts virtual opcode handler tables, traces virtual instruction execution, and assists in devirtualizing VM-protected code. Provides automated analysis of custom VM architectures in protected binaries—aimed at reverse engineers deobfuscating VM-protected malware and commercially protected software. (source: wiki/sources/descriptions/gmh5225__VMAttack.md)

Companion surface to protector-specific devirt tooling ([[tde]], [[novmpy]], [[rumba]], [[vmdragonslayer]]): generic custom-VM dispatcher/handler recovery inside IDA rather than a single-protector symbolic-exec or unpack path.

## Links

- Repo: https://github.com/gmh5225/VMAttack

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[tde]] · [[vmdragonslayer]] · [[novmpy]] · [[rumba]] · [[vmprotect]] · [[cerberus]]
