---
title: Hyapk
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/beto2-dev__Hyapk.md
updated: 2026-09-12
confidence: medium
---

# Hyapk

**Hyapk** is a command-line protection and hardening packer for Android applications and games. The Kotlin CLI drives a C native runtime that applies dex-level and native defenses: selected methods can be converted to generated C via Dex2C or to custom **HyVm** virtual-machine bytecode with per-build opcode permutation and ChaCha20-Poly1305 encryption. Additional layers include signature and DEX integrity checks, anti-tamper and anti-debug guards, smali renaming, encrypted assets, and anti-Frida, anti-root, and emulator heuristics. The tool targets legitimate app owners who need to raise the cost of reverse engineering, tampering, and cheating on Android titles. (source: wiki/sources/descriptions/beto2-dev__Hyapk.md)

README lane: Anti Cheat → Binary Packer — complements smali-level obfuscation such as [[obfuscapk]] and commercial shielding research such as [[appsealing-reversal]]; pairs with unpack/ID lanes ([[android-unpacker]], [[apkid]], [[jadx]]) when studying protected mobile clients.

## Mechanisms

| Layer | Notes |
|-------|-------|
| HyVm VMP | Per-method custom VM bytecode; per-build opcode permutation |
| Dex2C | Selected methods lowered to generated native C |
| Encryption | ChaCha20-Poly1305 on VM opcodes |
| Integrity | APK signature and DEX integrity checks |
| Environment | Anti-Frida, anti-root, emulator heuristics |
| Obfuscation | Smali renaming, encrypted assets, anti-debug/anti-tamper |

## Links

- Repo: https://github.com/beto2-dev/Hyapk

## Related

[[mobile-anti-cheat]] · [[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[obfuscapk]] · [[appsealing-reversal]] · [[pairipcore]] · [[android-unpacker]] · [[apkid]] · [[jadx]] · [[frida]] · [[antifrida]]
