---
title: Cerberus
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__cerberus.md
updated: 2026-08-09
confidence: medium
---

# Cerberus

**Win32 VM-based code protection engine** built around a custom x86 virtual machine called **ChaosVm**. Native x86 instructions are translated into proprietary bytecode and executed through a software CPU emulator, providing code virtualization for PE binaries. The C codebase includes a full x86 disassembler and assembler, a binary analyzer for procedure and instruction flow recovery, PE file parsing and patching, CRC32 integrity checking, and a Qt-based GUI frontend for applying protection. Aimed at software protection researchers studying VM-based obfuscation engines and code virtualization techniques under Anti Cheat → Obfuscation Engine / `[VM]`. (source: wiki/sources/descriptions/gmh5225__cerberus.md)

Useful as an open Win32 x86 virtualization reference alongside bin2bin virtualizers such as [[nocturne]] and [[phantasm-x86-virtualizer]], and commercial-style protectors such as [[vxlang-page]] — distinct from VMProtect/Themida handler-recovery tooling like [[novmpy]].

## Links

- Repo: https://github.com/gmh5225/cerberus

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[phantasm-x86-virtualizer]] · [[nocturne]] · [[vxlang-page]] · [[wprotect]] · [[novmpy]]
