---
title: inline-syscall
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/JustasMasiulis__inline_syscall.md
  - wiki/sources/descriptions/gmh5225__inline-syscall.md
updated: 2026-08-24
confidence: medium
---

# inline-syscall

Direct Windows **syscall invocation** libraries for calling native routines without going through hooked `ntdll` stubs or normal import-table paths. Used in low-level systems programming, anti-hooking experiments, and game-security research (Anti Cheat → Compile Time / Windows Ring3).

## JustasMasiulis/inline_syscall

Header-only C++ library for generating **direct system calls inline**. Provides initialization and macro-based wrappers so callers invoke native routines without normal import-table usage. Focused on compact, inlinable machine code and low overhead on **x64 Windows** targets (Clang-oriented). (source: wiki/sources/descriptions/JustasMasiulis__inline_syscall.md)

Canonical Clang/x64 inline-syscall reference in the README lane. Complements compile-time string hiding via [[xorstr]], runtime lazy import via [[lazy-importer]], and sibling direct-call helpers such as [[syscalls-cpp]] and [[doom-syscalls]]. Defensive analysts should pair inline `syscall` stubs in `.text` with origin checks such as [[syscall-detect]].

- Repo: https://github.com/JustasMasiulis/inline_syscall

## gmh5225/inline-syscall

Simple C++ direct syscall wrapper with compatibility for **x86 and x64** user-mode programs. Lightweight invocation stubs rather than full SSN table tooling. (source: wiki/sources/descriptions/gmh5225__inline-syscall.md)

- Repo: https://github.com/gmh5225/inline-syscall

## Related

[[syscalls-cpp]] · [[doom-syscalls]] · [[higu-ntcall]] · [[ntsleuth]] · [[syscall-detect]] · [[lazy-importer]] · [[xorstr]] · [[instrumentation-callback-syscall-logger]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
