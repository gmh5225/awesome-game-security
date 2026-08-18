---
title: Chasm
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/aqilc__chasm.md
updated: 2026-08-18
confidence: medium
---

# Chasm

**Chasm Runtime Assembler** — high-performance runtime **x86-64 assembler library** written in C. Provides an instruction IR, fast assembly and execution helpers, relative reference linking, rich operand macros, and debugging utilities such as IR stringification. Supports many x86 extensions including **AVX-256** and targets very low-latency **dynamic code generation** workloads: JIT compilers, emulators, runtime optimization, and systems research. (source: wiki/sources/descriptions/aqilc__chasm.md)

A library building block—not a debugger plugin or standalone GUI like [[quickasm]]. Complements other runtime codegen stacks such as AsmJit-based tooling ([[shoggoth]], [[alcatraz]], [[vmtrace]]) and encoder/disassembler libraries such as [[farm64]].

## Links

- Repo: https://github.com/aqilc/chasm

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[quickasm]] · [[farm64]] · [[shoggoth]] · [[multiline-ultimate-assembler]]
