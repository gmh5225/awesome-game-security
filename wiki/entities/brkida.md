---
title: brkida
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/android1337__brkida.md
updated: 2026-08-18
confidence: medium
---

# brkida

Header-only C++ macro framework that intentionally breaks Hex-Rays decompilation. Generates compile-time stubs and crafted stack-access patterns so protected functions fail to decompile cleanly in IDA's Hex-Rays plugin. Targets MSVC on x64 and exposes a simple `BRKIDA` macro with example usage. Aimed at software protection and game anti-tamper experiments where raising reverse-engineering cost on critical functions matters (Anti Cheat → anti-analysis / decompiler evasion). (source: wiki/sources/descriptions/android1337__brkida.md)

Complements compile-time obfuscation from the same author such as [[crystr]] and [[crycall]]; distinct from decompiler-side plugins like [[d810-ng]] or [[obpo-plugin]] that recover obfuscated pseudocode. Analysts counter with disassembly-first workflows, microcode plugins such as [[genmc]], or emulation when decompilation fails.

## Links

- Repo: https://github.com/android1337/brkida

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[crystr]] · [[crycall]] · [[d810-ng]] · [[genmc]] · [[obpo-plugin]]
