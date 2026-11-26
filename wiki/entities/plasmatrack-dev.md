---
title: PlasmaTrack Dev
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/KoJesko__PlasmaTrack-Dev.md
updated: 2026-11-26
confidence: high
---

# PlasmaTrack Dev

**PlasmaTrack** ([KoJesko/PlasmaTrack-Dev](https://github.com/KoJesko/PlasmaTrack-Dev)) is a **Euro Truck Simulator 2 / American Truck Simulator VTC job-tracking stack** that records in-game telemetry on the player PC, uploads raw timeline chunks, and **reconstructs and scores each haul on the server** so community operators are not limited to client-trusted scorekeeping. (source: wiki/sources/descriptions/KoJesko__PlasmaTrack-Dev.md)

## Client pipeline

- **C++ in-game plugin** built on the **SCS** and **TruckersMP** telemetry SDKs streams haul telemetry to a background uploader.
- **Background client** persists chunks locally in **SQLite** and uploads raw telemetry to ingest.
- **Windows Electron installer** packages deployment for virtual-trucking (VTC) members.

## Shared replay core

- **`pt-core` (Rust)** implements timeline reconstruction, scoring rules, and **bit-identical replay** on both client preview and server adjudication—pair scoring outcomes with [[input-provenance]] **server-derived** labels after replay, not client-reported job totals.

## Backend

- **Cloudflare Workers** deployment with **D1**, **R2**, **queues**, and **durable objects**; public and admin APIs plus **Discord webhook** integrations for bot workflows.

## Anti-cheat posture

Server-side checks flag **suspicious jobs for manual review** rather than trusting client-computed scores—suited to VTC operators who need auditable haul validation. Operational review queues align with [[detector-operations]] human-disposition patterns beside replay-first references such as [[dmn-minigame]] and [[serverless-time-trial-racing-game]].

## Related

[[concepts/input-provenance]] · [[concepts/detector-operations]] · [[spf-ghidra-pattern-helper]] · [[overviews/anti-cheat]]