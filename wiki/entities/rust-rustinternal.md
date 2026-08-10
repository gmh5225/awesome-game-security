---
title: rust-rustinternal
kind: entity
topics: [game-hacking, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Rust-RustInternal.md
updated: 2026-08-10
confidence: medium
---

# rust-rustinternal

C++ **internal** cheat for Facepunch **Rust** that hooks the **Unity** engine runtime inside the game process. Provides ESP, aimbot, player and item information, no-recoil, and other gameplay modifications via **Mono/IL2CPP** method hooking and direct memory access to Unity game objects. Framed for game security researchers studying Unity-based FPS cheat implementations and **EAC**-protected game exploitation. (source: wiki/sources/descriptions/gmh5225__Rust-RustInternal.md)

Complements the DX11/Horizon scaffold in [[rust-internal]], external kernel/RPM sample [[rust-external-1]], OOP base [[simple-rust-base]], and minimal source [[simple-rust-hack]] for comparing Unity Mono/IL2CPP in-process hooking vs DirectX overlay scaffolds and out-of-process ESP under [[easy-anti-cheat]].

## Links

- Repo: https://github.com/gmh5225/Rust-RustInternal

## Related

[[rust-internal]] · [[rust-external-1]] · [[simple-rust-base]] · [[simple-rust-hack]] · [[il2cpp]] · [[easy-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
