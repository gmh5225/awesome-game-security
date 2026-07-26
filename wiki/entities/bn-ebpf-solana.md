---
title: bn-ebpf-solana
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/otter-sec__bn-ebpf-solana.md
updated: 2026-07-26
confidence: medium
---

# bn-ebpf-solana

Binary Ninja plugin for disassembling and analyzing Solana eBPF (SBF) bytecode. Adds Solana’s custom BPF instruction set to Binary Ninja—SBF-specific encoding, memory model, and calling conventions—so compiled Solana programs (smart contracts) can be decompiled and audited. Aimed at blockchain security researchers; sits in the Cheat Binary Ninja Plugins lane as a non-x86 architecture RE tool. (source: wiki/sources/descriptions/otter-sec__bn-ebpf-solana.md)

Not a standalone Solana VM—scoped to Binary Ninja SBF / eBPF ISA support and program analysis.

## Links

- Repo: https://github.com/otter-sec/bn-ebpf-solana

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[binaryninja-pcode]] · [[ptxninja]] · [[ariadne]] · [[binja-kc]] · [[x64dbgbinja]] · [[opaque-predicates-detective]]
