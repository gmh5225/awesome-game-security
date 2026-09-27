---
title: ida-teams-docker
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ioncodes__ida-teams-docker.md
  - wiki/sources/README-categories.md
updated: 2026-09-27
confidence: medium
---

# ida-teams-docker

**ida-teams-docker** (ioncodes/ida-teams-docker) dockerizes the **Hexvault** and **Lumina** servers used by **IDA Pro Teams**, packaging them for deployment with **Docker Compose**. Separate container images serve Hexvault and Lumina; a **MySQL** backend backs Lumina metadata; shell entry scripts handle **TLS certificate generation**, **license validation**, and **database schema initialization**. Build-time Python setup scripts create license files without leaving the scripts in final images, while Docker volumes persist vault data, database state, and TLS material. Targets reverse engineers and security researchers who need a self-hosted collaborative IDA Teams environment for shared databases, function signatures, and team vault storage. (source: wiki/sources/descriptions/ioncodes__ida-teams-docker.md)

README category: Cheat / RE Tools.

## Architecture

- **Hexvault container** — team vault storage for shared IDA databases and collaborative project state.
- **Lumina container** — function-signature and metadata sharing service for IDA Teams clients.
- **MySQL backend** — Lumina persistence layer with schema init handled at container startup.
- **TLS + volumes** — entry scripts generate certificates; named volumes retain vault data, DB state, and TLS material across redeploys.

## Positioning

Self-hosted **IDA Teams infrastructure** rather than an in-IDA plugin: complements real-time IDB co-editing via [[idarling]], Git-backed partial sync via [[labsync]], and third-party Lumina client connectivity via [[openlumina]]—this stack is the server side that Hexvault/Lumina clients attach to. Contrasts with disposable batch harnesses such as [[ida-nexus-docker]] (LLM-driven isolated analysis runs).

## Links

- Repo: https://github.com/ioncodes/ida-teams-docker

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[openlumina]] · [[idarling]] · [[labsync]] · [[ida-nexus-docker]] · [[ida-plugin-repository]]
