---
title: Nexora
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/epicclowds__Nexora.md
updated: 2026-11-24
confidence: medium
---

# Nexora

**Nexora** (epicclowds/Nexora) is a self-hosted **Minecraft network manager** for multi-server fleets on **Velocity** proxies and **Paper** backends. It unifies administration and player intelligence in a **Docker Compose** stack: **NestJS**/**TypeScript** API, **Next.js** dashboard, and Java proxy/backend plugins that authenticate to the control plane with **HMAC-signed** requests, heartbeats, and buffered event sync. Operators get network-wide moderation, player profiles and statistics, server monitoring, inventory editing with revision history, **role-based access control**, audit logging, and real-time dashboard updates over **Redis**-backed streams. (source: wiki/sources/descriptions/epicclowds__Nexora.md)

A dedicated anti-cheat layer exposes a Java API for trusted cheat-detection plugins, dashboard **rule engines** with violation thresholds and automated punishments, and **evidence-linked** enforcement workflows—aimed at network owners who want production-style ops and unified anti-cheat/moderation instead of per-server silos. Distinct from the unrelated Paper/Folia plugin [[nexora-anticheat]] (yuonsovann5656-netizen). (source: wiki/sources/descriptions/epicclowds__Nexora.md)

## Positioning

Self-hosted Velocity/Paper control plane with integrated AC rule orchestration beside proxy ML telemetry platforms such as [[corvus]], remote-engine Paper plugins such as [[thorium-minecraft-plugin]] and [[pluginskers-shield]], on-server heuristics such as [[bs-anticheat]], and consent/admission tooling such as [[mcace]]. Operational patterns: [[detector-operations]].

## Links

- Repo: https://github.com/epicclowds/Nexora

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[nexora-anticheat]] · [[corvus]] · [[thorium-minecraft-plugin]] · [[pluginskers-shield]] · [[bs-anticheat]] · [[mcace]] · [[detector-operations]]