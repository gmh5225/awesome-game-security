---
title: ModernWarfare2-Cpp-External
kind: entity
topics: [game-hacking, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/Ckateowm__ModernWarfare2-Cpp-External.md
updated: 2026-08-27
confidence: medium
---

# ModernWarfare2-Cpp-External

**ModernWarfare2-Cpp-External** (Ckateowm/ModernWarfare2-Cpp-External) is a C++ **internal cheat DLL** for **Call of Duty: Modern Warfare II**. Despite the repo name, it injects in-process, hooks the game's **DirectX 11/12 swap-chain Present** path via **Kiero**, and renders an **ImGui** overlay for ESP (boxes, skeletons, names, distance, visibility), aimbot (bone selection, velocity prediction, FOV, smoothing), and misc features (no recoil, proximity warning). **MinHook** handles API interception; separate offset paths cover **Battle.net** and **Steam** clients. Evasion-oriented techniques include lazy imports, XOR string obfuscation, and direct syscalls for input simulation. Aimed at game security researchers studying in-process cheat architecture, memory-based game SDK usage, and anti-cheat bypass methods. (source: wiki/sources/descriptions/Ckateowm__ModernWarfare2-Cpp-External.md)

Sits in the COD MWII in-process lane beside [[warzone-internal]], [[modern-warfare-warzone-cheat]], and [[warzone-mw-internal]] as a D3D11/12 Kiero + MinHook internal with dual-client offset handling and explicit evasion tradecraft.

## Feature modules

| Module | Role |
|--------|------|
| ESP | Boxes, skeletons, names, distance, visibility checks |
| Aimbot | Bone selection, velocity prediction, FOV targeting, smoothing |
| Misc | No recoil, proximity warning |
| Present hook | Kiero swap-chain hook; ImGui overlay (D3D11/12) |
| Evasion | Lazy imports, XOR strings, direct syscalls for input |

## Links

- Repo: https://github.com/ckateowm/modernwarfare2-cpp-external

## Related

[[warzone-internal]] · [[modern-warfare-warzone-cheat]] · [[warzone-mw-internal]] · [[kiero]] · [[ntminhook]] · [[present-hook]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
