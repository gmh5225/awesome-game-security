---
title: NMMP
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/maoabc__nmmp.md
updated: 2026-07-31
confidence: medium
---

# NMMP

**Nativ Method Map Protector** — Android native code protection that lifts selected Java/Kotlin DEX methods into native implementations. The toolchain extracts DEX method bytecodes, compiles them to ARM/x86 via an interpreter or JIT-like transform, and replaces originals with JNI bridges to the native equivalents. Standard DEX decompilers such as [[jadx]] no longer recover the protected logic from bytecode alone; analysis shifts to bundled `.so` RE and JNI dispatch. (source: wiki/sources/descriptions/maoabc__nmmp.md)

Aimed at Android developers hardening apps and security researchers studying bytecode-to-native conversion as a mobile protection technique. Complements LLVM native obfuscators such as [[dprotect]], packer fingerprinting via [[apkid]], and Zygisk DEX dump hooks such as [[zygisk-dump-dex]].

## Links

- Repo: https://github.com/maoabc/nmmp

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[jadx]] · [[apkid]] · [[dprotect]] · [[zygisk-dump-dex]] · [[android-unpacker]]
