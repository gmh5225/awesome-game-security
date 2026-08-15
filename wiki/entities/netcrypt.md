---
title: netcrypt
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/friedkiwi__netcrypt.md
updated: 2026-08-15
confidence: medium
---

# netcrypt

**.NET PE file packer** written in C# that embeds a target managed assembly as an **encrypted and compressed resource** inside a loader-stub executable. At runtime the stub decrypts, decompresses, and invokes the original assembly entry point **entirely within the CLR**—no native code and near-zero unpacking delay. A companion WinForms GUI (**SimplePacker**) provides drag-and-drop packing. Listed under Anti Cheat → Binary Packer / `.NET`; aimed at anti-cheat engineers and defensive researchers studying managed-client packing vs dnSpy/IL-level RE—not an AC product. (source: wiki/sources/descriptions/friedkiwi__netcrypt.md)

Useful as a pure-CLR PE packer reference alongside [[confuserex]], [[xorpacker]], and [[obfuscar]]—not a full unpacker or commercial protector.

## Links

- Repo: https://github.com/friedkiwi/netcrypt

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[confuserex]] · [[xorpacker]] · [[obfuscar]] · [[obfuscation-methods]] · [[packer-tutorial]]
