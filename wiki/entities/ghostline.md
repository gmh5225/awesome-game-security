---
title: Ghostline
kind: entity
topics: [anti-cheat, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/marclourens19__ghostline.md
updated: 2026-10-27
confidence: medium
---

# Ghostline

Top-down **2D arena shooter** reference that demonstrates **authoritative server-side input replay verification** so leaderboard scores are not trusted from the client alone. The **Godot 4 C#** client records per-tick player inputs into a compact binary **GHST** replay stream; an **ASP.NET Core** API ingests replays, applies bounds checks, **SHA-256** deduplication, and rate limiting, then re-runs the match in a headless deterministic simulator. (source: wiki/sources/descriptions/marclourens19__ghostline.md)

A shared **C# simulation engine** uses integer fixed-point math and circular physics so Windows clients and Linux servers agree on outcomes; verified runs persist in **PostgreSQL**. A zero-dependency **HTML5 replay inspector** parses GHST frames in the browser for tick scrubbing and telemetry review. Useful for game security and anti-cheat research, deterministic netcode study, and cheat-resistant online scoring architectures.

## Links

- Repo: https://github.com/marclourens19/ghostline

## Related

[[overviews/anti-cheat]] · [[overviews/game-engine]] · [[pew-game]] · [[blastscale]] · [[gatewarden-public]] · [[dot-server-security]]
