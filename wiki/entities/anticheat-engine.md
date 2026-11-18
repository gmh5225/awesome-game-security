---
title: AntiCheat Engine
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/bvishwesh__AntiCheat-Engine.md
updated: 2026-11-18
confidence: high
---

# AntiCheat Engine

**AntiCheat-Engine** (bvishwesh) is a **behavioral anomaly detection** stack for multiplayer games that scores suspicious players from **session telemetry** instead of static cheat signatures. Python **scikit-learn Isolation Forest** models train only on **normal** player profiles to flag novel cheats—aimbots, speedhacks, score-farming, macro bots—from metrics such as velocity, accuracy, headshot rate, and actions per second. A **FastAPI** service exposes live analysis endpoints; companion modules add **multi-session confidence scoring** (fewer false bans), **shadow-lobby quarantine** for flagged accounts, and **dynamic matchmaking** with adaptive detection thresholds. An HTML operations dashboard and data simulator support demos and SecOps-style monitoring. Useful for game security engineers and anti-cheat researchers prototyping **ML-driven, telemetry-based** enforcement pipelines. (source: wiki/sources/descriptions/bvishwesh__AntiCheat-Engine.md)

README category: unsupervised behavioral anti-cheat stack (Isolation Forest) with FastAPI telemetry, shadow-lobby quarantine, and SecOps dashboard.

## Stack

| Layer | Role |
|-------|------|
| Models | Isolation Forest on normal-only training data |
| API | FastAPI live session analysis |
| Policy | Multi-session confidence, shadow lobbies, adaptive thresholds |
| Ops | HTML dashboard + telemetry simulator |

Research/prototype orientation—integrators supply game-specific feature engineering, labels, and production ban policy.

## Links

- Repo: https://github.com/bvishwesh/AntiCheat-Engine

## See also

[[cs2-anti-cheat-ml-research]] · [[aegis-ac-fps]] · [[apex-anticheat-lab]] · [[scaxe-anti-cheat-oss]] · [[detector-operations]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]]