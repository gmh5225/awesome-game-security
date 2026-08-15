---
title: themida-unmutate
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ergrelet__themida-unmutate.md
updated: 2026-08-15
confidence: medium
---

# themida-unmutate

Python 3 tool to **statically deobfuscate** functions protected by Themida, WinLicense, and Code Virtualizer 3.x **mutation-based obfuscation**. Tested on Themida up to version 3.1.9. Aimed at game security researchers and reverse engineers studying offensive techniques in the cheat / Fix Themida lane. (source: wiki/sources/descriptions/ergrelet__themida-unmutate.md)

Companion surface to Cheat → Fix Themida work ([[unlicense]] Frida dynamic unpack, [[tde]] IDA devirtualization, [[themida-research]] VM internals): **static mutation recovery** on selected functions rather than live OEP/IAT rebuild or VM handler lifting.

## Links

- Repo: https://github.com/ergrelet/themida-unmutate

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unlicense]] · [[themida-research]] · [[tde]] · [[magicmida-rs]]
