---
title: x64-virtualizer-rs
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/cursey__x64-virtualizer-rs.md
updated: 2026-08-16
confidence: medium
---

# x64-virtualizer-rs

**Toy x86-64 virtualizing obfuscator** written in Rust. Uses the **iced-x86** crate to disassemble raw x86-64 byte arrays, translates native instructions into a **custom stack-machine bytecode** (Const, Load, Store, Add, Mul, …), and **JIT-assembles vmenter and vmexit bridge routines** at runtime. The `Machine` struct maintains virtual registers and a stack pointer for bytecode execution. Aimed at security researchers studying **VM-based code obfuscation internals** and exploring Rust for binary-transformation tooling—not a production protector. (source: wiki/sources/descriptions/cursey__x64-virtualizer-rs.md)

Useful as an educational Rust stack-VM virtualization reference alongside [[guardian-rs]] and [[covirt]], and as a minimal lift/JIT pipeline contrast to commercial protectors such as [[vxlang-page]].

## Links

- Repo: https://github.com/cursey/x64-virtualizer-rs

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[guardian-rs]] · [[covirt]] · [[phantasm-x86-virtualizer]] · [[rust-obfuscator]] · [[novmpy]]
