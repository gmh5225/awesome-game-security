---
title: DWM-DwmDraw
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__DWM-DwmDraw.md
updated: 2026-08-14
confidence: medium
---

# DWM-DwmDraw

Technique for rendering overlays through the **Desktop Window Manager (DWM)** drawing pipeline by hooking **`DwmDraw`** functions. ESP and visual-hack elements are drawn directly through the Windows compositor rather than via a separate overlay HWND or in-game Present hook—aimed at evading screenshot-based detection that captures game backbuffers or external layered windows but may miss compositor-integrated draw paths. (source: wiki/sources/descriptions/gmh5225__DWM-DwmDraw.md)

README category tag: **`[DWM StackWalk]`** — situates the sample beside stack-walk / compositor-hook research in the DWM overlay lane alongside [[dwm-hook]], [[dwmhook]], and [[anti-screenshot-capture]] evasion patterns.

## Links

- Repo: https://github.com/gmh5225/DWM-DwmDraw

## Related

[[dwm-hook]] · [[dwmhook]] · [[present-hook]] · [[anti-screenshot-capture]] · [[disablenvidiascreenshot]] · [[screenshot]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
