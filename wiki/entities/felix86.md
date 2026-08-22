---
title: felix86
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/OFFTKP__felix86.md
updated: 2026-08-22
confidence: medium
---

# felix86

Linux **userspace emulator** that runs **x86 and x86-64** programs on **RISC-V** processors. Uses a **JIT recompiler**, **vectorized SSE translation**, and multiple RISC-V extensions for compatibility and performance. Implemented mainly in modern C++ with external libraries for decoding, formatting, and testing. Targets emulator developers and low-level systems researchers exploring cross-architecture execution. (source: wiki/sources/descriptions/OFFTKP__felix86.md)

Sits in the **`Linux Emulator`** lane — the inverse direction of Android `Windows Emulator` stacks such as [[winlator]] (x86→ARM) and complements JIT user-mode emulators such as [[zyemu]] on the binary-translation / cross-arch execution axis.

## Links

- Repo: https://github.com/OFFTKP/felix86 (README tag: Run x86-64 programs on RISC-V Linux)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[zyemu]] · [[winlator]] · [[dynre-x86]] · [[levo]]
