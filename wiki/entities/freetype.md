---
title: FreeType
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/freetype__freetype.md
updated: 2026-08-15
confidence: medium
---

# FreeType

Portable C font rasterization library that renders high-quality glyph images from TrueType, OpenType, CFF, Type 1, and bitmap font formats. Implements bytecode hinting interpretation, anti-aliased rendering, subpixel positioning, and auto-hinting behind a modular architecture with pluggable font drivers. Builds on virtually every platform (including DOS, Amiga, OS/2, and Symbian) via Make, CMake, and Meson. (source: wiki/sources/descriptions/freetype__freetype.md)

Sits in the README **Render fonts** lane as the full-featured upstream for engine UI text, ImGui custom-font loading, and overlay/menu typography—heavier than single-header [[stb]] `stb_truetype`, but with broader format coverage and hinting control.

## Links

- Repo: https://github.com/freetype/freetype

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[stb]] · [[imgui]] · [[paintfe]] · [[olive-c]]
