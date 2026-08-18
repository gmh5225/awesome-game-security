---
title: R6Intel
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/baldspots440__R6Intel.md
updated: 2026-08-18
confidence: medium
---

# R6Intel

Web-based **Rainbow Six Siege** statistical analysis platform (Node.js/Express backend; vanilla JavaScript frontend) that evaluates player accounts for performance anomalies and cheating indicators. Pulls ranked stats from the **R6Data API** across Ubisoft, Xbox, and PlayStation and computes a 0–100 **Suspicion Score** from K/D, headshot rate, kills per match, win rate, and related metrics—with current-season vs historical snapshot comparison, compound anomaly bonuses, sample-size confidence weighting, and separate tracking of confirmed sanctions. Profiles, aliases, and snapshots persist via Supabase or local JSON; caching, rate-limit pacing, and request deduplication manage upstream API constraints. Intended for game security researchers, community moderators, and competitive integrity workflows seeking data-driven leads—not definitive cheat verdicts. (source: wiki/sources/descriptions/baldspots440__R6Intel.md)

## Links

- Repo: https://github.com/baldspots440/R6Intel

## Related

[[battleye]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[r6-external]] · [[r6s-external-v2]] · [[rainbow-six-siege-rs6-external-esp-aimbot-hack-cheat]]
