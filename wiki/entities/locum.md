---
title: locum
kind: entity
topics: [graphics-api, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Kalmarv__locum.md
updated: 2026-11-03
confidence: medium
---

# locum

Direct3D 11 frame capture and inspection tool that records every draw and dispatch in a frame—shaders, constants, textures, buffers, pipeline state, and render targets—into a single SQLite database for browse, SQL query, live edits, and offline replay. Deployment uses companion DXGI and D3D11 shim DLLs beside a 64-bit game executable (RenderDoc-style analysis without process injection). The Rust core handles hooking, capture storage, and offline replay with bit-for-bit render-target verification; a Bun-powered local web viewer and `locum-cli` expose draw lists, shader disassembly, resource export, SQL access, live draw overrides, and capture diffs. Resource tracing links GPU assets to on-disk files and game memory; replay supports skipping draws or swapping shaders for experiments. Targets Windows graphics debugging, rendering reverse engineering, and security research on D3D11 titles—not live online games protected by anti-cheat. (source: wiki/sources/descriptions/Kalmarv__locum.md)

## Audience

Graphics and security researchers who need queryable, replayable D3D11 frame evidence (SQLite + CLI/web UI) from proxy-DLL deployment rather than injected frame debuggers—especially offline or AC-free lab titles. (source: wiki/sources/descriptions/Kalmarv__locum.md)

## Links

- Repo: https://github.com/Kalmarv/locum

## Related

[[overviews/graphics-api]] · [[overviews/reverse-engineering]] · [[frame-observation-boundary]] · [[draw-call-hook]] · [[rdc-cli]] · [[gpu-inspector]] · [[segcap]]
