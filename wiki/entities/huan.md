---
title: Huan
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/frkngksl__Huan.md
updated: 2026-08-15
confidence: medium
---

# Huan

**Encrypted PE loader generator** built for learning PE file structure and the Windows PE loading process. Encrypts the target PE with **different keys on each run** and embeds the ciphertext in a **new section** of the generated loader binary. Listed under Anti Cheat → Binary Packer; aimed at anti-cheat engineers and defensive security researchers studying binary packers and custom PE loaders—not an AC product. (source: wiki/sources/descriptions/frkngksl__Huan.md)

Useful as a PE loader/packer reference alongside [[packer-tutorial]], [[atom-pe-packer]], and [[tinyload]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/frkngksl/Huan

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[packer-tutorial]] · [[atom-pe-packer]] · [[pepacker]] · [[tinyload]] · [[awesome-executable-packing]]
