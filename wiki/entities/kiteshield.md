---
title: Kiteshield
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/GunshipPenguin__kiteshield.md
updated: 2026-08-25
confidence: medium
---

# Kiteshield

**Linux x86-64 ELF packer and protector** (GunshipPenguin) written mainly in C with assembly helpers. Wraps executables with layered RC4 encryption and injects a custom loader that decrypts, maps, and runs code entirely in user space. The runtime engine uses **ptrace** to keep only functions on the active call stack decrypted and adds multiple anti-debugging checks during execution. Serves as an educational platform for binary obfuscation and anti-analysis research—not a production anti-cheat product. (source: wiki/sources/descriptions/GunshipPenguin__kiteshield.md)

Useful as a Linux ELF packer/protector reference alongside [[elfpacker]], [[elfcrypt]], [[silent-packer]], and [[vmpacker]] for studying call-stack–scoped decryption and ptrace-based anti-debug patterns. Complements Linux anti-debug catalogs such as [[adbg]] and Windows technique collections such as [[anti-debugging]].

## Links

- Repo: https://github.com/GunshipPenguin/kiteshield

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[elfpacker]] · [[elfcrypt]] · [[elfuck]] · [[silent-packer]] · [[vmpacker]] · [[adbg]] · [[anti-debugging]] · [[midgetpack]]
