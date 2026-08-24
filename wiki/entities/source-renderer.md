---
title: SourceRenderer
kind: entity
topics: [game-engine, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/K0bin__SourceRenderer.md
updated: 2026-08-24
confidence: medium
---

# SourceRenderer

**SourceRenderer** (K0bin) is a Rust toy game engine with a custom low-level graphics stack built to load and render Valve **Source-engine** content alongside modern assets. It reuses large parts of **Bevy** for engine infrastructure while replacing windowing, asset management, and rendering with its own implementations. (source: wiki/sources/descriptions/K0bin__SourceRenderer.md)

The graphics layer targets **Vulkan 1.3** as the primary backend, with **Metal** and **WebGPU** support, and includes bindless resources, ray tracing where available, multi-draw indirect, occlusion queries, and pipelined multi-threaded rendering with PBR, SSAO, TAA, and related effects. An async asset manager loads **glTF** plus Source formats—BSP maps, VPK packs, VMT/VTF materials, and MDL models, including CS:GO-related loaders.

Mainly useful for graphics and reverse-engineering work around Source maps and assets, and for experimenting with modern GPU-driven rendering across desktop, web, and mobile—not a cheat scaffold, but a format-validation and render-pipeline study surface beside official SDK trees and netvar tooling.

## Links

- Repo: https://github.com/K0bin/SourceRenderer (README tag: [Rust toy engine/renderer with Valve Source format loaders (bsp/mdl/vpk/vtf) and Vulkan/Metal/WebGPU backends])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[source-netvars]] · [[source-sdk-2013]] · [[source-engine]] · [[kisak-strike]] · [[gltf]] · [[tinygltf]] · [[ursus]] · [[nightshade]] · [[awesome-game-file-format-reversing]]
