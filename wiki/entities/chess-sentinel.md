---
title: Chess Sentinel
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/prob1st__chess-sentinel.md
  - wiki/sources/README-categories.md
updated: 2026-10-24
confidence: medium
---

# Chess Sentinel

**Chess Sentinel** (prob1st/chess-sentinel) is an open-source **Chrome Manifest V3** extension that estimates real-time opponent cheat probability on **Chess.com** and shows results in a Shadow DOM HUD and inline username badge. Built in strict TypeScript, it fuses six public forensic signals through a **Bayesian scoring engine**: recent win-rate anomalies, CAPS2 accuracy versus Elo bands, PGN `[%clk]` move-pacing (metronome timing), rating surge velocity, and account trust indicators—all from Chess.com’s read-only Published-Data API. Processing stays entirely local with no telemetry or move assistance. (source: wiki/sources/descriptions/prob1st__chess-sentinel.md)

README category: Anti Cheat / Open Source Anti Cheat System.

## Positioning

Complements server-side chess platforms such as [[chessking]] and federation post-game review stacks such as [[sentinel-anticheat-chess]] with a **browser-side fair-play HUD** for online smurf/engine-use triage on public stats—adjacent to [[gomoku-anti-cheat-detector]] for other board sites and demo ML stacks such as [[chess-anti-cheat]].

## Links

- Repo: https://github.com/prob1st/chess-sentinel

## Related

[[overviews/anti-cheat]] · [[sentinel-anticheat-chess]] · [[chessking]] · [[chess-anti-cheat]] · [[gomoku-anti-cheat-detector]] · [[ai-aimbot-detection]] · [[research-rigor]]
