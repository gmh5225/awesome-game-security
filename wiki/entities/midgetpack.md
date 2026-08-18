---
title: midgetpack
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/arisada__midgetpack.md
updated: 2026-08-18
confidence: medium
---

# midgetpack

ELF binary packer for protecting executables on untrusted systems. Offers password mode and a challenge-response mode based on Curve25519 key exchange with AES-128 and HMAC-SHA256. Supports cross-architecture packing across Linux and FreeBSD targets including x86, x86-64, and ARM. Aimed at security practitioners hardening sensitive tooling during controlled assessments and deployments under Anti Cheat → Binary Packer / `[ELF]`. (source: wiki/sources/descriptions/arisada__midgetpack.md)

Useful as a Linux/FreeBSD ELF crypto-packing reference alongside [[elfpacker]], [[elfuck]], and [[papaw]]—not a full unpacker or commercial protector.

## Links

- Repo: https://github.com/arisada/midgetpack

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[elfpacker]] · [[elfuck]] · [[papaw]] · [[pe32-password]] · [[harmless]] · [[awesome-executable-packing]]
