---
title: HydraHook
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/nefarius__HydraHook.md
updated: 2026-07-28
confidence: medium
---

# HydraHook

Windows C++ DLL framework that hooks DirectX (9–12) and related APIs to render custom overlays inside foreign game processes. Detects the game’s DirectX version at runtime, exposes a small callback API, and ships a self-contained runtime with Microsoft Detours statically linked; also covers Core Audio and input-related hooks. Supports mid-process inject/eject, a lock-free hot path, and loader-lock-safe shutdown. Sample host DLLs demonstrate ImGui, DirectXTK, and OpenCV overlays—aimed at overlay / API-hook / RE study on owned DirectX titles (caution around anti-cheat). (source: wiki/sources/descriptions/nefarius__HydraHook.md)

## Links

- Repo: https://github.com/nefarius/HydraHook

## Related

[[present-hook]] · [[directxhook]] · [[dx11-basehook]] · [[directx11hook]] · [[imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
