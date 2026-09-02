---
title: jit-dumper
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Anonym0ose__JitDumper.md
updated: 2026-09-02
confidence: medium
---

# jit-dumper

**Windows-focused toolchain** for dumping **.NET CIL method bodies** by intercepting **JIT compilation internals**. Combines a **C# analysis application** with a **C++ hook component** that leverages **Detours** and **symbol or PDB data**. Supports multiple **.NET generations** and reconstructs metadata needed to inspect compiled method behavior. Aimed at reverse engineers and software-protection analysts working with managed code internals. (source: wiki/sources/descriptions/Anonym0ose__JitDumper.md)

Complements static managed RE via [[dnspy]] and [[ilspy]], static CIL parsing via [[dncil]], and runtime .NET unpack via [[vmunprotect-dumper]] when protection hides method bodies until JIT.

## Links

- Repo: https://github.com/Anonym0ose/JitDumper

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[dnspy]] · [[dncil]] · [[ilspy]] · [[detours]] · [[vmunprotect-dumper]] · [[confuserex]] · [[dnspymcp]]
