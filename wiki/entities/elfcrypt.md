---
title: ELFcrypt
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/droberson__ELFcrypt.md
updated: 2026-08-16
confidence: medium
---

# ELFcrypt

Tool that RC4-encrypts the `.text` section of ELF binaries and embeds a decryption stub that `mprotect`s the section, decrypts it at runtime, then jumps to the original entry point. Operates by mmap-ing the ELF, locating the target section via section headers, applying RC4 encryption, and writing a self-decrypting binary to disk. Mainly useful for security researchers studying ELF binary encryption, runtime unpacking techniques, and basic software protection on Linux under Anti Cheat → Binary Packer / `[ELF]` RC4. (source: wiki/sources/descriptions/droberson__ELFcrypt.md)

Useful as a Linux/ELF `.text` encryption reference alongside [[elfpacker]] (XOR stub), [[elfuck]], and [[harmless]]—not a full unpacker or debugger.

## Links

- Repo: https://github.com/droberson/ELFcrypt

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[elfpacker]] · [[elfuck]] · [[harmless]] · [[m0dern-p4cker]] · [[ward]]
