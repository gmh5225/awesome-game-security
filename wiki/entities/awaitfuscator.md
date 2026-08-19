---
title: AwaitFuscator
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/Washi1337__AwaitFuscator.md
updated: 2026-08-19
confidence: medium
---

# AwaitFuscator

**.NET binary-to-binary obfuscator** (Washi1337) that rewrites managed method bodies into long chains of **await** expressions. It uses custom awaiters plus **GetAwaiter** / **GetResult** transforms to produce control flow that is harder for decompilers to reconstruct cleanly. Implemented in **C#** on .NET and shipped as a **command-line tool** with sample programs for testing. Primarily a proof-of-concept for obfuscation research and reverse-engineering resistance experiments. (source: wiki/sources/descriptions/Washi1337__AwaitFuscator.md)

Sits in the managed **Obfuscation Engine** lane beside technique demos such as [[obfuscation-methods]] and production-style protectors such as [[confuserex]] / [[obfuscar]], but focuses on async-state-machine control-flow distortion rather than rename/string encryption or full protector passes. Analysts typically pair output study with [[dnspy]] / de4dot-style tooling and broader [[control-flow-flattening]] recovery workflows.

Same author as [[ghidra-nativeaot]] (Ghidra .NET Native AOT RE plugin).

## Links

- Repo: https://github.com/Washi1337/AwaitFuscator

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[control-flow-flattening]] · [[obfuscation-methods]] · [[confuserex]] · [[obfuscar]] · [[dnspy]] · [[ghidra-nativeaot]]
