---
title: Chess Assist (chess-hacks)
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/ThatKidGlitchy__chess-hacks.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# Chess Assist (chess-hacks)

**Chess Assist** (ThatKidGlitchy/chess-hacks) is a client-side browser toolkit that injects **Stockfish** analysis and automation into live **chess.com** games. Implemented in JavaScript as userscripts, bookmarklets, and an optional Chrome extension (separate desktop and mobile Safari builds), it studies how web chess clients can be augmented during play and how heuristic engine-correlation metrics approximate fair-play monitoring. (source: wiki/sources/descriptions/ThatKidGlitchy__chess-hacks.md)

README category: **Game:Chess** / Cheat.

## Automation and assist

Embedded **Stockfish** can auto-play engine moves with configurable delay and depth, overlay **best-move** and **opponent-prediction** hints, and customize the board UI; preferences persist in **local storage**. Delivery spans Tampermonkey-style userscripts, bookmarklets, an optional Chrome extension, and mobile Safari builds. (source: wiki/sources/descriptions/ThatKidGlitchy__chess-hacks.md)

## Heuristic detection panel

A built-in panel tracks **centipawn loss**, **accuracy**, **best-move rate**, and a **suspicion gauge** for the user or opponent, with optional **full-game reanalysis**—mirroring engine-correlation signals used in fair-play research without server-side telemetry. (source: wiki/sources/descriptions/ThatKidGlitchy__chess-hacks.md)

## Positioning

Offensive **browser-side** chess.com augmentation lane—contrasts with defensive Published-Data tooling such as [[chess-sentinel]], ML baselines such as [[chess-anti-cheat]], and arbiter platforms such as [[sentinel-anticheat-chess]] on [[overviews/anti-cheat]] and [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/thatkidglitchy/chess-hacks

## Related

[[chess-sentinel]] · [[sentinel-anticheat-chess]] · [[chess-anti-cheat]] · [[stockfish]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[ai-aimbot-detection]]
