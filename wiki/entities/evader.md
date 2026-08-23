---
title: Evader
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/KooroshRZ__Evader.md
updated: 2026-08-23
confidence: medium
---

# Evader

**KooroshRZ** Windows **PE packer and crypter** that encrypts an executable payload and embeds it into a new output file. Supports configurable **key size** and **keyspace complexity**, then performs **runtime key recovery** and **in-memory payload execution** in the unpacking stage. The repository splits into a **packer component** and an **unpack stub**, both implemented in C++. Core techniques include **payload obfuscation**, **resource embedding**, and **staged decryption**. Mainly used for packer development practice and evasion-focused reverse-engineering research. Listed under Anti Cheat → Binary Packer `[PE]`. (source: wiki/sources/descriptions/KooroshRZ__Evader.md)

Useful as an educational PE packer/crypter reference alongside [[pe-packer]], [[hm-pe-packer]], and [[polyengine]]—not a full commercial protector or unpacker.

## Links

- Repo: https://github.com/KooroshRZ/Evader

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pe-packer]] · [[hm-pe-packer]] · [[polyengine]] · [[pepacker-samlarenn]] · [[exe-packer]] · [[atom-pe-packer]] · [[packer-tutorial]] · [[windows-dll-injector]] · [[unpacker]]
