---
title: Screenshot Detection Bypass
kind: entity
topics: [anti-cheat, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/Mes2d__Screenshot-Detection-Bypass.md
updated: 2026-08-23
confidence: medium
---

# Screenshot Detection Bypass

C++ **proof of concept** from Mes2d that hooks **`BitBlt` in gdi32** so anti-cheat screenshot pipelines receive a **pre-stored clean frame** instead of the live overlay-modified game client area. Uses a simple **class-based hook** and settings structure with readable call flow from the original function to the hooked handler. Primary use case is **educational anti-cheat research** on screenshot-detection evasion and GDI capture-hook behavior. README **BitBlt** tag. (source: wiki/sources/descriptions/Mes2d__Screenshot-Detection-Bypass.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| gdi32 `BitBlt` hook | Intercepts AC GDI screenshot reads at the Windows graphics API layer |
| Clean-frame substitution | Returns stored unmodified capture instead of current composited client pixels |
| Class-based hook + settings | Documents original→handler call flow for study and extension |

Contrasts with **frame suppression** (skip overlay draw on detected capture) and **display-affinity** evasion—this PoC **feeds alternate pixel data** at the GDI boundary. Pair with [[screenshot]] and [[getpixel-vs-bitblt-getdibits]] for BitBlt capture fundamentals, [[not-an-overlay]] for external GDI rendering tradeoffs, and [[anti-screenshot-capture]] for broader AC capture vs evasion paths.

## Links

- Repo: https://github.com/Mes2d/Screenshot-Detection-Bypass

## Related

[[overviews/anti-cheat]] · [[overviews/graphics-api]] · [[anti-screenshot-capture]] · [[screenshot]] · [[getpixel-vs-bitblt-getdibits]] · [[not-an-overlay]] · [[present-hook]] · [[eac-overlay]]
