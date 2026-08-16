---
title: D2D Overlay
kind: entity
topics: [graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/coltonon__D2DOverlay.md
updated: 2026-08-16
confidence: medium
---

# D2D Overlay

Header-only **Direct2D** external overlay library (coltonon) aimed at simplicity and performance. **`DirectOverlay.h`** contains the full API documentation. Creates transparent layered Win32 windows and draws with **Direct2D** over a target game HWND—no in-process graphics hook. (source: wiki/sources/descriptions/coltonon__D2DOverlay.md)

Useful for game security researchers and reverse engineers studying offensive **external overlay** techniques in the cheat / overlay lane. Sits beside GDI externals such as [[external-esp-hack-assaultcube]] and GPU-composited frameworks such as [[imoverlay-dx11]], without requiring [[present-hook]] injection.

Downstream cheat samples such as [[pubg-lite-esp]] (gmh5225; RPM + UE4 offsets + D2D ESP on a transparent HWND) illustrate typical adoption.

## Links

- Repo: https://github.com/coltonon/D2DOverlay

## Related

[[external-esp-hack-assaultcube]] · [[imoverlay-dx11]] · [[pubg-lite-esp]] · [[present-hook]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
