---
title: themida-spotter-bn
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ergrelet__themida-spotter-bn.md
updated: 2026-08-15
confidence: medium
---

# themida-spotter-bn

Binary Ninja plugin to **detect obfuscated code locations** in executables protected with Themida, WinLicense, and Code Virtualizer. Tested on x86 and x86_64 targets protected with Oreans products up to version 3.1.9. Aimed at game security researchers and reverse engineers studying offensive techniques in the cheat / Binary Ninja plugins lane. (source: wiki/sources/descriptions/ergrelet__themida-spotter-bn.md)

Companion surface to Cheat → Fix Themida work ([[themida-unmutate]] static mutation recovery, [[unlicense]] Frida dynamic unpack, [[tde]] IDA devirtualization): **BN-side region spotting** for Oreans obfuscation before deobfuscation or VM handler lifting rather than unpack or insn mutation itself.

## Links

- Repo: https://github.com/ergrelet/themida-spotter-bn

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[themida-unmutate]] · [[unlicense]] · [[themida-research]] · [[tde]] · [[triton-bn]] · [[binary-ninja-mcp]] · [[obfuscation-detection]]
