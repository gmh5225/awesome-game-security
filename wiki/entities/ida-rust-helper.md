---
title: IDARustHelper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/JANlittle__IDARustHelper.md
updated: 2026-08-24
confidence: medium
---

# IDARustHelper

Python IDA Pro plugin that improves analysis of Rust binaries. Demangles Rust symbols, normalizes names for IDA compatibility, injects common Rust type definitions, and provides architecture-aware string recovery helpers for x86, ARM, and RISC-V targets. Aimed at reverse engineers who need faster navigation of Rust malware, game clients, or system binaries. (source: wiki/sources/descriptions/JANlittle__IDARustHelper.md)

Broader than symbol-only tools such as [[ida-rust-demangler]]—adds type context and cross-arch string recovery alongside demangling. Complements [[ida-rust-cargo]] for dependency hints during Rust client or anti-cheat RE.

## Links

- Repo: https://github.com/JANlittle/IDARustHelper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ida-rust-demangler]] · [[ida-rust-cargo]] · [[happyida]] · [[demumble]]
