---
title: MKAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/korpys667__MKAC.md
  - wiki/sources/README-categories.md
updated: 2026-11-15
confidence: medium
---

# MKAC

**MKAC** (korpys667/MKAC) is a free, open-source **Paper** and **Folia** Minecraft server anti-cheat plugin focused on **combat** cheating. It uses **machine learning** to flag aim-related clients such as killaura and aim assist from player input patterns, routed through a **hosted MKAC inference API** rather than purely signature-only mod blocking. The implementation is primarily **Kotlin** with a **Gradle** build targeting **Java 21**. (source: wiki/sources/descriptions/korpys667__MKAC.md)

## Detection and enforcement

- **Packet-level checks** — combat-oriented signals alongside ML inference for aim-assist-style behavior.
- **Violation logging** — auditable misconduct history for staff review.
- **Configurable punishments** — operator-tuned sanction ladders.

## Operator stack

- **Storage** — optional **SQLite**, **MySQL**, or **Redis** for persistence and **cross-server alerting**.
- **Configuration** — YAML tuning of detection and enforcement policy.
- **In-game commands** — live monitoring, suspicion review, data collection, and staff alerts.

Targets multiplayer server owners and anti-cheat researchers who want an **AI-assisted, combat-focused** deterrent on authoritative Java servers—same **cloud-inference** operator lane as [[guardac]] and [[shard]], distinct from on-server embedded models such as [[wepac]], [[powerac]], and [[civ-anticheat]].

## Links

- Repo: https://github.com/korpys667/MKAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[detector-operations]] · [[mlanticheat]] · [[guardac]] · [[shard]] · [[minecraft-anti-cheat]]