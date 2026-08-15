---
title: nvidia-overlay-renderer
kind: entity
topics: [graphics-api, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/es3n1n__nvidia-overlay-renderer.md
updated: 2026-08-15
confidence: low
---

# nvidia-overlay-renderer

Windows overlay renderer that hijacks NVIDIA GeForce Experience's in-game overlay window—locating the overlay HWND, obtaining its rendering context, and drawing Dear ImGui menus or ESP through the existing trusted overlay surface instead of creating new overlay windows that anti-cheat may flag. Aimed at game security researchers studying overlay hijacking and anti-cheat overlay-detection bypass; sits beside [[nvidia-overlay-hijack]], [[nvidia-overlay]], [[mwclap]], [[discord-overlay-hook]], and [[steam-overlay-x64]] in the third-party overlay hijack lane. (source: wiki/sources/descriptions/es3n1n__nvidia-overlay-renderer.md)

## Links

- Repo: https://github.com/es3n1n/nvidia-overlay-renderer

## Related

[[overviews/graphics-api]] · [[overviews/game-hacking]] · [[present-hook]] · [[imgui]] · [[nvidia-overlay-hijack]] · [[nvidia-overlay]] · [[discord-overlay-hook]] · [[winbo]]
