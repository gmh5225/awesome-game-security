---
title: Ursus
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/PrograMistV1__ursus.md
updated: 2026-08-22
confidence: medium
---

# Ursus

Custom **Vulkan** game engine written in **Rust**, organized as a Cargo workspace with a core engine crate, opinionated deferred pipelines, model loaders, and a demo app. Centers on a **render-graph** architecture with automatic barrier tracking, a deferred pipeline (shadows, depth prepass, G-buffer, lighting, post-process, and FSR1 upscaling), and **bindless textures**. Game logic and rendering run on separate threads synchronized through a lock-free triple buffer, with async loading of OBJ/glTF assets, **hecs**-based ECS, and GPU timestamp profiling via **puffin**. Targets Linux and Windows with Vulkan 1.3+, **ash**, and build-time SPIR-V shader compilation. (source: wiki/sources/descriptions/PrograMistV1__ursus.md)

Sits in the Game Engine / source lane—an OSS Rust Vulkan engine for studying modern real-time rendering, render graphs, and engine internals, not a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/PrograMistV1/ursus (README tag: [Rust Vulkan engine with render graph, ECS, asset pipeline, and deferred pipelines])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[oxylus]] · [[cat-annihilation]] · [[lumos]] · [[hazel]] · [[prowl]] · [[ravengine]] · [[island]]
