---
title: LLVM-MSVC
kind: entity
topics: [reverse-engineering, windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/aftermathlabs__llvm-msvc.md
updated: 2026-10-28
confidence: medium
---

# LLVM-MSVC

**llvm-msvc** (aftermathlabs) is an **LLVM monorepo fork** packaging **Clang**, **compiler-rt**, and **LLVM BOLT** with CMake-based builds typical of upstream llvm-project. **Clang** adds **Microsoft Visual C++ compatibility**: an MSVC-oriented driver, cross-Windows toolchain support, and MSVC-specific varargs handling so Windows-native code can be built with an LLVM compiler aligned to the MSVC ecosystem. **BOLT** supplies post-link binary rewriting, profiling, and optimization passes for **x86**, **AArch64**, and **RISC-V** executables. README positioning also highlights **Windows/Android kernel driver toolchains** and hooks for **custom obfuscation passes**—useful when studying or building hardened native modules without relying solely on the proprietary Microsoft toolchain. (source: wiki/sources/descriptions/aftermathlabs__llvm-msvc.md)

## Links

- Repo: https://github.com/aftermathlabs/llvm-msvc

## Related

[[overviews/reverse-engineering]] · [[overviews/windows-kernel]] · [[oboro]] · [[dll-ollvm]] · [[amice]] · [[limba]]
