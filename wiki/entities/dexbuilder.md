---
title: DexBuilder
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/LSPosed__DexBuilder.md
updated: 2026-08-23
confidence: medium
---

# DexBuilder

**DexBuilder** (LSPosed) is a **C++ library** for programmatically constructing **DEX bytecode** structures as an alternative to **dexmaker**-style generation. The codebase is largely derived from **AOSP** components and includes LSPosed-specific modifications for **runtime integration** scenarios. Instruction coverage targets what primary users need rather than every opcode path. Useful for **Android framework researchers** and **tooling developers** who need native-side DEX generation. (source: wiki/sources/descriptions/LSPosed__DexBuilder.md)

Complements DEX manipulation and analysis lanes such as [[dex2jar]], [[dexkit-android]], and runtime DEX recovery via [[zygisk-dump-dex]]; pairs with LSPosed/Xposed hook scaffolding such as [[xposed-module-kit]] and [[dirty-sepolicy]].

## Links

- Repo: https://github.com/LSPosed/DexBuilder (README tag: Generate dex file by c++)

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[dex2jar]] · [[dexkit-android]] · [[zygisk-dump-dex]] · [[xposed-module-kit]] · [[dirty-sepolicy]] · [[jadx]]
