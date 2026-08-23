---
title: lord-abbot-rust-external-cheat
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/LordAbbot__Rust-External-Cheat.md
updated: 2026-08-23
confidence: medium
---

# lord-abbot-rust-external-cheat

**lord-abbot-rust-external-cheat** (LordAbbot/Rust-External-Cheat) is a C++ **external** cheat framework for Facepunch **Rust** on Windows that combines user-mode and kernel-mode components. A custom kernel driver handles cross-process memory read/write, paired with an external DLL module for game logic. The user-mode side integrates **Dear ImGui** and **DirectX** rendering to provide ESP, aimbot, and recoil-related assistance. Intended for game cheating research and for studying anti-cheat detection surfaces around driver-assisted externals under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/LordAbbot__Rust-External-Cheat.md)

Sits in the kernel-assisted Unity external lane beside other Facepunch Rust externals such as [[rust-external-cheat]], [[rust-external-1]], [[rust-external-source]], and [[overflow-rust]].

## Links

- Repo: https://github.com/LordAbbot/Rust-External-Cheat

## Related

[[easy-anti-cheat]] · [[world-to-screen]] · [[present-hook]] · [[rust-external-cheat]] · [[rust-external-1]] · [[rust-external-source]] · [[overflow-rust]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
