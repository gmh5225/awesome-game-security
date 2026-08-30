---
title: d3doverlay-nvidia-hijack
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/Brattlof__D3DOverlay-Nvidia-Hijack.md
updated: 2026-08-30
confidence: medium
---

# d3doverlay-nvidia-hijack

**D3DOverlay-Nvidia-Hijack** (Brattlof) is a **Direct3D9 overlay framework** that renders **Dear ImGui** content through the **NVIDIA GeForce Overlay** window. The C++ implementation locates the existing overlay HWND, configures **transparent click-through** behavior, and drives a **per-frame render callback**. Helper drawing primitives cover text, rectangles, and circles on top of the target display surface. Mainly used in **external game tooling** that needs a reusable overlay layer with minimal custom window management. (source: wiki/sources/descriptions/Brattlof__D3DOverlay-Nvidia-Hijack.md)

Sits in the third-party **NVIDIA GeForce Experience overlay hijack** lane beside DX11 samples such as [[nvidia-overlay-hijack]], [[nvidia-overlay]], and [[nvidia-overlay-renderer]]—reusing the vendor overlay surface instead of spawning a separate transparent HWND. Same author (Brattlof) also maintains kernel mapper fork [[kdmapper-1909]].

## Architecture highlights

| Component | Role |
|-----------|------|
| Direct3D9 | Overlay draw path through GeForce overlay window |
| Dear ImGui | Menu and debug UI on hijacked surface |
| Overlay HWND discovery | Attach to existing NVIDIA overlay window |
| Click-through | Transparent input passthrough to underlying game |
| Per-frame callback | Continuous render loop for external tooling |
| Draw helpers | Text, rectangles, circles on display surface |

See [[present-hook]] for in-process Present interception and [[direct3d9-overlay]] for DX9 proxy-DLL overlay patterns without third-party hijack.

## Links

- Repo: https://github.com/Brattlof/D3DOverlay-Nvidia-Hijack

## Related

[[overviews/graphics-api]] · [[overviews/game-hacking]] · [[present-hook]] · [[imgui]] · [[nvidia-overlay-hijack]] · [[nvidia-overlay]] · [[nvidia-overlay-renderer]] · [[direct3d9-overlay]] · [[d3dhook-imgui]] · [[kdmapper-1909]]
