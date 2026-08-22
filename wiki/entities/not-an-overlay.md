---
title: NotAnOverlay
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/PierreCiholas__NotAnOverlay.md
updated: 2026-08-22
confidence: medium
---

# NotAnOverlay

Windows **proof of concept** from PierreCiholas that renders a game view in a **regular window** instead of a classic transparent always-on-top overlay. Written in **C++** with Win32 and **GDI**, it uses `BitBlt` and `StretchBlt` to clone screen regions and draw continuously. The accompanying explanation focuses on anti-cheat visibility of traditional external overlays and why a less suspicious window model may help experimentation. Aimed at game security researchers studying **external ESP rendering strategies** and detection tradeoffs. README **Duplicating with GDI** tag. (source: wiki/sources/descriptions/PierreCiholas__NotAnOverlay.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| Regular Win32 window | Avoids `WS_EX_LAYERED` / always-on-top overlay heuristics |
| GDI `BitBlt` / `StretchBlt` | Screen-region duplication into the display window |
| Continuous redraw loop | Keeps cloned game view synchronized |

Contrasts with transparent layered GDI externals such as [[cs2external]] and [[external-esp-hack-assaultcube]], Direct2D layered libraries such as [[d2d-overlay]], and overlay-hijack PoCs such as [[window-hijack-overlay]]. Pair with [[anti-screenshot-capture]] for how AC screenshot and overlay-enumeration surfaces differ from classic transparent HWNDs.

## Links

- Repo: https://github.com/PierreCiholas/NotAnOverlay

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[external-esp-hack-assaultcube]] · [[cs2external]] · [[d2d-overlay]] · [[window-hijack-overlay]] · [[anti-screenshot-capture]] · [[world-to-screen]]
