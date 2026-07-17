---
title: Kagura
kind: entity
topics: [anti-cheat, reverse-engineering, mobile-security]
sources:
  - wiki/sources/descriptions/ykus4__kagura.md
updated: 2026-07-17
confidence: medium
---

# Kagura

LLVM New Pass Manager plugin (LLVM 17+, `-fpass-plugin`; no LLVM source tree patch) for native code obfuscation and anti-tamper across mobile, desktop, and WebAssembly. Passes include control-flow flattening / bogus CFG, string and data encryption, memory-value obfuscation, import indirection, and basic-block integrity. Companion runtime covers anti-debug, hook/breakpoint detection, integrity checks, and jailbreak/root detection. Integrates with Android NDK, iOS/Xcode, CMake, Bazel, Unity, and Unreal for game protection / DRM / SDK hardening. (source: wiki/sources/descriptions/ykus4__kagura.md)

Useful as an Obfuscation Engine / OLLVM-style pass-plugin reference for defensive RE and AC research—not a shipped anti-cheat product.

## Links

- Repo: https://github.com/ykus4/kagura

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[shredder-rs]] · [[pe32-password]] · [[deobf]] · [[idadeflat]]
