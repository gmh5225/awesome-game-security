---
title: Ghidra Decompiler Plugins
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/thixotropist__ghidra_decompiler_plugins.md
updated: 2026-08-09
confidence: medium
---

# Ghidra Decompiler Plugins

Research workspace for **runtime-loadable plugins** that extend Ghidra's decompiler without enduring upstream Ghidra source changes. Patches the decompiler executable to add a plugin manager, then builds experimental shared libraries with Bazel that register custom Rules, Actions, and builtin functions through the decompiler API. The proof-of-concept RISC-V vector plugin recognizes vectorized instruction sequences and lifts them into higher-level calls such as `vector_memcpy`, `vector_memset`, and `vector_strlen`, reducing clutter and improving decompiled-output readability. Development is primarily C++ with Python tooling; uses the decompiler datatest framework for fast compile-test cycles independent of the Ghidra GUI. Aimed at Ghidra users and reverse engineers analyzing RISC-V binaries, embedded firmware, and other programs that use ISA extensions where clearer decompiler output accelerates security and binary analysis work. (source: wiki/sources/descriptions/thixotropist__ghidra_decompiler_plugins.md)

Complements the full [[ghidra]] framework tree and Ghidra automation peers ([[ghidra-bridge]], [[ghidra-headless-mcp]], [[ghidrassist]]) by extending decompiler semantics at the p-code/rule layer rather than the Java GUI scripting surface.

## Links

- Repo: https://github.com/thixotropist/ghidra_decompiler_plugins

## Related

[[overviews/reverse-engineering]] · [[ghidra]] · [[ghidra-bridge]] · [[ghidrametrics]] · [[embedded-hacking]] · [[mytechnotalent-reverse-engineering]]
