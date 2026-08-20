---
title: Squalr-Sharp
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Squalr__Squalr-Sharp.md
updated: 2026-08-20
confidence: medium
---

# Squalr-Sharp

**Squalr-Sharp** (Squalr/Squalr-Sharp) is a high-performance **Windows memory editing** application for creating and sharing cheats in desktop games. Written primarily in **C#/.NET**, it combines memory scanning, pointer resolution, and **x86/x64 assembly injection** through a **WPF GUI**, a **CLI**, and a reusable **engine API**. (source: wiki/sources/descriptions/Squalr__Squalr-Sharp.md)

Fast scans use multi-threading and **SIMD** (SSE, AVX, or AVX-512). **NASM-based** assemble/disassemble support and **C# scripting** enable deeper analysis and automation. Additional modules cover process attachment, memory viewing, debugging, and **.NET object inspection**—useful for game hacking, reverse engineering, and Windows memory research.

Sits in the Windows **C# memory-editor** lane beside [[cheat-engine]] and [[pince]], and complements managed RE tooling such as [[dnspy]] when inspecting live .NET game objects.

## Links

- Repo: https://github.com/Squalr/Squalr-Sharp (README tag: C# game memory editor with scanning, pointers, and assembly injection)

## Related

[[cheat-engine]] · [[pince]] · [[bizhawk]] · [[intro-to-gamehacking]] · [[reclass-ex]] · [[dnspy]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
