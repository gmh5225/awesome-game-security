---
title: rax
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/HexRaysSA__rax.md
updated: 2026-08-24
confidence: medium
---

# rax

Hex-Rays' Rust-based **self-checking CPU emulator** for multi-architecture binary analysis, fuzzing, and IDA Pro integration. Targets x86, x64, ARM32, AArch64, Hexagon, and RISC-V with **SMIR JIT** compilation. Validates behavior through instruction-level diffs against KVM/QEMU oracles, boots Linux, supports SDE trace workflows, and exposes a **GDB stub for IDA**. (source: wiki/sources/descriptions/HexRaysSA__rax.md)

Official Hex-Rays tooling—distinct from plugin-level Unicorn harnesses such as [[unxorer]] or [[ripr]], and from research JIT emulators such as [[zyemu]]. Complements Hex-Rays decompiler/microcode plugins ([[hex-rays-deob]], [[hrtng]]) when analysts need faithful multi-arch execution rather than static lift alone.

## Links

- Repo: https://github.com/HexRaysSA/rax

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unxorer]] · [[ripr]] · [[emulator]] · [[unicorn-pe]] · [[zyemu]] · [[hex-rays-deob]] · [[hrtng]] · [[qemu-nyx]]
