---
title: Asdf Overlay
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/storycraft__asdf-overlay.md
updated: 2026-08-08
confidence: medium
---

# Asdf Overlay

High-performance Windows overlay library (primarily Rust) for rendering in-game UI inside arbitrary target processes. Injects an overlay DLL that hooks DirectX 9, 11, and 12, OpenGL, and Vulkan swap chains via Microsoft Detours; host clients in Rust or Node.js/TypeScript communicate over named-pipe IPC. Supports shared-texture surface rendering, cursor management, and input capture or blocking, with demos including an Electron-based in-game browser and standalone Rust samples—aimed at overlay developers and game-security researchers studying process injection, graphics API hooking, and input interception. (source: wiki/sources/descriptions/storycraft__asdf-overlay.md)

## Links

- Repo: https://github.com/storycraft/asdf-overlay

## Related

[[present-hook]] · [[goverlay]] · [[hydrahook]] · [[imgui]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
