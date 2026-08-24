---
title: Spoof-RetAddr
kind: entity
topics: [game-hacking, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/HulkOperator__Spoof-RetAddr.md
updated: 2026-08-24
confidence: medium
---

# Spoof-RetAddr

Compact **x64 proof-of-concept** for **spoofing WinAPI return addresses** by modifying the stack. Combines **C and NASM assembly** to demonstrate stack manipulation in a reusable example, illustrating **call-stack obfuscation** patterns common in red-team and anti-detection research. Intended for educational use in reverse engineering and low-level **Windows x64 calling-convention** study. (source: wiki/sources/descriptions/HulkOperator__Spoof-RetAddr.md)

Sits in the `Cheat > Spoof Stack` lane beside minimal x64 return-address spoofing samples such as [[ret-spoofing]], x64 trampoline implementations such as [[callstackspoofer-2]], and x86 header-only libraries such as [[x86-ret-spoof]].

## Links

- Repo: https://github.com/HulkOperator/Spoof-RetAddr

## Related

[[stack-spoofing]] · [[ret-spoofing]] · [[callstackspoofer-2]] · [[x86-ret-spoof]] · [[return-address-spoofer]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
