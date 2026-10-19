---
title: Eigen (ML combat anti-cheat)
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/voilecx__eigen.md
  - wiki/sources/README-categories.md
updated: 2026-10-19
confidence: medium
---

# Eigen (ML combat anti-cheat)

Open-source **machine-learning combat anti-cheat** for **Minecraft Paper and Folia** (voilecx/eigen). Scala 3 + sbt server plugin uses **PacketEvents** to observe per-player network traffic and reconstruct what each client sees—lag-compensated aim geometry plus sensitivity-independent mouse input—without trusting client-side reports. (source: wiki/sources/descriptions/voilecx__eigen.md)

## Detection pipeline

Every client tick becomes a **feature row** in a combat telemetry schema. Rows aggregate into **combat** and **baseline** windows, then stream over an authenticated **WebSocket** to a separate backend for labelled dataset collection and online inference—ML-driven combat cheat detection instead of purely heuristic rule stacks. (source: wiki/sources/descriptions/voilecx__eigen.md)

## Architecture

Core modules hold platform-agnostic simulation, schema, and wire encoding; a Paper adapter bridges the game server. Techniques from projects such as GrimAC and Shard inform transaction-based lag compensation and ML-oriented tick features. (source: wiki/sources/descriptions/voilecx__eigen.md)

## Audience

Server operators and anti-cheat developers who want **ML-driven combat cheat detection** from server-observable packets rather than purely heuristic plugins—aligned with [[concepts/ai-aimbot-detection]] and [[concepts/input-provenance]] server-side telemetry discipline. (source: wiki/sources/descriptions/voilecx__eigen.md)

## Links

- Repo: https://github.com/voilecx/eigen

## Related

[[overviews/anti-cheat]] · [[tfg-anticheat-serverside]] · [[thorium-minecraft-plugin]] · [[grim]] · [[shard]] · [[concepts/detector-operations]] · [[concepts/ai-aimbot-detection]]
