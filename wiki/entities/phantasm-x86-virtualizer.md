---
title: Phantasm x86 Virtualizer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/layerfsd__phantasm-x86-virtualizer.md
updated: 2026-08-01
confidence: medium
---

# Phantasm x86 Virtualizer

**x86 code virtualizer** for protecting native programs by translating selected logic into a custom VM. The VM runtime can be **statically linked** into the target binary or **manually copied** into the executable during integration. Aimed at anti-cheat engineers and defensive security researchers building or evaluating obfuscation-engine protections under Anti Cheat → Obfuscation Engine / `[VM]`. (source: wiki/sources/descriptions/layerfsd__phantasm-x86-virtualizer.md)

Useful as an open x86 virtualization-obfuscation reference alongside bin2bin virtualizers such as [[nocturne]] and commercial-style protectors such as [[vxlang-page]] — distinct from VMProtect/Themida handler-recovery tooling like [[novmpy]].

## Links

- Repo: https://github.com/layerfsd/phantasm-x86-virtualizer

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[nocturne]] · [[vxlang-page]] · [[wprotect]] · [[novmpy]]
