---
title: GPU Inspector
kind: entity
topics: [graphics-api, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/brendan-duncan__gpu_inspector.md
  - wiki/sources/README-categories.md
updated: 2026-09-19
confidence: medium
---

# GPU Inspector

Cross-platform desktop GPU frame capture and graphics debugger (brendan-duncan; TypeScript/Electron UI + C++ capture layers). Captures and inspects frames from Vulkan, Direct3D 12, Metal, and Android native apps: object inspection, draw state and resources, shader debugging with live editing, validation reporting, pixel history, render graphs, and profiling (pass timings, GPU bottlenecks, overdraw). Supports saved capture files, export of frames to standalone C++ projects, WebGPU capture from major browsers, and an MCP-based Claude Code plugin for automated capture analysis. README **Cheat / Debugging** lane; legitimate frame-debug tooling beside RenderDoc/PIX for rendering-pipeline and shader RE on shipping titles. (source: wiki/sources/descriptions/brendan-duncan__gpu_inspector.md)

## Links

- Repo: https://github.com/brendan-duncan/gpu_inspector

## Related

[[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frame-observation-boundary]] · [[presentmon]] · [[tracy]] · [[draw-call-hook]]
