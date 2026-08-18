---
title: raytracing
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/ashawkey__raytracing.md
updated: 2026-08-18
confidence: medium
---

# raytracing

CUDA-accelerated mesh ray-tracing library (ashawkey; README `[RayTracer]`) with BVH acceleration and Python bindings. Core kernels are CUDA/C++; the Python package exposes PyTorch-tensor ray–mesh intersection queries. Includes a renderer example for normal visualization plus camera and ray-generation workflows—useful for graphics, simulation, and vision research needing fast GPU ray queries. Not a Present hook, cheat overlay, or game engine. (source: wiki/sources/descriptions/ashawkey__raytracing.md)

## Links

- Repo: https://github.com/ashawkey/raytracing

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[tinyraytracer]] · [[tinyrenderer]] · [[d3d12renderer]] · [[pbrtbook]] · [[present-hook]]
