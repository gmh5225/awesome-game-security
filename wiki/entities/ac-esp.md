---
title: ac-esp
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/jerryshell__ac-esp.md
  - wiki/sources/README-categories.md
updated: 2026-10-30
confidence: medium
---

# ac-esp

Rust `cdylib` injectable DLL that draws a Direct2D ESP overlay on AssaultCube 1.3.0.2 (32-bit): reads entity list, health, and view matrix from fixed in-process offsets, projects head/foot positions with [[world-to-screen]] math, and renders bounding boxes in a transparent overlay window aligned to the game HWND. Built for `i686` Windows with the Rust `windows` crate; ships release builds with injection notes; overlay unit tests run separately from live injection. Aimed at reverse engineers and game-security researchers studying fixed-offset entity reads, projection math, and transparent overlay composition on a lightweight open FPS client. (source: wiki/sources/descriptions/jerryshell__ac-esp.md)

## Links

- Repo: https://github.com/jerryshell/ac-esp

## Related

[[simple-ac-internal-cheat]] · [[assault-cube-cheat]] · [[external-esp-hack-assaultcube]] · [[world-to-screen]] · [[overviews/game-hacking]] · [[overviews/graphics-api]]
