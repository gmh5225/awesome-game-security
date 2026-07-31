---
title: ida2llvm
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/loyaltypollution__ida2llvm.md
updated: 2026-07-31
confidence: medium
---

# ida2llvm

IDA Pro plugin for **dynamic binary lifting**: lifts disassembled code at the cursor to LLVM IR. A viewer stays synchronized with the disassembly window and indicates whether the current selection can be lifted. (source: wiki/sources/descriptions/loyaltypollution__ida2llvm.md)

Aimed at game-security researchers and reverse engineers studying offensive static RE in the cheat / IDA Plugins lane. Complements offline Ghidra→LLVM paths such as [[levo]] and Hex-Rays microcode tooling such as [[genmc]] for IR-level analysis workflows.

## Links

- Repo: https://github.com/loyaltypollution/ida2llvm

## Related

[[levo]] · [[genmc]] · [[ida-plugin-pcodegpt]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
