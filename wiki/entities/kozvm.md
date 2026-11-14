---
title: KozVM
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ivanpotatoes__KozVM.md
updated: 2026-11-14
confidence: medium
---

# KozVM

Open-source **x64dbg plugin** that counters **VMProtect-style anti-virtual-machine** checks on **64-bit** targets without a kernel driver. Built in C++ with the x64dbg plugin SDK and CMake; ships CPUID-focused backends for VMProtect **3.3.1**, **3.4.0**, and **3.5.0** that locate handlers at runtime in executable sections via pattern matching and memory execute breakpoints. Settings GUI, INI-based configuration beside the DLL, and debugger commands arm the backend, report status, and apply settings to a paused session—for reverse engineers debugging VMProtect-protected binaries inside x64dbg while mitigating CPUID-based VM detection. (source: wiki/sources/descriptions/ivanpotatoes__KozVM.md)

Companion to [[kozdbg]] (anti-debug) on the same author’s VMProtect-focused x64dbg plugin pair; pairs unpack/lift tooling such as [[codex-vmprotect-unpack-skill]], [[vmprotect-unpacker]], and [[vmplift]].

## Links

- Repo: https://github.com/ivanpotatoes/KozVM (README tag: Debugging / RE Tools)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[kozdbg]] · [[vmprotect-unpacker]] · [[themidie]] · [[scyllahide-for-ida9.0rc]]