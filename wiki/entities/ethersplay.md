---
title: ethersplay
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__ethersplay.md
updated: 2026-08-09
confidence: medium
---

# ethersplay

Binary Ninja plugin for disassembling Ethereum Virtual Machine (EVM) bytecode. Adds EVM instruction decoding, control-flow graph generation, and cross-reference analysis for smart-contract binaries inside Binary Ninja—aimed at analyzing compiled Solidity contracts for blockchain security auditors. (source: wiki/sources/descriptions/gmh5225__ethersplay.md)

Not a standalone EVM emulator—scoped to Binary Ninja EVM ISA support and on-chain contract bytecode RE.

Complements other non-x86 Binary Ninja architecture plugins such as [[bn-ebpf-solana]] (Solana SBF/eBPF) and [[ptxninja]] (PTX/CUDA GPU ISA).

## Links

- Repo: https://github.com/gmh5225/ethersplay

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[bn-ebpf-solana]] · [[binaryninja-pcode]] · [[ptxninja]] · [[ariadne]] · [[binja-kc]] · [[x64dbgbinja]]
