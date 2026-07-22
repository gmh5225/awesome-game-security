---
title: Mystic-xorstr
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/wufhex__Mystic-xorstr.md
updated: 2026-07-22
confidence: medium
---

# Mystic-xorstr

C++17 header-only library that encrypts strings and integers at compile time and decrypts them at runtime with SIMD (AVX / SSE / ARM NEON). Per-value keys and IVs come from constexpr computations seeded at compile time; optional junk-code injection and decompiler-breaking tricks (stack bloating, opaque predicates) clutter disassembly and can disrupt tools such as IDA Pro without slowing runtime. Supports CRT-less / minimal builds via `_MYSTIC_MINIMAL`. Aimed at string/integer obfuscation for game security, anti-cheat, or reverse-engineering resistance. (source: wiki/sources/descriptions/wufhex__Mystic-xorstr.md)

Useful as a compile-time xorstr-style encrypt-variable reference alongside [[sbox]] / [[obfusk8]]; recovery-side counterpart [[ida-jm-xorstr-decrypt-plugin]] targets JM Xorstr-style strings in IDA. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/wufhex/Mystic-xorstr

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[sbox]] · [[obfusk8]] · [[ida-jm-xorstr-decrypt-plugin]] · [[obfcoder]] · [[kagura]]
