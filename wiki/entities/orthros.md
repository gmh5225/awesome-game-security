---
title: Orthros
kind: entity
topics: [graphics-api, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Lomchat__orthros.md
updated: 2026-11-08
confidence: medium
---

# Orthros

[Lomchat/orthros](https://github.com/Lomchat/orthros) — **browser-based runtime** that runs **unmodified 32-bit x86 Windows game executables** in the client using local CPU, memory, and graphics resources. Combines a reference x86 interpreter, **dynamic x86-to-WebAssembly JIT**, a **PE32 loader**, and **Win32/DirectX high-level emulation (HLE)** on browser primitives; game assets are served through a **virtual filesystem over HTTP**. Targets preservation, in-browser play of legacy PC titles, and an inspectable client-side execution environment for studying binary loading and API behavior. (source: wiki/sources/descriptions/Lomchat__orthros.md)

## Stack

Primarily **ECMAScript modules** on Node.js and in the browser, with Python and native C tooling for CPU conformance testing and benchmarks. (source: wiki/sources/descriptions/Lomchat__orthros.md)

## Dedicated ports

Also ships dedicated browser ports for select titles via WebAssembly engines such as **GoldSrc** and **decompiled re3-family** builds. (source: wiki/sources/descriptions/Lomchat__orthros.md)

## Research use

Like [[bottleship]], separate **emulated guest CPU** behavior from **reimplemented Win32/DirectX host paths** when using Web output as a Windows-faithful reference—apply [[static-runtime-evidence]] lift-vs-HLE labeling. The x86→WASM JIT boundary is another observable split between interpreter fallback and translated hot paths. (source: wiki/sources/descriptions/Lomchat__orthros.md)

Listed under **DirectX → Emulation** beside browser Win32 stacks such as [[bottleship]].

## Links

- Repo: https://github.com/Lomchat/orthros

## Related

[[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[bottleship]] · [[qemu-wasm]] · [[webcheat]] · [[static-runtime-evidence]]
