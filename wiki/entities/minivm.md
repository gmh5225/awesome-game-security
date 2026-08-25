---
title: minivm
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/FastVM__minivm.md
updated: 2026-08-25
confidence: medium
---

# minivm

Small **optimizing virtual machine and runtime** with **JIT compilation** (FastVM). Implemented in **C11**, integrates **Cuik TB** for native code generation, and ships **Lua-based** test and benchmark programs. Built with **GNU Make** and targets desktop platforms plus **WebAssembly**. Primarily aimed at **VM, compiler, and runtime performance experimentation** rather than production binary protection. (source: wiki/sources/descriptions/FastVM__minivm.md)

Useful as a minimal **JIT VM runtime reference** when studying custom bytecode interpreters, optimizing compilers, and codegen pipelines — complementary to educational obfuscation VMs such as [[bytecodevm]], [[q3vm]], and [[x64-virtualizer-rs]], and to commercial protector VMs such as [[vmprotect]].

## Links

- Repo: https://github.com/FastVM/minivm

## Related

[[q3vm]] · [[bytecodevm]] · [[x64-virtualizer-rs]] · [[covirt]] · [[vmp-devirtualization-lab]] · [[overviews/reverse-engineering]]
