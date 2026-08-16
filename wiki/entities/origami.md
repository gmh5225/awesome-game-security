---
title: Origami
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/dr4k0nia__Origami.md
updated: 2026-08-16
confidence: medium
---

# Origami

**.NET assembly packer** that compresses managed executables and stores the compressed payload inside PE format structures—either by abusing the **debug directory** or a custom **`.origami`** section. A runtime **RelocLoader** decompresses the embedded payload and executes the original assembly from PE data at load time. Listed under Anti Cheat → Binary Packer / `.NET`; aimed at security researchers studying .NET packing, PE format abuse, and managed code protection—not an AC product. (source: wiki/sources/descriptions/dr4k0nia__Origami.md)

Useful as a PE-structure–centric .NET packer reference alongside [[netcrypt]], [[confuserex]], and [[packer-tutorial]]—not a full unpacker or commercial protector.

## Links

- Repo: https://github.com/dr4k0nia/Origami

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[netcrypt]] · [[confuserex]] · [[xorpacker]] · [[packer-tutorial]] · [[totalpe2]]
