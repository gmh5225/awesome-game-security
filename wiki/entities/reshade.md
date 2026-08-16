---
title: ReShade
kind: entity
topics: [graphics-api]
sources:
  - wiki/sources/descriptions/crosire__reshade.md
updated: 2026-08-16
confidence: medium
---

# ReShade

Generic cross-API post-processing injector for games and video software. Hooks the graphics present/swap path to expose automated access to frame color and depth buffers, then runs user effects through the **ReShade FX** shader language (ambient occlusion, depth of field, color correction, and similar post-processing). Targets graphics programmers and rendering researchers in the Renderer / post-processing lane—not a cheat overlay framework, but shares the same in-process inject and Present-hook surface as overlay tooling. (source: wiki/sources/descriptions/crosire__reshade.md)

## Links

- Repo: https://github.com/crosire/reshade

## Related

[[present-hook]] · [[draw-call-hook]] · [[shader-injector]] · [[swapchain-bottleneck]] · [[kiero2]] · [[overviews/graphics-api]]
