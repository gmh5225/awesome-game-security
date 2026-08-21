---
title: dll-ollvm
kind: entity
topics: [reverse-engineering, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/R7flex__dll-ollvm.md
updated: 2026-08-21
confidence: medium
---

# dll-ollvm

**LLVMObfuscationx** is an **LLVM 18 New Pass Manager** plugin (C++) that obfuscates Windows binaries at the **intermediate representation** stage before code generation. It integrates into a **clang / opt / llc** toolchain and applies **instruction substitution**, **bogus control flow**, **control-flow flattening**, and **size-trimming** passes that strip **global constructors** for **manual-map** compatibility. The preset **tess-obf** pipeline runs these transforms in sequence; **per-function annotation markers** can skip, protect, or force obfuscation on selected code. Designed and tested for **manually mapped DLLs** in injection scenarios where CRT startup and global initializers are not run—hardening cheat payloads against anti-cheat **allocation and table-pattern scans**. (source: wiki/sources/descriptions/R7flex__dll-ollvm.md)

Offensive obfuscation counterpart to CFF recovery tools such as [[ollvm-unflattener]], [[idadeflat]], and [[hex-rays-deob]].

## Links

- Repo: https://github.com/R7flex/dll-ollvm

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[control-flow-flattening]] · [[the-poor-mans-obfuscator]] · [[kagura]] · [[ollvm-unflattener]] · [[manual-mapping-dll-injector]]
