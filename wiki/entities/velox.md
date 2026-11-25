---
title: Velox
kind: entity
topics: [graphics-api, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/ajendras__velox.md
updated: 2026-11-25
confidence: medium
---

# Velox

Velox is a Rust-native compatibility layer that runs unaltered Xbox Series x86-64 game binaries on Windows without full CPU emulation. It loads PE executables and DLLs inside a controlled process, translates console GPU bytecode to DXIL with optional on-disk caching, and exposes swappable GPU, audio, and input backends with Direct3D 12 as the default path. (source: wiki/sources/descriptions/ajendras__velox.md)

A built-in sandbox applies memory isolation, page guards, and API whitelisting by default. An Axum HTTP server reports live FPS and memory metrics and accepts remote commands. Dynamic plugins can hook frame, input, and shader events without patching title binaries, alongside parallel asset streaming with BCPack and Zlib decode. The project targets preservationists, modders, and researchers who want an extensible, testable way to study and extend console title behavior on PC hardware.

## Links

- Repo: https://github.com/ajendras/velox (README: Rust native compatibility layer—unaltered Series PE on Windows; pluggable GPU/audio/input; default sandboxing; HTTP monitoring)

## Related

[[mesia-unified]] · [[xenia]] · [[nxbox]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]