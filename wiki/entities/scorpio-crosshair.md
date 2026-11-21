---
title: Scorpio Crosshair
kind: entity
topics: [game-hacking, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/Deikus-LXXVII__Scorpio-Crosshair.md
updated: 2026-11-21
confidence: medium
---

# Scorpio Crosshair

**Scorpio Crosshair** (Deikus-LXXVII) is a free **desktop crosshair overlay** for PC games on **Windows and Linux**. It draws a **CS2-style reticle** in a separate **transparent, click-through** window above the game, using **Rust** with **Tauri 2** and an on-demand HTML, CSS, and JavaScript settings UI. Platform-specific overlay and window-focus logic keep the stack outside game processes. (source: wiki/sources/descriptions/Deikus-LXXVII__Scorpio-Crosshair.md)

## Features

CS2 share codes, per-game profiles, launcher-based game detection, raw-input aim hiding, global shortcuts, and optional **OBS browser-source** output. (source: wiki/sources/descriptions/Deikus-LXXVII__Scorpio-Crosshair.md)

## Security posture

Deliberately avoids **process handles**, **injection**, **hooks**, **memory reads**, and **synthetic input** so anti-cheat systems are less likely to flag the tool—an external visual aid that stays outside the game and AC **trust boundary**. Suits players who want a consistent crosshair and developers researching overlay design without touching the protected process. Compare [[crosshair-z]], [[iris-overlay]], and [[perfoverlay-supreme]]; apply [[frame-observation-boundary]] when triaging transparent HWND overlays. (source: wiki/sources/descriptions/Deikus-LXXVII__Scorpio-Crosshair.md)

## Links

- Repo: https://github.com/Deikus-LXXVII/Scorpio-Crosshair

## Related

[[crosshair-z]] · [[iris-overlay]] · [[perfoverlay-supreme]] · [[frame-observation-boundary]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]