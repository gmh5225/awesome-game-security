---
title: H-AC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Benardelys__H-AC.md
  - wiki/sources/README-categories.md
updated: 2026-09-25
confidence: medium
---

# H-AC

**H-AC** (HukumAC; Benardelys/H-AC) is a high-performance, modular **Paper 1.21** server-side anti-cheat plugin for Minecraft. Written in Java with a Maven build, it detects hacked clients through authoritative physics simulation, combat heuristics, and network balance analysis—aimed at server administrators and anti-cheat developers who need production-grade, server-authoritative cheat mitigation on modern Paper releases. (source: wiki/sources/descriptions/Benardelys__H-AC.md)

README category: Anti Cheat / game:minecraft.

## Detection layers

Dozens of isolated checks span three domains, each with configurable thresholds, punishments, and violation decay to reduce false positives:

- **Combat** — kill aura, reach, auto-clicking.
- **Movement** — fly, speed, phase.
- **World / player** — scaffold, fast break, timer drift.

Latency-aware reach raytracing validates combat distance against server geometry; network balance analysis complements physics simulation for timing and packet-rate anomalies. (source: wiki/sources/descriptions/Benardelys__H-AC.md)

## Operations and staff tooling

Server TPS safeguards prevent check storms under load; asynchronous violation logging and Discord webhook alerts keep enforcement off the main thread. Staff commands support live alerts, debugging, and violation review. Client brand fingerprinting, injector detection, and reconnect protection add client-integrity signals beside movement and combat heuristics.

## Positioning

Complements heuristic Paper plugins such as [[bs-anticheat]] (Folia-aware transaction lag compensation, SQLite logging) and custom-SMP plugins such as [[larping-anti-cheat]] (honeypot/ESP decoys, modded-SMP capability analyzer) with a **modular, latency-compensated reach** stack and explicit client-brand/injector probes—closer to production operator tooling than research foundations such as [[inertia]] or physics-prediction references such as [[grim]].

## Peers

[[bs-anticheat]] · [[larping-anti-cheat]] · [[grim]] · [[ultimate-meteor-anticheat]] · [[minecraft-anticheat-list]]

## Links

- Repo: https://github.com/Benardelys/H-AC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[detector-operations]] · [[bs-anticheat]] · [[larping-anti-cheat]] · [[grim]] · [[minecraft-anticheat-list]]
