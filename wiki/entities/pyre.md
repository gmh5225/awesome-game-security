---
title: pyre
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ant4g0nist__pyre.md
updated: 2026-08-18
confidence: medium
---

# pyre

**WebAssembly-compiled Ghidra decompiler** that runs entirely in the browser. Compiles the **SLEIGH** framework to WASM and decompiles binaries for **multiple architectures** with **no server-side processing**—pseudocode generation stays client-side. Useful for quick Ghidra-quality decompilation when a full Ghidra install is unavailable, or for sharing decompilation workflows in a portable web UI. Listed as *Ghidra decompiler in your browser* in the curated list. (source: wiki/sources/descriptions/ant4g0nist__pyre.md)

Complements headless Ghidra decompiler peers such as [[ghiradec]] and [[viv-ghidra-decompiler]] by offering browser-native access to Ghidra's SLEIGH-based lifting. Differs from the full [[ghidra]] framework tree, which requires a JVM desktop install.

## Links

- Repo: https://github.com/ant4g0nist/pyre

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghiradec]] · [[viv-ghidra-decompiler]] · [[retdec]]
