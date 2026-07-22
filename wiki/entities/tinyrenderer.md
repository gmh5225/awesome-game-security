---
title: tinyrenderer
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/ssloy__tinyrenderer.md
updated: 2026-07-22
confidence: medium
---

# tinyrenderer

Software 3D renderer in ~500 lines of bare C++ with no third-party graphics libraries. Implements the full pipeline from scratch: Bresenham lines, triangle rasterization, barycentric coordinates, z-buffer, camera, shading, texture / normal / shadow mapping, and ambient occlusion. Course lectures walk OpenGL / Vulkan / Metal / DirectX internals by building each stage step by step—aimed at graphics programmers and game-engine researchers learning software rendering fundamentals. (source: wiki/sources/descriptions/ssloy__tinyrenderer.md)

Sits in the README Renderer lane as an educational CPU 3D pipeline study surface (deeper than 2D soft-raster helpers such as [[olive-c]]), not a GPU Present hook or cheat overlay.

## Links

- Repo: https://github.com/ssloy/tinyrenderer

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[olive-c]] · [[island]] · [[xash-rt]] · [[present-hook]]
