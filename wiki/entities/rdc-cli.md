---
title: rdc-cli
kind: entity
topics: [graphics-api, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/adriank56793__rdc-cli.md
updated: 2026-10-16
confidence: medium
---

# rdc-cli

Scriptable Python CLI on the RenderDoc replay module that exposes `.rdc` GPU capture files as tab-separated or JSON text streams and a virtual filesystem for terminal inspection. Lists draw calls, disassembles shaders, exports textures and buffers, and supports pixel-level debugging without the RenderDoc GUI. Output pipes into grep, awk, sort, diff, and jq; a long-running daemon avoids reloading captures on every query. CI-oriented assertions, two-frame diffs, local and split remote replay, and Android capture workflows support automated graphics validation. Suited to game security and reverse engineering when researchers need repeatable, scriptable analysis of rendering behavior, shader logic, and frame-to-frame GPU state changes on D3D/Vulkan/OpenGL frames. (source: wiki/sources/descriptions/adriank56793__rdc-cli.md)

## Audience

Graphics and security researchers automating RenderDoc capture analysis in terminals, CI pipelines, or agent workflows rather than manual GUI review. (source: wiki/sources/descriptions/adriank56793__rdc-cli.md)

## Links

- Repo: https://github.com/adriank56793/rdc-cli

## Related

[[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frame-observation-boundary]] · [[gpu-inspector]] · [[capture-engine]] · [[tracy]] · [[presentmon]]
