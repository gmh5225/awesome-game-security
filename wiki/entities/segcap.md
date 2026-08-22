---
title: segcap
kind: entity
topics: [graphics-api, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/Qervas__segcap.md
updated: 2026-08-22
confidence: medium
---

# segcap

Windows research tool that injects into live **Direct3D 12** games and captures per-pixel **object-ID segmentation masks** aligned frame-for-frame with the rendered RGB image. Implemented in C++ with Python orchestration; uses **MinHook** to intercept D3D12 command submission and introspects **Unreal Engine 4 and 5** at runtime, assigning stable labels through the engine's **CustomDepth** pass instead of rebuilding renderer pipeline state. Runs fully automated capture sessions on shipping retail titles—driving menus with a virtual gamepad—and exports masks, RGB frames, and JSON sidecars for verification and analysis. Targets reverse engineers and game-security researchers who need ground-truth segmentation and deep visibility into closed-source UE rendering without engine source or symbols. (source: wiki/sources/descriptions/Qervas__segcap.md)

Complements in-engine capture tutorials such as [[unreal-image-capture]] by extracting segmentation from **external** D3D12 hooks on retail UE4/UE5 builds. Sits beside D3D12 interceptors such as [[shader-injector]] in the DirectX hook lane, but focuses on object-ID mask export rather than pixel-shader replacement.

## Links

- Repo: https://github.com/Qervas/segcap (D3D12 hooking tool extracting per-pixel object-ID segmentation masks from shipping UE4/UE5 games without engine source or modification)

## Related

[[draw-call-hook]] · [[present-hook]] · [[shader-injector]] · [[unreal-image-capture]] · [[capture-engine]] · [[overviews/graphics-api]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
