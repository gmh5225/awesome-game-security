---
title: GameApiDetector
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/iamnotoneself__GameApiDetector.md
updated: 2026-11-17
confidence: medium
---

# GameApiDetector

**GameApiDetector** (iamnotoneself/GameApiDetector) is a **Windows** desktop utility written in **Rust** with an **egui** UI that scans installed **game libraries** and reports which **graphics APIs** each title actually uses at runtime. It enumerates loaded modules in running game processes to classify **Vulkan**, **DirectX 9–12**, and **OpenGL** from standard system DLLs (`vulkan-1.dll`, `d3d11.dll`, `opengl32.dll`, etc.). Storefront discovery covers **Steam**, **Epic**, **GOG**, **EA**, **Ubisoft**, **Battle.net**, and **Xbox**, with support for manually added executables. It can detect **DXVK** via version metadata in game-local D3D DLLs and offers install, restore, or Vulkan-related launch options. The tool targets PC gamers and **compatibility researchers** who need a clear view of rendering stacks and DXVK status, including awareness of risks when altering binaries on titles protected by **anti-cheat**. (source: wiki/sources/descriptions/iamnotoneself__GameApiDetector.md)

## Detection model

- **Runtime module attribution** — infers the active graphics backend from loaded system and game-local DLLs in a live process, not from static launcher metadata alone.
- **Library aggregation** — unifies titles from major PC storefronts plus user-defined binaries into one audit surface.

## DXVK workflow

- **Local DLL inspection** — reads DXVK version metadata from game-directory D3D wrappers.
- **Managed changes** — optional install, restore, and launch helpers for Vulkan-oriented compatibility layers.

## Research framing

Legitimate **rendering-stack inventory** and **translation-layer triage**; swapping game-local DXGI/D3D binaries can trigger **integrity checks** on multiplayer or kernel-protected titles—pair observations with [[overviews/anti-cheat]] policy before modifying installs. Complements Win11 legacy-compat tooling such as [[legacy-game-launcher]] and cross-platform library advisors such as [[mac-game-library-advisor]]. (source: wiki/sources/descriptions/iamnotoneself__GameApiDetector.md)

## Links

- Repo: https://github.com/iamnotoneself/GameApiDetector [Windows Rust utility that scans local game libraries and running processes to detect DXGI/Vulkan/OpenGL usage and manage DXVK installs]

## Related

[[legacy-game-launcher]] · [[mac-game-library-advisor]] · [[dxwrapper]] · [[ffnx]] · [[overviews/graphics-api]] · [[overviews/game-hacking]] · [[frame-observation-boundary]]