---
title: PluginsKers Shield
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/PluginsKers__Shield.md
  - wiki/sources/README-categories.md
updated: 2026-10-15
confidence: high
---

# PluginsKers Shield

**Shield** (PluginsKers/Shield) is an open-source Minecraft server plugin for **Paper**, **Folia**, and **Purpur** that collects player movement, combat, and interaction events for anti-cheat and behavior monitoring. Written in **Kotlin** (Gradle, **Java 21**), it targets operators who want cloud-assisted review rather than fully offline on-server inference. (source: wiki/sources/descriptions/PluginsKers__Shield.md)

## Architecture

- **Capture** — Bukkit-style gameplay events plus **ProtocolLib** packet-oriented capture; local **rate limiting** before export.
- **Transport** — **Signed**, batched events over **HTTPS** to the remote Shield analysis service (remote inference plus human review).
- **Reliability** — In-memory queuing with **disk-backed retry** when HTTPS delivery fails.
- **Enrollment** — Operators register through the **Shield dashboard** and configure a **server key**; behavior analysis depends on that cloud service, not offline models on the game host. (source: wiki/sources/descriptions/PluginsKers__Shield.md)

## Enforcement

Configurable **warnings** and **authorized kicks**; the plugin deliberately **avoids automatic bans**—high-impact sanctions remain operator-controlled after remote review. (source: wiki/sources/descriptions/PluginsKers__Shield.md)

## Positioning

**Open telemetry + cloud review** on the authoritative Java server—beside WebSocket/protobuf remote-engine plugins such as [[thorium-minecraft-plugin]], HTTPS inference plugins such as [[shard]] and [[guardac]], and on-server heuristic stacks such as [[bs-anticheat]]. Catalog context: [[minecraft-anticheat-list]]. Operational patterns: [[detector-operations]]. (source: wiki/sources/descriptions/PluginsKers__Shield.md)

## Links

- Repo: https://github.com/PluginsKers/Shield

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[thorium-minecraft-plugin]] · [[shard]] · [[guardac]] · [[bs-anticheat]] · [[detector-operations]] · [[minecraft-anticheat-list]]
