---
title: amice
kind: entity
topics: [reverse-engineering, anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/fuqiuluo__amice.md
updated: 2026-09-09
confidence: medium
---

# amice

**Amice** is a **Rust** LLVM **New Pass Manager** plugin (fuqiuluo) that loads into the compiler via `clang -fpass-plugin` and applies **compile-time obfuscation** to LLVM IR from **C/C++**, **Rust**, and other LLVM-based languages. Built with **llvm-plugin-rs** and **inkwell**, it supports **LLVM 11 through 22** and includes **Android NDK** integration for mobile native builds. (source: wiki/sources/descriptions/fuqiuluo__amice.md)

## Protection transforms

Broad IR-stage hardening aimed at reverse engineering, tampering, and static analysis resistance in game security and software-protection contexts:

- String encryption
- [[control-flow-flattening]] and bogus control flow
- [[mixed-boolean-arithmetic]] rewriting
- Indirect calls and branches
- Basic-block splitting and shuffling
- Instruction-level virtual machine protection (VMP)

## Links

- Repo: https://github.com/fuqiuluo/amice

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[control-flow-flattening]] · [[mixed-boolean-arithmetic]] · [[dll-ollvm]] · [[the-poor-mans-obfuscator]] · [[kagura]] · [[dprotect]]
