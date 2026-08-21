---
title: Static String Obfuscation
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Reijaff__static_string_obfuscation.md
updated: 2026-08-21
confidence: medium
---

# Static String Obfuscation

Zig compile-time static string obfuscation demo. The build pipeline generates randomized keys at compile time and applies XOR-based transforms so plaintext literals are not stored directly in the output binary. Targets stripped x86_64 Windows executables with lightweight runtime decryption. Primary use case is reverse-engineering resistance experiments and anti-analysis hardening in security-oriented software (Anti Cheat → String Crypter). (source: wiki/sources/descriptions/Reijaff__static_string_obfuscation.md)

Useful alongside other compile-time string crypters such as [[obfuscate]] / [[crystr]] / [[skcrypter]] / [[xorlit]] / [[xordata]] / [[mystic-xorstr]]. Zig-specific; not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/Reijaff/static_string_obfuscation

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[obfuscate]] · [[crystr]] · [[skcrypter]] · [[xorlit]] · [[xordata]] · [[obfuscatxor]]
