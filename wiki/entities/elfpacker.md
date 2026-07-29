---
title: ELFpacker
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/mix64__ELFpacker.md
updated: 2026-07-29
confidence: medium
---

# ELFpacker

ELF32 binary packer that XOR-encrypts the `.text` section and prepends a decryption stub that restores the original code at runtime before jumping to the original entry point. Manipulates ELF headers, program headers, and section headers to inject the stub segment while preserving the binary's loadable structure. Aimed at anti-cheat engineers and defensive researchers studying packed ELF clients under Anti Cheat → Binary Packer / `[ELF]`, rather than shipping as an AC product. (source: wiki/sources/descriptions/mix64__ELFpacker.md)

Useful as a Linux/ELF packer reference alongside [[woody-woodpacker]], [[elfuck]], and [[m0dern-p4cker]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/mix64/ELFpacker

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[woody-woodpacker]] · [[elfuck]] · [[m0dern-p4cker]] · [[pe32-password]] · [[2pack]]
