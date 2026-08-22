---
title: NeverC
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/NeverSight__NeverC.md
updated: 2026-08-22
confidence: medium
---

# NeverC

**Security-oriented C23 compiler and toolchain** from NeverSight built on a **customized LLVM backend** for producing hardened native binaries on **Windows**, **Linux**, and **Android**. Written primarily in **C and C++**, it ships compile-time protections such as **encrypted string builtins**, **string hashing**, and **mimalloc**, together with a **DynCode** pipeline for position-independent runtime code generation including **kernel-mode** use. The project exposes an extensible **plugin API** across preprocessing, AST and semantic analysis, IR and MIR passes, LTO linking, and custom calling conventions, with examples covering user-mode executables and DLLs, Windows kernel drivers, and Android kernel modules. It targets game security researchers, reverse engineers, and developers building low-level tools where obfuscation, evasion, and cross-platform native code generation are required. (source: wiki/sources/descriptions/NeverSight__NeverC.md)

Complements sibling [[neverd]] in the NeverSight AI-era compiler/decoder pair: NeverC hardens source→binary generation (pure C23, integrated linker, PE/ELF/Mach-O output, 130+ compiler-phase plugins) while NeverD lifts existing machine code back to LLVM IR or structured C. Compile-time string protection overlaps [[static-string-obfuscation]], [[obfuscate]], and [[crystr]] lanes but as a full toolchain rather than header-only crypters.

## Links

- Repo: https://github.com/NeverSight/NeverC

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[neverd]] · [[the-poor-mans-obfuscator]] · [[kagura]] · [[dll-ollvm]] · [[static-string-obfuscation]] · [[dynamizer]] · [[polymorphic-engine]]
