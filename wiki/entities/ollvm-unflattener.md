---
title: ollvm-unflattener
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cdong1012__ollvm-unflattener.md
updated: 2026-08-17
confidence: medium
---

# ollvm-unflattener

Python tool that **deobfuscates OLLVM control-flow flattening** using the **Miasm** symbolic execution framework. Reconstructs the original CFG by identifying and connecting basic blocks, supports **multi-layer deobfuscation** via BFS-based call following, and emits **deobfuscated binaries** for Windows and Linux on x86 and x64. Unlike purely static deflatteners, it uses Miasm to dynamically recover program flow from the flattened state-variable dispatch structure. Targets reverse engineers and deobfuscation researchers in the cheat / Fix OLLVM lane. (source: wiki/sources/descriptions/cdong1012__ollvm-unflattener.md)

Not an IDA plugin—standalone binary-in / binary-out CFF recovery.

## Links

- Repo: https://github.com/cdong1012/ollvm-unflattener

## Related

[[overviews/reverse-engineering]] · [[control-flow-flattening]] · [[idadeflat]] · [[unflat]] · [[d810-ng]] · [[obpo-plugin]]
