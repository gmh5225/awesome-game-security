---
title: HuntOpenHighlights
kind: entity
topics: [anti-cheat, graphics-api, game-hacking]
sources:
  - wiki/sources/descriptions/Mlovo__HuntOpenHighlights.md
updated: 2026-10-29
confidence: medium
---

# HuntOpenHighlights (HuntReplay Studio)

Standalone **Hunt: Showdown 1896** clip recorder that auto-saves kills, deaths, and downs from the game’s official **Highlights SDK** events. Listens on the standard **NVIDIA MessageBus** IPC pipe with Authenticode-verified MessageBus integration—no process injection, hooks, or input emulation—so it stays compatible with **Easy Anti-Cheat**. Video uses **Windows Graphics Capture** with hardware encoding (NVENC, AMD AMF, Intel QSV, or x264); clips are cut from an in-memory ring buffer with keyframe-accurate trimming without re-encoding on save. Stack: .NET 8 WPF desktop UI, native C++ media layer on FFmpeg, Protocol Buffers for bus messaging; ships as a portable single executable with built-in gallery and player. Useful for players who want automatic highlights and for researchers studying legitimate, anti-cheat-safe game-event and overlay IPC on Windows. (source: wiki/sources/descriptions/Mlovo__HuntOpenHighlights.md)

## Architecture

| Layer | Role |
|-------|------|
| Event intake | Highlights SDK events via NVIDIA MessageBus IPC (Authenticode-verified client) |
| Capture | Windows Graphics Capture + NVENC / AMF / QSV / x264 |
| Clip pipeline | In-memory ring buffer; keyframe-accurate trim without re-encode on export |
| UI / packaging | .NET 8 WPF + FFmpeg native layer; portable single EXE, gallery + player |

## Links

- Repo: https://github.com/Mlovo/HuntOpenHighlights

## Related

[[capture-engine]] · [[obs-game-capture]] · [[easy-anti-cheat]] · [[lanternlight]] · [[overviews/anti-cheat]] · [[overviews/graphics-api]] · [[overviews/game-hacking]]
