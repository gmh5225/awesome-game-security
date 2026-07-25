---
title: krnl-gdi-render
kind: entity
topics: [graphics-api, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/r1cky33__krnl-gdi-render.md
updated: 2026-07-25
confidence: medium
---

# krnl-gdi-render

Windows **kernel-mode GDI rendering** framework (C++ WDK) that hooks GDI drawing functions to paint overlay graphics from Ring0. Includes signature scanning, NT kernel utilities, and prebuilt signed driver binaries for deploying kernel-level visual overlays—useful for studying GDI / Dxgkrnl-adjacent render-draw paths that bypass typical user-mode overlay detection. (source: wiki/sources/descriptions/r1cky33__krnl-gdi-render.md)

Adjacent to graphics-kernel buffer hooks such as [[dxgkrnl-hook]], kernel DWM samples such as [[double-callback]], and user-mode [[present-hook]] / overlay surfaces under [[overviews/graphics-api]].

## Links

- Repo: https://github.com/r1cky33/krnl-gdi-render

## Related

[[dxgkrnl-hook]] · [[present-hook]] · [[double-callback]] · [[dwm-hook]] · [[eac-overlay]] · [[overviews/graphics-api]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
