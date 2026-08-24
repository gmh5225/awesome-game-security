---
title: Ouroboros
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Hexorg__Ouroboros.md
updated: 2026-08-24
confidence: medium
---

# Ouroboros

**Symbolic-execution decompiler** written in **Rust** for recovering high-level program structure from binaries. Design emphasizes **constraint tracking**, **expression rewriting**, and **structured control-flow reconstruction** beyond classic SSA-only lifting approaches. Includes processor specification assets and a modern frontend stack for interactive analysis. Targets reverse-engineering researchers and developers exploring advanced decompilation techniques. (source: wiki/sources/descriptions/Hexorg__Ouroboros.md)

Complements Rust-native peers [[kuna]] and [[oxidizer]] by focusing on symbolic-execution-driven structure recovery rather than Ghidra porting or angr acceleration.

## Links

- Repo: https://github.com/Hexorg/Ouroboros

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[kuna]] · [[oxidizer]] · [[neverd]] · [[retdec]] · [[enigma]] · [[decbench]]
