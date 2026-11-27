---
title: X-Hair
kind: entity
topics: [game-hacking, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/ybreakless__x-hair.md
updated: 2026-11-27
confidence: medium
---

# X-Hair

**X-Hair** (ybreakless) is a **cross-platform desktop crosshair overlay** for FPS games. It draws a **transparent, click-through reticle** at screen center via **OS-native overlay windows** on **Windows**, **X11**, and **Wayland**, implemented as a modular **Rust Cargo workspace**. Passive input uses **Windows Raw Input** and **Linux evdev**; an on-demand **egui** studio designs and manages reticles. (source: wiki/sources/descriptions/ybreakless__x-hair.md)

## Features

Built-in tactical presets, **per-game weapon-slot profiles** with ADS and fire behavior, portable share codes, **JSON Schema** validation, PNG and SVG export, and a **GitHub-synced community catalog**. (source: wiki/sources/descriptions/ybreakless__x-hair.md)

## Security posture

Deliberately avoids **game memory reads**, **code injection**, and **graphics API hooks**—only a separate click-through OS window—engineered to stay outside common anti-cheat **detection surfaces**. Targets competitive shooters and researchers studying overlay-based aiming aids without touching the protected process. Compare [[crosshair-z]], [[scorpio-crosshair]], and [[iris-overlay]]; apply [[frame-observation-boundary]] when triaging transparent HWND overlays. (source: wiki/sources/descriptions/ybreakless__x-hair.md)

## Links

- Repo: https://github.com/ybreakless/x-hair

## Related

[[crosshair-z]] · [[scorpio-crosshair]] · [[iris-overlay]] · [[frame-observation-boundary]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]