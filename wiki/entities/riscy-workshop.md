---
title: RiscyWorkshop
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/mrexodia__RiscyWorkshop.md
updated: 2026-07-29
confidence: medium
---

# RiscyWorkshop

**Payload Obfuscation for Red Teams** workshop materials from mrexodia. Teaches RISC-V–based payload hiding via a custom VM interpreter (**riscvm**), a C-to-RISC-V cross-compiler toolchain (**llvm-mingw**), and an obfuscator that applies liveness analysis plus instruction mutation to RISC-V binaries. Exercises cover VM basics, shellcode generation, host API interaction, transpilation, and anti-analysis hardening. (source: wiki/sources/descriptions/mrexodia__RiscyWorkshop.md)

Useful as an educational VM-obfuscation / cross-architecture payload pipeline reference alongside x64 virtualizers such as [[nocturne]] and PE mutators such as [[alcatraz]] — distinct from Android OTA tooling like [[payload-dumper]].

## Links

- Repo: https://github.com/mrexodia/RiscyWorkshop

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[nocturne]] · [[alcatraz]] · [[scfw]] · [[the-poor-mans-obfuscator]] · [[dumpulator]] · [[titanhide]] · [[ida-pro-mcp]]
