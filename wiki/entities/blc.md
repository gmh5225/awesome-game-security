---
title: blc
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cseagle__blc.md
updated: 2026-08-16
confidence: medium
---

# blc

**Binary Lifting Contraption (blc)** is an IDA Pro plugin that integrates **Ghidra's decompiler** into the IDA workflow. It gives reverse engineers an alternate pseudocode view inside IDA—useful when comparing decompiler output, working without Hex-Rays, or studying protected game and anti-cheat binaries from the cheat / IDA Plugins lane. (source: wiki/sources/descriptions/cseagle__blc.md)

Complements the full [[ghidra]] framework and headless Ghidra decompilation peers such as [[ghiradec]] by bridging Ghidra's analysis engine into IDA's disassembly UI rather than running a separate Ghidra session. Sits beside IR-lifting tooling such as [[ida2llvm]] and Hex-Rays microcode utilities such as [[genmc]] for multi-backend static RE.

## Links

- Repo: https://github.com/cseagle/blc

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghiradec]] · [[ida2llvm]] · [[genmc]] · [[happyida]]
