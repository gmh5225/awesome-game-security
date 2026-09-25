---
title: Sentinel AntiCheat (Chess)
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/AbdulAmi09__SentinelAntiCheat.md
  - wiki/sources/README-categories.md
updated: 2026-09-25
confidence: medium
---

# Sentinel AntiCheat (Chess)

**Sentinel AntiCheat** (AbdulAmi09/SentinelAntiCheat) is a **chess integrity platform** that analyzes games for statistical engine-assistance signals and produces explainable risk findings for human arbiters rather than automated cheating verdicts. Built in Python with a FastAPI backend and Next.js arbiter dashboard, it combines a Regan-style move-quality baseline with seven signal layers (complexity, timing, historical play, behavioral patterns, online behavior, environmental/identity cues), fused into tiered risk scores with per-layer explanations. Stockfish-backed PGN analysis, Maia human-likeness comparison, optional XGBoost/Isolation Forest fusion, hash-chained audit logging, case management, live-game monitoring, and a partner API support federation-scale workflows. (source: wiki/sources/descriptions/AbdulAmi09__SentinelAntiCheat.md)

README category: Anti Cheat / Open Source Anti Cheat System.

Distinct from [[sentinel-anti-cheat]] (HEEAAP usermode daemon) and [[sentinel-anticheat-neoforge]] (NeoForge Minecraft mod).

## Links

- Repo: https://github.com/AbdulAmi09/SentinelAntiCheat

## Related

[[overviews/anti-cheat]] · [[chessking]] · [[ai-aimbot-detection]] · [[detector-operations]] · [[research-rigor]]
