---
title: Kajiya
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/EmbarkStudios__kajiya.md
updated: 2026-08-25
confidence: medium
---

# Kajiya

Experimental **real-time global illumination** renderer from Embark Studios that targets path-traced quality in dynamic scenes. Engine code is **Rust**; the graphics backend is **Vulkan**; shading uses a large **HLSL** stack for hybrid rasterization, compute, and ray-tracing passes. Features include dynamic GI without prebaked probes, temporal reconstruction, ray-traced shadows and reflections, and a reference path-tracing mode for validation. Primary audience is developers studying modern real-time lighting techniques—not anti-cheat or cheat tooling. (source: wiki/sources/descriptions/EmbarkStudios__kajiya.md)

Sits in the Renderer / real-time GI research lane beside [[strolle]], [[spartan-engine]], and [[source-renderer]] as a Vulkan + RT hybrid lighting study surface.

## Links

- Repo: https://github.com/EmbarkStudios/kajiya (README tag: [Experimental real-time global illumination renderer])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[strolle]] · [[spartan-engine]] · [[source-renderer]] · [[d3d12renderer]] · [[explosion]]
