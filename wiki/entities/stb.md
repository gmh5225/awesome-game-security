---
title: stb
kind: entity
topics: [graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/nothings__stb.md
updated: 2026-07-27
confidence: medium
---

# stb

Collection of single-file public-domain C libraries for game developers and graphics programmers. Notable headers include stb_image (JPEG/PNG/BMP/GIF load), stb_truetype (TrueType rasterization), stb_vorbis (Ogg Vorbis decode), and stb_image_write (image write). Each library is a drop-in header with no dependencies, aimed at lightweight embedded and gamedev utility use. (source: wiki/sources/descriptions/nothings__stb.md)

Sits in the README Image Codec lane as the canonical single-header codec/font/audio utility set—upstream of soft-raster helpers such as [[olive-c]] and glTF texture paths that depend on stb_image (e.g. [[tinygltf]]), not a GPU Present hook or cheat overlay.

## Links

- Repo: https://github.com/nothings/stb

## Related

[[overviews/graphics-api]] · [[overviews/game-engine]] · [[libjpeg-turbo]] · [[olive-c]] · [[kit]] · [[tinygltf]] · [[present-hook]]
