---
title: Kuna
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Noelo-Lab__kuna.md
updated: 2026-08-22
confidence: medium
---

# Kuna

**Agent-first binary decompiler** written in **Rust**, originally ported from Ghidra's C++ engine and designed for iterative improvement by **LLM agents**. Includes a full Rust port of Ghidra's decompiler and **SLEIGH** instruction-set compiler, vendored processor specs for many architectures, and a tunable **phase-based pipeline** with runtime-configurable decompilation options. Ships as a **CLI**, **WebAssembly** in-browser decompiler, and **Ghidra plugin** that replaces the stock decompiler core while keeping largely compatible output. Targets reverse engineers, security researchers, and automated analysis workflows—vulnerability research, malware analysis, and game security investigations where agents decompile and analyze binaries autonomously. (source: wiki/sources/descriptions/Noelo-Lab__kuna.md)

Complements native standalone peers [[enigma]] and browser [[pyre]] by offering a Rust-native, agent-tunable Ghidra-compatible stack with first-class CLI/WASM/Ghidra integration for LLM-driven refinement loops.

## Links

- Repo: https://github.com/Noelo-Lab/kuna

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[enigma]] · [[pyre]] · [[ghiradec]] · [[viv-ghidra-decompiler]] · [[kong]] · [[ghidra-mcp]]
