---
title: Wiz3D
kind: entity
topics: [graphics-api]
sources:
  - wiki/sources/descriptions/effcol__wiz3D.md
  - wiki/sources/README-categories.md
updated: 2026-10-29
confidence: medium
---

# Wiz3D

Windows stereoscopic 3D driver stack that wraps and intercepts game graphics APIs so flat DirectX, OpenGL, and Vulkan titles can render separate left- and right-eye views for 3D displays and glasses. Ships vendor proxy DLLs, vtable hooks, and D3D9 through D3D12 and DXGI wrapper layers with shader analysis, patching, and per-game hook profiles; integrates NVIDIA 3D Vision–style direct mode, iZ3D shutter hardware, and AMD HD3D-related proxies. C++ core with a C# control center, diagnostics, installer components, and automated test packs—useful for studying swap-chain/device proxying and shader-level interception surfaces that anti-cheat and graphics-integrity work often has to detect. (source: wiki/sources/descriptions/effcol__wiz3D.md)

## Mechanism

- **Proxy DLL / wrapper layers:** intercept D3D7–12, DXGI, and OpenGL exports with per-title profiles.
- **Stereo injection:** dual-view rendering path for shutter glasses and 3D displays (iZ3D lineage).

## Links

- Repo: https://github.com/effcol/wiz3D

## Related

[[present-hook]] · [[dxwrapper]] · [[opengl32-enhancer]] · [[draw-call-hook]] · [[frame-observation-boundary]] · [[overviews/graphics-api]]
