---
title: intro-to-dx11-revisited
kind: entity
topics: [graphics-api, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/yottaawesome__intro-to-dx11-revisited.md
updated: 2026-07-30
confidence: medium
---

# intro-to-dx11-revisited

Modernized reimplementation of Frank Luna's *Introduction to 3D Game Programming with DirectX 11* sample code—updated for current toolchains while keeping the book's teaching progression. Modern C++ with inline modules; drops deprecated D3DX11 and Effects11 in favor of standard Direct3D 11 APIs, a custom ComPtr wrapper, and explicit HLSL compilation via `D3DReadFileToBlob`. Working demos cover DirectXMath fundamentals, Direct3D initialization, geometry rendering, and lighting, with ongoing FX→standard HLSL conversion. Aimed at developers and security researchers who need a clear, up-to-date reference for DX11 rendering pipelines, shader/resource layout, and the low-level graphics structures commonly encountered when analyzing game engines—not Present-hook or overlay tooling. (source: wiki/sources/descriptions/yottaawesome__intro-to-dx11-revisited.md)

Sits in the README DirectX / guide lane beside sibling [[intro-to-dx12-2nd-edition-revisited]] and other educational DX11 samples such as [[hw3d]] and [[dx11-basehook]].

## Links

- Repo: https://github.com/yottaawesome/intro-to-dx11-revisited

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[intro-to-dx12-2nd-edition-revisited]] · [[directxmath]] · [[hw3d]] · [[dx11-basehook]] · [[directx11hook]] · [[present-hook]]
