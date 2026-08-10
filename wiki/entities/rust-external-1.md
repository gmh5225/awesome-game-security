---
title: rust-external-1
kind: entity
topics: [game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/gmh5225__rust-external-1.md
updated: 2026-08-07
confidence: medium
---

# rust-external-1

C++ **external** cheat for Facepunch **Rust** that reads the Unity game process without injection. Uses a kernel driver or `ReadProcessMemory` to pull player positions, item locations, and game state, then renders ESP on a separate overlay. Framed for game security researchers studying external cheat patterns on **EAC-protected Unity** titles. (source: wiki/sources/descriptions/gmh5225__rust-external-1.md)

Complements in-process scaffolds such as [[rust-internal]] and minimal title-specific sources [[simple-rust-hack]], the rendering/networking external sample [[rust-external]], plus the OOP driver/rendering base [[simple-rust-base]], for comparing external kernel/RPM + overlay ESP vs internal DX11/ImGui hooks under [[easy-anti-cheat]].

## Links

- Repo: https://github.com/gmh5225/rust-external-1

## Related

[[rust-external]] · [[rust-internal]] · [[simple-rust-hack]] · [[simple-rust-base]] · [[world-to-screen]] · [[il2cpp]] · [[easy-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]]
