---
title: ida2llvm
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/loyaltypollution__ida2llvm.md
  - wiki/sources/descriptions/Sandspeare__ida2llvm.md
updated: 2026-08-21
confidence: medium
---

# ida2llvm

Two related **IDA→LLVM IR lifting** projects share this name in the cheat / IDA Plugins lane. Both target reverse-engineering research, binary analysis pipelines, and experiments that combine IDA artifacts with LLVM tooling.

## loyaltypollution — dynamic disassembly lifting

IDA Pro plugin for **dynamic binary lifting**: lifts disassembled code at the cursor to LLVM IR. A viewer stays synchronized with the disassembly window and indicates whether the current selection can be lifted. (source: wiki/sources/descriptions/loyaltypollution__ida2llvm.md)

## Sandspeare — microcode lifting

Python script using IDA APIs with **llvmlite** to translate **IDA microcode** into LLVM IR for downstream analysis. Includes logic for mapping IDA types and structures to LLVM types; ships sample binaries and generated IR examples. (source: wiki/sources/descriptions/Sandspeare__ida2llvm.md)

Complements offline Ghidra→LLVM paths such as [[levo]] and Hex-Rays microcode tooling such as [[genmc]] for IR-level analysis workflows.

## Links

- loyaltypollution: https://github.com/loyaltypollution/ida2llvm
- Sandspeare: https://github.com/Sandspeare/ida2llvm

## Related

[[levo]] · [[genmc]] · [[ida-plugin-pcodegpt]] · [[static-analyzer-factory]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
