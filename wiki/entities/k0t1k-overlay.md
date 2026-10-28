---
title: k0t1k Overlay
kind: entity
topics: [game-hacking, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/hhhhhffd___k0t1k-overlay.md
  - wiki/sources/README-categories.md
updated: 2026-10-28
confidence: medium
---

# k0t1k Overlay

**k0t1k-overlay** ([hhhhhffd/_k0t1k-overlay](https://github.com/hhhhhffd/_k0t1k-overlay)) is a **Steam-style in-game overlay** for Minecraft Java Edition: one fat JAR attaches as a **`-javaagent`** instead of registering as a mod. (source: wiki/sources/descriptions/hhhhhffd___k0t1k-overlay.md)

## Hooking model

**Byte Buddy** instruments LWJGL **swap, present, and input** paths so the overlay draws on the finished frame and captures input **without patching Minecraft classes**. Works across vanilla, Fabric, Forge, and NeoForge from roughly **1.8 through current releases** on **OpenGL or Vulkan**, reusing the game’s LWJGL stack for GLSL or SPIR-V rendering.

## Feature surface

Bundled utilities include chat history search, persistent notes, mod listings, performance HUD, optional **JCEF** in-game browsing, GPU-backed replay clips, and related QoL—aimed at players and launcher integrators as much as researchers.

## Research use

Reference for **JVM instrumentation**, **graphics API hooking at the LWJGL boundary**, and **client-side overlay injection** beside attach-based agents such as [[nocturne-client]]—not a sanctioned multiplayer tool.

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]] · [[present-hook]] · [[nocturne-client]] · [[vortex-client]]

## Links

- Repo: https://github.com/hhhhhffd/_k0t1k-overlay
