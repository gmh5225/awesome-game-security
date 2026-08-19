---
title: Enigma
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/adam-040__Enigma.md
updated: 2026-08-19
confidence: medium
---

# Enigma

**Standalone native decompiler engine** extracted from Ghidra's **SLEIGH/Pcode** framework and reimplemented in **C++**. Integrates **BFD** for multi-architecture binary loading and analysis without requiring **Java** or a full Ghidra installation. Reimplements Ghidra's analytical core (**SoftwareModeling + Utility**) with **SLEIGH** and native **Capstone** pipelines—designed to be **embeddable** in automation and **AI/agent** RE workflows. (source: wiki/sources/descriptions/adam-040__Enigma.md)

Complements JVM-based [[ghidra]] and headless decompiler peers ([[ghiradec]], [[pyre]], [[viv-ghidra-decompiler]]) by offering a native, Ghidra-compatible lifting/decompilation stack for pipelines that cannot depend on a Ghidra desktop install.

## Links

- Repo: https://github.com/adam-040/Enigma

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghiradec]] · [[pyre]] · [[viv-ghidra-decompiler]] · [[ghidra-headless-mcp]] · [[kong]]
