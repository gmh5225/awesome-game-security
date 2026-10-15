---
title: PluginsKers Shield
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/descriptions/PluginsKers__Shield.md
  - wiki/sources/README-categories.md
updated: 2026-10-15
confidence: medium
---

# PluginsKers Shield

**Shield** (PluginsKers/Shield) is an open-source Minecraft server plugin for Paper, Folia, and Purpur that streams movement, combat, and interaction telemetry to the remote Shield analysis service for inference and human review. Kotlin on Java 21 with Gradle; ProtocolLib for packet capture, rate limiting, and disk-backed retry when HTTPS delivery fails. Signed batched events feed cloud review; the plugin applies configurable warnings and authorized kicks while avoiding automatic bans. Operators register via the Shield dashboard and configure a server key—detection depends on that service rather than fully offline on-server models. (source: wiki/sources/descriptions/PluginsKers__Shield.md)

## Detection stack

Server-side event capture (movement, combat, interaction); ProtocolLib packet path; HTTPS batching with retry; remote Shield review; warnings and kicks only (no ban automation in-plugin).

## Links

- Repo: https://github.com/PluginsKers/Shield

## Related

[[overviews/anti-cheat]] · [[thorium-minecraft-plugin]] · [[shard]] · [[bs-anticheat]] · [[detector-operations]] · [[minecraft-anticheat-list]]
