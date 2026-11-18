---
title: UE4SS KartRider Drift
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Yoshino-Loli__UE4SS-KartRiderDrift.md
updated: 2026-11-18
confidence: medium
---

# UE4SS KartRider Drift

**UE4SS-KartRiderDrift** (Yoshino-Loli) ships a **patched UE4SS 4.0.0** build aimed at the **Themida-packed** *KartRider Drift* shipping client on **Unreal Engine 4.27**, so script injectors and mod loaders can attach reliably to a protected PE. The fork documents a **pattern sleuth** bounds-check fix in **Rust**, guidance for a **one-byte `DllMain` control-flow** repair, and build notes for **MSVC**, **CMake**, and **Ninja**. A companion **pktcap** module in **C++** hooks **Winsock** `send`/`recv` (including overlapped I/O); **Python** helpers cover DLL injection and **PCAP-style** dump parsing for client–server protocol study. The stack targets reverse engineers and game-security researchers who need stable [[re-ue4ss]] on commercial packers, SDK or Lua modding on a live UE4.27 title, and socket-layer traffic capture beside runtime scripting. (source: wiki/sources/descriptions/Yoshino-Loli__UE4SS-KartRiderDrift.md)

## Positioning

Listed under README **Cheat** as a patched UE4SS 4.0.0 for Themida-packed KartRider Drift with patternsleuth bounds-check fix plus socket-layer pktcap (Game Engine Explorer:Unreal). Complements generic [[re-ue4ss]] and desktop orchestration such as [[ue4ss-launcher]] with **title-specific** packer compatibility and **protocol-capture** tooling rather than a general-purpose mod front end.

## Links

- Repo: https://github.com/Yoshino-Loli/UE4SS-KartRiderDrift [Patched UE4SS 4.0.0 for Themida-packed KartRider Drift: patternsleuth bounds-check fix plus socket-layer pktcap for protocol analysis]

## Related

[[re-ue4ss]] · [[ue4ss-launcher]] · [[unreal-mod-loader]] · [[unreal-object-model]] · [[dumper-7]] · [[bobalkkagi]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]