---
title: crycall
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/android1337__crycall.md
updated: 2026-08-18
confidence: medium
---

# crycall

Compile-time C++ call obfuscation library for hiding function invocations. Wraps calls through lambda and virtual-dispatch machinery so the real callee and argument flow are harder to recover during static or dynamic analysis. Header-based implementation supports C++14+, includes macros for normal and virtual calls, and is designed to work with obfuscation-focused compiler settings. Aimed at anti-reversing and game protection research where call-site clarity is a detection or analysis risk (Anti Cheat → Compile Time). (source: wiki/sources/descriptions/android1337__crycall.md)

Complements compile-time constant obfuscation such as [[crystr]] from the same author; distinct from PE post-processors like [[call-obfuscator]] that rewrite import tables at the binary level. Not a full obfuscation engine or commercial protector.

## Links

- Repo: https://github.com/android1337/crycall

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[crystr]] · [[call-obfuscator]] · [[obfusk8]] · [[skcrypter]]
