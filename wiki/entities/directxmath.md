---
title: DirectXMath
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/microsoft__DirectXMath.md
updated: 2026-07-30
confidence: medium
---

# DirectXMath

Microsoft's all-inline SIMD C++ linear algebra library for Windows and Xbox game code (README `Mathematics`). Provides SSE/SSE2/AVX/AVX2 and ARM-NEON optimized vectors, matrices, quaternions, and collision primitives (`BoundingBox`, `BoundingSphere`, `BoundingFrustum`), with optional F16C half-float, FMA3/FMA4, spherical harmonics (`SHMath`), and DSP helpers (`XDSP`). Ships as header-only inlines—typical building block for DirectX render math, view/projection transforms, and frustum tests upstream of [[present-hook]] overlays and [[world-to-screen]] ESP math. Complements higher-level cheat-oriented frameworks such as [[omath]] and realtime libs such as [[rtm]]. (source: wiki/sources/descriptions/microsoft__DirectXMath.md)

## Links

- Repo: https://github.com/microsoft/DirectXMath

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[world-to-screen]] · [[omath]] · [[rtm]] · [[hw3d]] · [[d3d12renderer]]
