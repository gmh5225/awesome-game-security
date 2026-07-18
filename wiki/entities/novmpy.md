---
title: NoVmpy
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/wallds__NoVmpy.md
updated: 2026-07-18
confidence: medium
---

# NoVmpy

Python tool for deobfuscating VMProtect-virtualized code via symbolic execution. Traces VMProtect VM handler chains, symbolically executes each handler to extract semantics, and reconstructs the original instruction sequence from virtualized bytecode. Uses Triton (or similar) for analysis. Aimed at reverse engineers and malware analysts recovering code from VMProtect-protected binaries. (source: wiki/sources/descriptions/wallds__NoVmpy.md)

Companion surface to other Cheat → Fix VMP research (e.g. [[vmdevirt-vtil]]): symbolic-exec handler recovery rather than a VTIL compile/display demo.

## Links

- Repo: https://github.com/wallds/NoVmpy

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmdevirt-vtil]] · [[idadeflat]] · [[deobf]]
