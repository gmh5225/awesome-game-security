---
title: Silent Packer
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/SilentVoid13__Silent_Packer.md
updated: 2026-08-21
confidence: medium
---

# Silent Packer

Pure C binary packer for ELF and PE executables. Supports multiple packing strategies—section insertion, code-cave techniques, and text-section infection—with XOR and AES-based encryption options. The codebase includes low-level loader and assembly components that perform runtime unpacking before transferring control to the original entry point. Listed under Anti Cheat → Binary Packer. Mainly used for reverse-engineering practice, obfuscation experiments, and defensive research on packed binaries—not a commercial protector. (source: wiki/sources/descriptions/SilentVoid13__Silent_Packer.md)

Useful as a cross-format (ELF + PE) educational packer reference alongside [[elfpacker]], [[exe-packer]], and [[hxor-packer]]—not a full unpacker or analysis framework.

## Links

- Repo: https://github.com/SilentVoid13/Silent_Packer

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[elfpacker]] · [[exe-packer]] · [[hxor-packer]] · [[awesome-executable-packing]] · [[unpacker]]
