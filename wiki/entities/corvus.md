---
title: Corvus
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/OneLiteFeatherNET__Corvus.md
updated: 2026-10-16
confidence: medium
---

# Corvus

**Corvus** (OneLiteFeatherNET/Corvus) is an open-source **machine-learning anti-cheat platform** for **Minecraft** proxy networks. It passively collects player **network traffic**, enriches and scores it in Python backend services, and exposes per-player **likelihood-of-cheating** scores as a **staff decision aid**—not automatic punishment. A **Java Velocity** proxy plugin captures packets via **PacketEvents** and publishes them over **NATS JetStream**; shared **Protocol Buffers** schemas tie the stack together. Captures land in a pseudonymous **Parquet** data lake on S3-compatible storage with **PostgreSQL** catalog metadata; curated datasets feed offline training and evaluation with **scikit-learn**, **PyTorch**, and **ONNX**. A CPU-only online scoring service serves scores through a plugin API and a **Nuxt** management UI; **Docker Compose** and **Helm** charts support deployment. Targets network operators and anti-cheat teams who want evidence-backed moderation on proxy-based game infrastructure. (source: wiki/sources/descriptions/OneLiteFeatherNET__Corvus.md)

## Architecture

Proxy-side PacketEvents capture → NATS JetStream ingest → Python enrich/score pipeline → pseudonymous Parquet lake + PostgreSQL catalog → offline ML training (sklearn/PyTorch/ONNX) → CPU online scoring API → staff-facing Nuxt UI. (source: wiki/sources/descriptions/OneLiteFeatherNET__Corvus.md)

## Positioning

Velocity proxy ML telemetry and staff-review scoring beside remote-engine Paper plugins such as [[thorium-minecraft-plugin]] and [[pluginskers-shield]], on-server PacketEvents heuristics such as [[fox-addition]], and consent-based admission tooling such as [[mcace]]. Operational patterns: [[detector-operations]].

## Links

- Repo: https://github.com/OneLiteFeatherNET/Corvus

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[thorium-minecraft-plugin]] · [[pluginskers-shield]] · [[fox-addition]] · [[mcace]] · [[detector-operations]] · [[minecraft-anticheat-list]]
