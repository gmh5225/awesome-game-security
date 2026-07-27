---
title: Obscura
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/nkhmelni__Obscura.md
updated: 2026-07-27
confidence: medium
---

# Obscura

Out-of-tree LLVM New Pass Manager plugin that obfuscates binaries at compile time without source changes. Ships thirteen passes covering Objective-C metadata protection, anti-debug and anti-hook checks, string/constant encryption, dynamic symbol resolution, and classic transformations (bogus control flow, control-flow flattening, instruction substitution, indirect branching). Controlled via compiler flags, a small config header, or per-function annotations. Targets Clang, AppleClang, and Swift for C/C++/Objective-C/Swift, with strongest support on Darwin. Aimed at hardening apps and game clients against RE, class dumping, debugging, and runtime hooking. (source: wiki/sources/descriptions/nkhmelni__Obscura.md)

Useful as a Darwin-oriented Obfuscation Engine / OLLVM-style pass-plugin reference alongside [[kagura]], [[dprotect]], and lighter IR tools such as [[the-poor-mans-obfuscator]].

## Links

- Repo: https://github.com/nkhmelni/Obscura

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[kagura]] · [[dprotect]] · [[the-poor-mans-obfuscator]] · [[swiftshield]] · [[swift-string-obfuscator]] · [[alcatraz]]
