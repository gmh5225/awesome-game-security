---
title: ghidra-cpp-class-analyzer
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/astrelsky__Ghidra-Cpp-Class-Analyzer.md
updated: 2026-08-18
confidence: medium
---

# ghidra-cpp-class-analyzer

Ghidra extension that analyzes **C++ class metadata** and **runtime type information (RTTI)** in compiled binaries. Written in Java with Gradle build scripts, it adds analyzers for GCC, Clang, and MSVC RTTI models, vtables, constructors and destructors, and inheritance reconstruction. Visualization tooling includes class hierarchy views and scripts that integrate with the extension APIs. Intended for reverse engineers and game security analysts working on large native C++ targets. (source: wiki/sources/descriptions/astrelsky__Ghidra-Cpp-Class-Analyzer.md)

Ghidra-side peer to IDA C++ RTTI tooling such as [[rtti-parser]], [[pyclassinformer]], and [[ida-medigate]]. Gradle packaging may use the archived [[ghidra-gradle-plugin]] from the same maintainer; pairs with platform extensions such as [[ghidra-orbis]] on console-native C++ binaries.

## Links

- Repo: https://github.com/astrelsky/Ghidra-Cpp-Class-Analyzer (README tag: C++ Class and Run Time Type Information Analyzer)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-gradle-plugin]] · [[ghidra-orbis]] · [[rtti-parser]] · [[pyclassinformer]] · [[ida-medigate]] · [[classy]]
