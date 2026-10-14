---
title: Hermit
kind: entity
topics: [reverse-engineering, mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/xV4L3x__hermit.md
  - wiki/sources/README-categories.md
updated: 2026-10-14
confidence: high
---

# Hermit

Interactive **Hermes bytecode (HBC)** toolkit for React Native Android/iOS bundles: parse, disassemble, control-flow analysis, deterministic decompilation to JavaScript, and **structural patching** with full re-serialization so edited bundles remain loadable by the Hermes VM. C++ core plus Python GDB-style REPL (bytecode editors, Metro module recovery, xrefs, standalone `hbc` CLI) and pybind11 bindings. Targets HBC versions **94–96** with byte-identical round-trips on unmodified inputs. (source: wiki/sources/descriptions/xV4L3x__hermit.md)

Use when mobile game or hybrid-app RE must recover or patch compiled JS shipped as Hermes rather than plain DEX/IL2CPP alone—complements [[frida]] runtime hooks and [[unity-apk-reverse]] Unity APK lanes.

## Links

- Repo: https://github.com/xV4L3x/hermit

## Related

[[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[luadecompiler]] · [[bytecode-viewer]]
