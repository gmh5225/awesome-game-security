---
title: AimGuard
kind: entity
topics: [anti-cheat, mobile-security]
sources:
  - wiki/sources/descriptions/Ajitha-2001__aimguard.md
  - wiki/sources/README-categories.md
updated: 2026-10-22
confidence: high
---

# AimGuard

**AimGuard** (Ajitha-2001/aimguard) is a **Python server-side anti-cheat prototype** that ingests match telemetry, scores player behavior, and routes outcomes through **moderator-driven enforcement** rather than automatic bans. It targets game-security engineers and anti-cheat researchers who want to experiment with **shadow-mode scoring**, **evidence trust levels**, and operational workflows on **synthetic gameplay data** before integrating client protection and production-scale infrastructure. (source: wiki/sources/descriptions/Ajitha-2001__aimguard.md)

README category: Anti Cheat / Open Source Anti Cheat System.

## Detection surface

- **Aim and movement features** — feature extraction modules over ingested match telemetry for behavioral scoring.
- **Lag-compensated validation** — server rules that reconcile combat/movement claims against compensated server state.
- **Grid-based PVS** — potential visibility sets limit what clients replicate; pair visibility-bound features with [[input-provenance]] labels for replicated vs server-derived observables.
- **Network integrity** — HMAC and anti-replay checks on telemetry transport.
- **Attestation and client trust** — Play Integrity attestation handling for mobile-origin trust signals.
- **Statistical and ML detectors** — layered scoring beside rule-based validation.
- **Hash blocklists** — optional local PC scanning against known cheat artifacts.

## Operations

**SQLite** persistence backs a token-authenticated **HTTP API** with review queues, appeals, and ban waves—human disposition before high-impact sanctions. Calibrate shadow-mode trust levels and review volume with [[detector-operations]] canary practices before enabling automatic ban waves.

## Positioning

End-to-end server-side AC lab stack on synthetic data—beside server-log FPS evidence pipelines such as [[detect-fps-hackers]], Paper ML combat plugins such as [[powerac]] and [[eigen-anticheat]], and review-first Fabric stacks such as [[vylorq-vigil]]; complements authoritative-server SDKs such as [[guard-game]] and Godot dry-run addons such as [[dot-server-security]].

## Links

- Repo: https://github.com/Ajitha-2001/aimguard

## Related

[[concepts/detector-operations]] · [[concepts/input-provenance]] · [[guard-game]] · [[dot-server-security]] · [[overviews/anti-cheat]]
