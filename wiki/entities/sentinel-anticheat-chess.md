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

**Sentinel AntiCheat** (AbdulAmi09/SentinelAntiCheat) is a **chess integrity platform** that analyzes games for statistical engine-assistance signals and produces explainable risk findings for human arbiters rather than automated cheating verdicts. Built in Python with a FastAPI backend and Next.js arbiter dashboard, it targets chess arbiters, chief arbiters, and federations investigating over-the-board and online integrity incidents. (source: wiki/sources/descriptions/AbdulAmi09__SentinelAntiCheat.md)

README category: Anti Cheat / Open Source Anti Cheat System.

Distinct from [[sentinel-anti-cheat]] (HEEAAP usermode daemon) and [[sentinel-anticheat-neoforge]] (NeoForge Minecraft mod).

## Detection layers

Seven signal layers fuse into tiered risk scores with per-layer explanations:

- **Move-quality baseline** — Regan-style move-quality scoring against engine reference lines.
- **Complexity** — position difficulty and decision depth cues.
- **Timing** — clock-use and move-time distributions.
- **Historical play** — deviation from a player's established performance profile.
- **Behavioral patterns** — session-level consistency and anomaly cues.
- **Online behavior** — platform/account signals for remote events.
- **Environmental / identity** — venue, device, and identity-correlation cues.

Stockfish-backed PGN analysis and Maia human-likeness comparison anchor engine vs human baselines; optional XGBoost and Isolation Forest fusion add ensemble scoring on top of the layered signals. (source: wiki/sources/descriptions/AbdulAmi09__SentinelAntiCheat.md)

## Operations and arbiter workflow

Hash-chained audit logging, case management, live-game monitoring, and a partner API support federation-scale review workflows. Risk tiers and per-layer explanations feed **human adjudication**—the platform surfaces evidence for arbiters rather than issuing autonomous bans.

## Positioning

Complements online chess platforms with server-side risk scoring such as [[chessking]] (Rust Axum; device fingerprint, match integrity, CAPTCHA step-up) with an **offline/post-game statistical review workbench** for engine-assistance investigations—multi-layer PGN telemetry, explainable fusion, and audit-grade case tooling beside demo/replay ML stacks such as [[cs2-overwatch]] and [[yaacs-anticheat]] in other titles.

## Peers

[[chessking]] · [[cs2-overwatch]] · [[yaacs-anticheat]] · [[dlac]] · [[stockfish]]

## Links

- Repo: https://github.com/AbdulAmi09/SentinelAntiCheat

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[detector-operations]] · [[research-rigor]]
