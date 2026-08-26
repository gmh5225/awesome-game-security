---
title: rust-cheat-external-main
kind: entity
topics: [game-hacking, windows-kernel, game-engine, anti-cheat]
sources:
  - wiki/sources/descriptions/Disline1337__Rust-Cheat-External-main.md
updated: 2026-08-26
confidence: medium
---

# rust-cheat-external-main

**rust-cheat-external-main** (Disline1337/Rust-Cheat-External-main) is an **external** cheat framework for Facepunch **Rust** on Windows with separate kernel and user-mode components. A Windows driver handles cross-process memory read and write through **IOCTLs**, while the client side provides overlay rendering and gameplay SDK helpers. The code references **UnityPlayer** and **GameAssembly** module handling, indicating Unity/IL2CPP-based game memory interaction. Intended for cheat development experiments and anti-cheat research into external driver-assisted attack patterns under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/Disline1337__Rust-Cheat-External-main.md)

Slug disambiguates from [[rust-cheat-external]] (gmh5225). Sits in the kernel-assisted Unity external lane beside [[lord-abbot-rust-external-cheat]], [[rust-external-cheat]], [[overflow-rust]], and [[rust-external-1]].

## Links

- Repo: https://github.com/Disline1337/Rust-Cheat-External-main

## Related

[[easy-anti-cheat]] · [[il2cpp]] · [[oxide-dumper]] · [[lord-abbot-rust-external-cheat]] · [[rust-external-cheat]] · [[overflow-rust]] · [[rust-cheat-external]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
