---
title: winbo
kind: entity
topics: [anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/noahware__winbo.md
updated: 2026-07-27
confidence: medium
---

# winbo

Windows C++ tool for detecting overlay-style window hijacking via dxgkrnl ETW and GDI handle-table scanning. Parses Present-related ETW events to compare the calling process PID against the window owner PID, flagging unauthorized cross-process DirectX/OpenGL rendering; for GDI paths, walks the shared GDI handle table for DCs whose owner differs from the target window. Common-parent process pairs are whitelisted for legitimate multi-process window sharing. Aimed at anti-cheat and defensive researchers studying overlay detection. (source: wiki/sources/descriptions/noahware__winbo.md)

## Links

- Repo: https://github.com/noahware/winbo

## Related

[[present-hook]] · [[present-hook-detection]] · [[eac-overlay]] · [[window-hijack]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
