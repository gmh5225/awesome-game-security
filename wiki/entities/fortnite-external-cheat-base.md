---
title: fortnite-external-cheat-base
kind: entity
topics: [game-hacking, windows-kernel, graphics-api, anti-cheat, game-engine]
sources:
  - wiki/sources/descriptions/bootmgfw__Fortnite-External-Cheat-Base.md
updated: 2026-08-17
confidence: medium
---

# fortnite-external-cheat-base

**fortnite-external-cheat-base** (bootmgfw/Fortnite-External-Cheat-Base) is a C++ **starter template** for building an **external** cheat for Fortnite that reads game memory from outside the process and renders an overlay on top of the game window. It communicates with a kernel driver over **IOCTL** to perform physical memory reads and writes, resolve process base addresses, bypass **CR3** protections used by [[easy-anti-cheat]], and inject synthetic mouse input. The codebase includes Unreal Engine SDK helpers with offset definitions, encrypted **UWorld** pointer decoding, player and entity caching, bone-based [[world-to-screen]] math, and ESP rendering with visibility-colored 2D bounding boxes through an **ImGui** and **DirectX 11** overlay. Window hijacking and a configurable menu drive the main render loop after attaching to `FortniteClient-Win64-Shipping.exe`. Intended for game security researchers and reverse engineers studying external cheat architecture, kernel-assisted memory access, and anti-cheat evasion techniques. (source: wiki/sources/descriptions/bootmgfw__Fortnite-External-Cheat-Base.md)

Sits in the kernel-assisted UE external lane beside other bootmgfw title-specific externals such as [[apex-external-cheat]], [[valorant-external-cheat]], and [[rust-external-cheat]], driver primitives in [[lithium-kernel]], and IOCTL/CR3-oriented Fortnite bases such as [[fortnite-external-base-source]] and [[fortnite-external]].

## Links

- Repo: https://github.com/bootmgfw/fortnite-external-cheat-base (External Fortnite cheat base with kernel driver comms, DirectX 11 overlay, and ImGui menu)

## Related

[[easy-anti-cheat]] · [[unreal-object-model]] · [[world-to-screen]] · [[present-hook]] · [[lithium-kernel]] · [[fortnite-external-base-source]] · [[fortnite-external]] · [[apex-external-cheat]] · [[valorant-external-cheat]] · [[rust-external-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
