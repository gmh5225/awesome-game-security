---
title: sbox
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/x86byte__sbox.md
updated: 2026-07-18
confidence: medium
---

# sbox

C++ compile-time string obfuscation library using S-box / AES-128 substitution with constexpr encryption macros and encode/decode APIs, keeping plaintext strings out of static binary analysis. Spin-off from Obfusk8; no delimiters, binary-safe ciphertext blocks. Aimed at Anti Cheat → Compile Time / Obfuscation Engine research. (source: wiki/sources/descriptions/x86byte__sbox.md)

Useful as a compile-time string-encryption reference alongside LLVM pass-plugin and packer hardeners—not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/x86byte/sbox

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[kagura]] · [[wprotect]] · [[ida-jm-xorstr-decrypt-plugin]] · [[shredder-rs]]
