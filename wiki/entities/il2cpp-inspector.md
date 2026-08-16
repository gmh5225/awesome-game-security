---
title: Il2CppInspector
kind: entity
topics: [game-engine, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/djkaty__Il2CppInspector.md
updated: 2026-08-16
confidence: medium
---

# Il2CppInspector

Comprehensive C# [[il2cpp]] reverse-engineering tool and library for Unity IL2CPP titles. Parses `global-metadata.dat` and IL2CPP binaries (`GameAssembly.dll`, `libil2cpp.so`, etc.) to recover type definitions, method signatures, and metadata — helping game security researchers and modders reconstruct original C# class layouts and method offsets. Generates IDA Pro, Ghidra, and Binary Ninja scripts with full type annotations, C++ header scaffolds, and DLL injection frameworks; supports all IL2CPP versions and platforms. README lane `[Il2Cpp Dump]`. (source: wiki/sources/descriptions/djkaty__Il2CppInspector.md)

Complements generic dump forks such as [[il2cppdumper]] and live mobile harvesters like [[frida-il2cpp-bridge]] when analysts need cross-platform metadata extraction plus ready-made disassembler import scripts.

## Links

- Repo: https://github.com/djkaty/Il2CppInspector

## Related

[[il2cpp]] · [[il2cppdumper]] · [[il2cpp-finder]] · [[il2cpp-versions]] · [[il2cpp-runtime-dumper]] · [[frida-il2cpp-bridge]] · [[dnspy]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
