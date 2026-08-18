---
title: gexec
kind: entity
topics: [windows-kernel, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/zer0condition__gexec.md
updated: 2026-08-18
confidence: medium
---

# gexec

Register-machine **bytecode interpreter** for embedding in Windows kernel drivers, implemented in C without a JIT. Ships with a text assembler (**gasm**), an x86-64 PE lifter (**gvmlift**) built on Zydis, and loader, verifier, and execution APIs integrated through a host function table. Bytecode uses fixed 16-byte instructions with roughly 180 opcodes covering integer and floating-point arithmetic, memory operations, structured exception handling, atomics, and host callbacks. Host callbacks expose kernel memory, MSR, and physical access to guest bytecode. Aimed at kernel-mode security research and anti-cheat development where updatable, portable logic must run inside a driver instead of as native compiled code. (source: wiki/sources/descriptions/zer0condition__gexec.md)

## Links

- Repo: https://github.com/zer0condition/gexec

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[pawnio]] · [[ntlua]] · [[ntmemory]]
