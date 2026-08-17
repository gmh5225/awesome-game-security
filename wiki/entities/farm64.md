---
title: fARM64
kind: entity
topics: [reverse-engineering, mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/binsnake__fARM64.md
updated: 2026-08-17
confidence: medium
---

# fARM64

**fARM64** is a pure-Rust `no_std` **AArch64 disassembler and encoder** with an **iced-x86-shaped API**: a borrowing `Decoder`, value-type `Instruction`, typed `OpKind`/operand accessors, and a token-emitting `Formatter`. It targets a **zero-heap decode path**, covers **SVE/SME/SIMD/FP**, supports **semantic round-trip encode**, and runs in **wasm** and **bare-metal** environments — useful for game-security researchers and reverse engineers building cheat or RE tooling on ARM64. (source: wiki/sources/descriptions/binsnake__fARM64.md)

Library component for decode/encode pipelines — not a debugger, emulator, or game-attached injector. Complements ARM64 debuggers such as [[koidbg]] and per-instruction tracers such as [[qbdi-tracer-android]].

## Links

- Repo: https://github.com/binsnake/fARM64

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[koidbg]] · [[qbdi-tracer-android]] · [[quickasm]]
