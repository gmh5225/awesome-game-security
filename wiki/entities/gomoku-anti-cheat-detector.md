---
title: Gomoku Anti-Cheat Detector (Baishen)
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/AODOJUST__gomoku-anti-cheat-detector.md
  - wiki/sources/README-categories.md
updated: 2026-10-03
confidence: medium
---

# Gomoku Anti-Cheat Detector (Baishen)

**Baishen** (AODOJUST/gomoku-anti-cheat-detector) is a **Chrome and Edge browser extension** that flags suspected AI-assisted play on online Gomoku at gomoku.com and papergames.io. During spectating or play it records move sequences; after each game it **locally replays** them with the Rapfi WebAssembly engine and optional KataGomo HTTP or custom Rapfi weight backends to produce **0–100 risk scores** from engine agreement, win-rate gaps, sharp-move streaks, evasion patterns, and related shape-based signals. (source: wiki/sources/descriptions/AODOJUST__gomoku-anti-cheat-detector.md)

README category: Anti Cheat / Open Source Anti Cheat System.

## Detection mechanism

- **Move capture** — records full move sequences while spectating or playing on supported Gomoku sites.
- **Local engine replay** — post-game WASM replay via Rapfi with optional KataGomo HTTP or custom Rapfi weight backends.
- **Scoring signals** — engine agreement, win-rate gaps, sharp-move streaks, evasion patterns, and shape-based fingerprints fused into a 0–100 risk score.
- **Threshold learning** — sample library lets moderators tune suspicion cutoffs from labeled games before acting on scores.

## Architecture

- **Browser extension** — Chrome/Edge; no server-side game integration required.
- **Live overlay** — in-session suspicion hints during spectating or play.
- **Archive viewer** — review past games and score history offline.
- **Player blacklist** — persistent watchlist for repeat suspects.
- **Multilingual chat questioning** — thirteen-language UI plus in-chat challenge prompts for human review.
- **Optional Supabase sync** — cloud activation for cross-device archive sync without restricting free offline analysis.

## Positioning

Complements federation-scale chess integrity platforms such as [[sentinel-anticheat-chess]] with a **browser-side, post-game engine-replay scorer** for casual online board titles—similar offline demo ML stacks such as [[cs2-overwatch]] and [[yaacs-anticheat]] in FPS titles, but scoped to Gomoku move telemetry and WASM engine agreement. Intended for **moderators, organizers, and players** doing practical game-security triage—not a substitute for official platform rulings.

## Peers

[[sentinel-anticheat-chess]] · [[cs2-overwatch]] · [[yaacs-anticheat]] · [[chessking]]

## Links

- Repo: https://github.com/AODOJUST/gomoku-anti-cheat-detector

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[detector-operations]] · [[research-rigor]]
