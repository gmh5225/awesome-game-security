---
title: Triton
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JonathanSalwan__Triton.md
updated: 2026-08-24
confidence: medium
---

# Triton

Dynamic binary analysis (DBA) library for building program analysis tools, automating reverse engineering, verifying software, and emulating code. Provides dynamic symbolic execution, dynamic taint analysis, expression synthesis, and SMT simplification with ISA semantics for x86, x86-64, ARM32, AArch64, and RISC-V 32/64. Can lift code to LLVM and Z3 (and back) and interfaces with SMT solvers including Z3 and Bitwuzla. Implemented primarily in C++ with Python bindings for scriptable symbolic and taint-based binary analysis workflows. (source: wiki/sources/descriptions/JonathanSalwan__Triton.md)

Upstream DBA engine behind in-IDA [[ponce]], Binary Ninja [[triton-bn]], and many VMProtect/Themida deobfuscation workflows ([[titan]], [[novmpy]], [[vmprotect-devirtualization]], [[rumba]]); complements radare2-backed [[radius2]] and angr-based [[angrop]] rather than replacing disassembler plugins.

## Links

- Repo: https://github.com/JonathanSalwan/Triton

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ponce]] · [[triton-bn]] · [[titan]] · [[novmpy]] · [[vmprotect-devirtualization]] · [[radius2]] · [[angrop]]
