---
title: Crosshair Z
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/Nn1ff__crosshair-z.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: high
---

# Crosshair Z

Lightweight **Windows Electron** desktop app that draws a customizable **crosshair** in a transparent, always-on-top overlay for **borderless or windowed** games. Built with JavaScript; uses **koffi** native bindings where low-level mouse input is needed (for example firing spread animation). Ships as a **portable offline** executable with minimal runtime dependencies.

## Features

Pixel-grid designer (lines, outlines, center dots, circles, image layers), firing spread animation, per-crosshair hotkeys, share codes, and import of locally saved **Crosshair X** profiles. (source: wiki/sources/descriptions/Nn1ff__crosshair-z.md)

## Security posture

Deliberately avoids **DLL injection** and in-game hooks—only a plain top-level **click-through** window—positioned as an offline-first alternative to heavier crosshair tools while targeting compatibility with typical anti-cheat expectations (separate-process visual aid, no game memory reads). Apply [[frame-observation-boundary]] when comparing this lane to Present hooks or in-process overlays. (source: wiki/sources/descriptions/Nn1ff__crosshair-z.md)

## Links

- Repo: https://github.com/Nn1ff/crosshair-z

## Related

[[imgui-external-overlay]] · [[imoverlay-dx11]] · [[borderless-gaming]] · [[present-hook]] · [[frame-observation-boundary]] · [[csgocrosshair]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
