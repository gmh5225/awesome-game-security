---
title: Chess Sentinel
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/prob1st__chess-sentinel.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: high
---

# Chess Sentinel

**Chess Sentinel** (prob1st/chess-sentinel) is an open-source **Chrome Manifest V3** extension that estimates real-time opponent cheat probability on **Chess.com** and shows results in a Shadow DOM HUD and inline username badge. Built in strict TypeScript, it fuses six public forensic signals through a **Bayesian scoring engine**, all sourced from Chess.com’s read-only **Published-Data API**. Processing stays entirely local with no telemetry or move assistance—suited to fair-play monitoring, smurf detection, and lightweight anti-cheat research on **historical public stats**, not live board evaluation. (source: wiki/sources/descriptions/prob1st__chess-sentinel.md)

README category: Anti Cheat / Open Source Anti Cheat System.

## Forensic signals

The scoring engine combines: recent **win-rate anomalies**; **CAPS2** accuracy versus Elo bands; archived-PGN **`[%clk]` move-pacing** (metronome timing); **rating surge velocity**; and **account trust** indicators. Clock parsing flags robotic move timing and suspected **mid-game engine toggles** even when Chess.com **Game Review** data is absent. (source: wiki/sources/descriptions/prob1st__chess-sentinel.md)

## Operations

Optional **watchlists** track flagged opponents for Chess.com **fair-play account closures**. Outputs are triage hints for human review—complementing federation arbiter platforms such as [[sentinel-anticheat-chess]] and Lichess ML baselines such as [[chess-anti-cheat]], not substitute platform rulings. (source: wiki/sources/descriptions/prob1st__chess-sentinel.md)

## Positioning

Browser-side fair-play HUD on Chess.com—adjacent to [[gomoku-anti-cheat-detector]] for other board sites and server-side stacks such as [[chessking]].

## Links

- Repo: https://github.com/prob1st/chess-sentinel

## Related

[[overviews/anti-cheat]] · [[sentinel-anticheat-chess]] · [[chessking]] · [[chess-anti-cheat]] · [[gomoku-anti-cheat-detector]] · [[ai-aimbot-detection]] · [[research-rigor]]
