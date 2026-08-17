---
title: rust-external-cheat
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/bootmgfw__Rust-External-Cheat.md
updated: 2026-08-17
confidence: medium
---

# rust-external-cheat

**rust-external-cheat** (bootmgfw/Rust-External-Cheat) is a C++ **external** cheat for Facepunch **Rust** that reads process memory from outside the client and renders features through a transparent overlay window. A Windows kernel-mode **WDM driver** (**DriverRW**) provides cross-process memory read, write, allocation, and module-base queries via **IOCTLs**, paired with a user-mode DLL that implements a Rust SDK, entity update loops, and game offset handling. Feature modules include ESP and visual drawing, aimbot logic, a **Dear ImGui** menu backed by **DirectX 9** and Win32, **DirectXMath** world-to-screen helpers, and socket-based communication, along with driver trace cleanup and kernel hooking techniques aimed at evading detection. Intended for game security researchers and reverse engineers studying external cheat architecture, kernel-assisted memory access, and anti-cheat evasion against Rust and similar Unity titles under [[easy-anti-cheat]]. (source: wiki/sources/descriptions/bootmgfw__Rust-External-Cheat.md)

Sits in the kernel-assisted Unity external lane beside other Facepunch Rust externals such as [[rust-external-1]], [[rust-external-source]], and [[rust-external-and-driver-aliencheats]], bootmgfw driver primitives in [[lithium-kernel]], and title-specific bootmgfw externals such as [[apex-external-cheat]] and [[valorant-external-cheat]].

## Links

- Repo: https://github.com/bootmgfw/rust-external-cheat (Rust external cheat with custom kernel driver (DriverRW) and usermode ESP/aim GUI)

## Related

[[easy-anti-cheat]] · [[world-to-screen]] · [[present-hook]] · [[lithium-kernel]] · [[rust-external-1]] · [[rust-external-source]] · [[rust-external-and-driver-aliencheats]] · [[rust-internal]] · [[apex-external-cheat]] · [[valorant-external-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
