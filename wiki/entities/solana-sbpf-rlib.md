---
title: solana-sbpf-rlib
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/cpkt9762__solana-sbpf-rlib.md
updated: 2026-08-16
confidence: medium
---

# solana-sbpf-rlib

Python tooling that builds **Solana sBPF rlib** signature packs for IDA Pro, Ghidra, and Binary Ninja. Targets plugin development, modding, and SDK generation workflows where analysts maintain IDA-style signature databases for Solana BPF bytecode—useful for game-security researchers and reverse engineers studying offensive techniques in that lane. (source: wiki/sources/descriptions/cpkt9762__solana-sbpf-rlib.md)

Complements live SBF disassembly plugins such as [[bn-ebpf-solana]] (Binary Ninja ISA support) by supplying static library identification signatures rather than a standalone VM or decompiler.

## Links

- Repo: https://github.com/cpkt9762/solana-sbpf-rlib

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[bn-ebpf-solana]] · [[bndb2pat]] · [[ida-sigmaker]] · [[sigmakerex]] · [[hyara]] · [[ethersplay]]
