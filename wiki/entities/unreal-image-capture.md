---
title: UnrealImageCapture
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/TimmHess__UnrealImageCapture.md
updated: 2026-08-20
confidence: medium
---

# UnrealImageCapture

Tutorial repository demonstrating **Unreal Engine image capture to disk** for machine-learning and computer-vision workflows. Uses Unreal C++ to perform high-FPS frame capture without blocking the render or main game threads. Covers synchronized RGB output, segmentation masks, and depth capture, with configuration guidance for output formats and engine build dependencies. Primary use case: generating annotated synthetic datasets from UE scenes for CV and simulation research—not a cheat, dumper, or anti-cheat artifact. (source: wiki/sources/descriptions/TimmHess__UnrealImageCapture.md)

Complements external D3D12 hook segmentation tools (e.g. segcap on shipping UE titles) by exporting masks and depth from **inside** the engine render path. Useful for game developers, graphics researchers, and ML practitioners studying UE render-output surfaces beside [[unreal-source-explained]] architecture walkthroughs and [[present-hook]] external capture pipelines.

## Links

- Repo: https://github.com/TimmHess/UnrealImageCapture (README: tutorial on capturing images with semantic annotation from Unreal Engine to disk)

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[unreal-source-explained]] · [[unreal-engine-guide]] · [[obs-game-capture]] · [[present-hook]]
