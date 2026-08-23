---
title: VMPacker
kind: entity
topics: [reverse-engineering, anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/LeoChen-CoreMind__VMPacker.md
  - https://github.com/LeoChen-CoreMind/VMPacker
updated: 2026-08-23
confidence: medium
---

# VMPacker

**ARM64 ELF virtual machine code protection system** (LeoChen-CoreMind) written in Go. Translates native ARM64 instructions into custom VM bytecode executed by an embedded interpreter, with layered protections: indirect dispatch, chained encryption, CRC integrity checks, and function-splitting obfuscation. The repository includes demo programs for individual instruction virtualization and protection-strategy evaluation. (source: wiki/sources/descriptions/LeoChen-CoreMind__VMPacker.md)

Primarily useful for **binary protection researchers and reverse engineers** studying VM-based obfuscation schemes on ARM64 ELF targets (Android/Linux native `.so` modules). Complements x86-64 open virtualizers such as [[binary-shield]], [[covirt]], and [[guardian-rs]], and ARM64 branch-obfuscation tooling such as [[deobfbr]].

## Links

- Repo: https://github.com/LeoChen-CoreMind/VMPacker

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[binary-shield]] · [[bytecodevm]] · [[covirt]] · [[vmp-devirtualization-lab]] · [[vmattack]] · [[deobfbr]] · [[elf-got-patcher]]
