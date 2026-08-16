---
title: covirt
kind: entity
topics: [reverse-engineering, anti-cheat]
sources:
  - wiki/sources/descriptions/dmaivel__covirt.md
updated: 2026-08-16
confidence: medium
---

# covirt

**x86-64 code virtualizer** that lifts native instructions into a **stack-based virtual machine** for VM-based obfuscation. Supports **PE (MinGW)** and **ELF** targets, applies **mixed boolean arithmetic (MBA)** transforms and **self-modifying code** passes, and uses **code markers** to delimit protected regions in the binary. Aimed at security researchers studying VM obfuscation and building custom binary protection schemes under Anti Cheat → Obfuscation Engine / `[VM]`. (source: wiki/sources/descriptions/dmaivel__covirt.md)

Useful as an open x64 virtualization reference alongside [[phantasm-x86-virtualizer]], [[guardian-rs]], and [[nocturne]] — with built-in MBA and SMC layers that pair with [[mixed-boolean-arithmetic]] recovery research.

## Links

- Repo: https://github.com/dmaivel/covirt

## Related

[[overviews/reverse-engineering]] · [[overviews/anti-cheat]] · [[mixed-boolean-arithmetic]] · [[phantasm-x86-virtualizer]] · [[guardian-rs]] · [[nocturne]] · [[cerberus]] · [[vmattack]]
