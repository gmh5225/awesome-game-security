---
title: Fatpack
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Fatmike-GH__Fatpack.md
updated: 2026-08-25
confidence: medium
---

# Fatpack

**Fatmike-GH** Windows **x64 PE packer** that compresses executables with **LZMA** and runs them through a **custom loader stub**. Written mainly in C++, it supports both **resource-based** and **section-based** packing, **icon and manifest** handling, and robust **relocation**, **import**, and **TLS** processing. The solution includes helper tooling to embed loader stubs and automate post-build integration. Primary use case is **executable protection research** and **manual-mapping style loader experimentation**. Listed under Anti Cheat → Binary Packer (full TLS support). (source: wiki/sources/descriptions/Fatmike-GH__Fatpack.md)

Useful as an educational x64 PE packer reference with strong TLS handling alongside [[hm-pe-packer]], [[atom-pe-packer]], and [[evader]]—not a full commercial protector or unpacker.

## Links

- Repo: https://github.com/Fatmike-GH/Fatpack

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[hm-pe-packer]] · [[atom-pe-packer]] · [[pe-packer]] · [[exe-packer]] · [[evader]] · [[tinyload]] · [[packer-tutorial]] · [[unpacker]]
