---
title: YAACS AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/oykuoner__YAACS-AntiCheat.md
updated: 2026-09-22
confidence: medium
---

# YAACS AntiCheat

**YAACS** (Yet Another Anti-Cheat System; oykuoner) is a Python server-side anti-cheat **research framework** that detects aim assistance in Counter-Strike by analyzing pitch and yaw aiming telemetry from match demos instead of probing client memory. It parses HLTV demos with **demoparser2**, builds synthetic and real-world datasets (NumPy, pandas, scikit-learn) modeling honest players, elite pros, hardware aimbots, and humanised evasion cheats, and benchmarks a static heuristic rule engine against a **Random Forest** classifier. (source: wiki/sources/descriptions/oykuoner__YAACS-AntiCheat.md)

## Pipeline

- **Demo ingestion** — extract per-tick aim telemetry from CS2 match demos via demoparser2.
- **Feature engineering** — spatiotemporal signals from 100-tick windows: velocity, acceleration, and angle deltas grounded in Fitts' Law and the Minimum Jerk Model.
- **Detection modes** — compare explainable heuristic rules vs supervised Random Forest classification.
- **Privacy posture** — no kernel driver or client memory scan; replay-only observable behavior.

Targets game-security researchers and anti-cheat developers who need a privacy-preserving, explainable alternative to kernel-level client monitoring for FPS aimbot detection.

## Peers

[[cs2guard]] · [[deepaimdetector]] · [[dlac]] · [[cs2ac]] · [[osanticheat]] · [[aimbot-detection-prototype]]

## Links

- Repo: https://github.com/oykuoner/YAACS-AntiCheat

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[input-provenance]] · [[research-rigor]]
