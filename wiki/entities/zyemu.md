---
title: zyemu
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ZehMatt__zyemu.md
updated: 2026-08-19
confidence: medium
---

# zyemu

Work-in-progress **x86-64 user-mode emulator** written in modern C++ that uses **JIT-generated handlers** instead of a purely interpreted execution model. Relies on **Zydis** for instruction decoding and encoding. Core components include code generation, code caching, CPU logic, and memory management, plus playground and test targets. Intended for low-level emulation, binary analysis, and advanced reverse-engineering research. (source: wiki/sources/descriptions/ZehMatt__zyemu.md)

Sits in the **Windows User Space Emulator** lane alongside Unicorn-based peers such as [[emulator]] and [[dumpulator]], WHP-hosted [[winvisor]], and research sandboxes such as [[kubera]]. Cross-arch Linux/RISC-V counterpart: [[felix86]]. Complements decode-first learning baselines such as [[dynre-x86]] and runtime codegen libraries such as [[chasm]] on the instruction-decode → JIT pipeline axis.

## Links

- Repo: https://github.com/ZehMatt/zyemu (README tag: x86-64 user mode emulation using Zydis)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[emulator]] · [[felix86]] · [[dynre-x86]] · [[chasm]] · [[kubera]] · [[winvisor]]
