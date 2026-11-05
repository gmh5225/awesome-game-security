---
title: SCVK
kind: entity
topics: [graphics-api, reverse-engineering, game-engine]
sources:
  - wiki/sources/descriptions/aspctt__scvk.md
updated: 2026-11-05
confidence: medium
---

# SCVK

Native Vulkan renderer for *SimCity 4*, delivered as a 32-bit DLL loaded through the game’s GZCOM graphics-driver plugin slot. It replaces the stock DirectX 7 and incomplete OpenGL drivers rather than wrapping them: C++ plus GLSL compiled to SPIR-V, emulating the fixed-function `cIGZGDriver` API with cached Vulkan pipelines and ubershaders instead of a thin API translator.

Capabilities include terrain and UI rendering, day/night lighting, optional live True3D shadows, ReShade add-on integration with correct depth, built-in FPS and presentation tuning, and exported frame callbacks for third-party overlays. Targets players and mod authors on Windows and Linux (via Wine) who want modern GPU performance; the project is a reference for reverse-engineering a legacy commercial game’s rendering and plugin interfaces for community-driven engine replacement. (source: wiki/sources/descriptions/aspctt__scvk.md)

## Links

- Repo: https://github.com/aspctt/scvk

## Related

[[dxwrapper]] · [[opencmr2]] · [[reshade]] · [[present-hook]] · [[vulkan-hook]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
