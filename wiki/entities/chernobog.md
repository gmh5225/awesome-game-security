---
title: chernobog
kind: entity
topics: [reverse-engineering]
sources:
  - wiki/sources/descriptions/19h__chernobog.md
updated: 2026-09-05
confidence: medium
---

# chernobog

**chernobog** (19h) is a **Hex-Rays decompiler plugin** for automatically deobfuscating binaries protected with the **Hikari LLVM obfuscator** in **IDA Pro**. Implemented mainly in C++, it applies symbolic reasoning with **Z3** plus extensive **MBA simplification** rules to restore control flow from flattening and bogus branches, resolve indirect control transfers, and recover encrypted data constructs. Primary use case is reverse engineering heavily obfuscated binaries in malware and game security research. (source: wiki/sources/descriptions/19h__chernobog.md)

Complements other Hex-Rays deobfuscation plugins such as [[d810]], [[hex-rays-deob]], and [[goomba]], and LLVM-oriented analysis tooling from the same author such as [[eac-analysis]].

## Links

- Repo: https://github.com/19h/chernobog

## Related

[[mixed-boolean-arithmetic]] · [[control-flow-flattening]] · [[goomba]] · [[d810]] · [[hex-rays-deob]] · [[eac-analysis]] · [[overviews/reverse-engineering]]
