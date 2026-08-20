---
title: CodeCleaner
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Steesha__CodeCleaner.md
updated: 2026-08-20
confidence: medium
---

# CodeCleaner

[[x64dbg]] plugin (C++) that **cleans and simplifies disassembled machine code** in the debugger. Uses Capstone for instruction analysis and AsmJit for transformation-oriented logic. Strips junk patterns such as redundant NOPs and no-op register moves so traces and disassembly views are easier to read. Primary use case: reverse engineering **packed or obfuscated binaries** in game-security research—README lane targets **Themida mutation assembly** cleanup. (source: wiki/sources/descriptions/Steesha__CodeCleaner.md)

Complements Cheat → Fix Themida work such as [[themida-unmutate]] (static mutation recovery), [[themidie]] (live anti-analysis neutralization during attach), and [[themida-research]] (VM internals)—**in-debugger disassembly simplification** for mutation junk rather than unpack, devirtualization, or anti-debug bypass.

## Links

- Repo: https://github.com/Steesha/CodeCleaner

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[x64dbg]] · [[themida-unmutate]] · [[themidie]] · [[themida-research]] · [[unlicense]] · [[magicmida-rs]]
