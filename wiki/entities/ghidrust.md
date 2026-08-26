---
title: GhidRust
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/DMaroo__GhidRust.md
updated: 2026-08-26
confidence: medium
---

# GhidRust

**GhidRust** is a **Ghidra extension** for analyzing **Rust binaries** and improving reverse-engineering workflows on stripped executables. Implemented mainly in **Java** as a standard Ghidra extension with supporting data assets, it adds **Rust binary detection heuristics**, integrates **Function ID** matching for common Rust standard-library functions, and experiments with translating Ghidra's C-like decompiler output toward **Rust-style pseudocode**. Useful for reverse engineers working on Rust malware, game clients, and anti-cheat modules where symbols are missing; the repository is in a **paused maintenance** state. (source: wiki/sources/descriptions/DMaroo__GhidRust.md)

Complements IDA-side Rust helpers such as [[ida-rust-helper]], [[ida-rust-demangler]], and [[ida-rust-cargo]], and agent-oriented Ghidra decompilers such as [[kuna]] when the goal is native Rust stdlib recovery inside Ghidra rather than full engine replacement.

## Links

- Repo: https://github.com/DMaroo/GhidRust

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[kuna]] · [[ghidra-nativeaot]] · [[ida-rust-helper]] · [[oxidizer]] · [[rust-obfuscator]]
