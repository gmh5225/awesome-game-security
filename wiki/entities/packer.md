---
title: Packer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/longqun__Packer.md
updated: 2026-07-31
confidence: medium
---

# Packer

Windows PE packer in C/C++ that compresses and encrypts executables, packs original sections, and prepends a decompression stub that restores the original code at runtime. Handles import table reconstruction, relocation fixing, and TLS callback preservation—illustrating the basic architecture of executable compression tools. Listed under Anti Cheat → Binary Packer / `[X86]`; aimed at security researchers studying PE packing, anti-analysis methods, and unpacking strategies rather than shipping as an AC product. (source: wiki/sources/descriptions/longqun__Packer.md)

Useful as an educational x86 PE packer reference alongside [[pe32-password]], [[x64-exe-packer]], and [[2pack]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/longqun/Packer

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[pe32-password]] · [[x64-exe-packer]] · [[2pack]] · [[xorpacker]] · [[totalpe2]]
