---
title: Aegis Log Sentinel
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/jeffreyesdavid__aegis-log-sentinel.md
updated: 2026-11-26
confidence: high
---

# Aegis Log Sentinel

**Aegis Log Sentinel** (jeffreyesdavid/aegis-log-sentinel) is a lightweight **live-service game security investigation and triage** pipeline for MMO and action titles. Python **stdlib-only** code ingests telemetry into **SQLite**, runs deterministic cheat heuristics, and escalates prioritized findings for analysts—combining rule checks with **AI-assisted reporting** while minimizing player-data leakage. (source: wiki/sources/descriptions/jeffreyesdavid__aegis-log-sentinel.md)

README category: Python live-service telemetry triage with HMAC pseudonymization, movement/bot/economy cheat heuristics, and unittest-backed detection benchmarks.

Repository: [jeffreyesdavid/aegis-log-sentinel](https://github.com/jeffreyesdavid/aegis-log-sentinel).

## Privacy and storage

Player IDs and IPs are **pseudonymized with HMAC-SHA256** before any external summarization, supporting zero-leak analyst briefings on production telemetry. Local SQLite retains investigation state without shipping raw identifiers to third-party AI layers.

## Detection stack

| Layer | Role |
|-------|------|
| Rules | Movement speed abuse, macro/smart-bot cadence, abnormal economy/currency spikes |
| ML | **Isolation Forest** on behavioral features for jittered automation missed by rules alone |
| Policy | Severity-ranked analyst actions (trade freezes, log capture, suspension **recommendations**)—no automatic bans |
| QA | Synthetic benchmarks and unit tests stress false positives vs legitimate high-skill play |

Isolation Forest hits route to **human review** rather than autonomous sanctions, aligned with [[detector-operations]] decision-state separation.

## Audience

Game security analysts and engineers who need **privacy-preserving telemetry triage** and exploit-briefing workflows on live game services—beside FPS behavioural stacks such as [[aegis-ac-fps]], log-review CLIs such as [[detect-fps-hackers]], and unsupervised session ML such as [[anticheat-engine]].

## See also

[[aegis-ac-fps]] · [[detect-fps-hackers]] · [[anticheat-engine]] · [[player-simulation]] · [[detector-operations]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]]