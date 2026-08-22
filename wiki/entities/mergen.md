---
title: Mergen
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/NaC-L__Mergen.md
updated: 2026-08-22
confidence: medium
---

# Mergen

**Binary lifting framework** that converts **assembly behavior into LLVM IR** for deeper static and symbolic analysis. Implemented primarily in **C/C++** with LLVM-oriented workflows and disassembly support components, it targets **symbolic execution**, **control-flow recovery**, **deobfuscation**, and **devirtualization** of protected binaries. Intended for reverse engineers and software security researchers, including analysts studying **protected game binaries**. (source: wiki/sources/descriptions/NaC-L__Mergen.md)

Complements instruction-level lifters such as [[neverd]] and [[ida2llvm]] by emphasizing LLVM IR as the analysis hub for obfuscated or virtualized code paths. Pairs with VM-oriented devirtualizers such as [[titan]] when lifting virtualized handlers back to analyzable IR, and with CFF recovery tooling in the [[control-flow-flattening]] lane.

## Links

- Repo: https://github.com/NaC-L/Mergen

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[neverd]] · [[ida2llvm]] · [[retdec]] · [[titan]] · [[control-flow-flattening]] · [[static-analyzer-factory]]
