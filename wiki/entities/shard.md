---
title: Shard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/KaelusAI__Shard.md
updated: 2026-08-24
confidence: medium
---

# Shard

Free, open-source, AI-powered anti-cheat plugin for Minecraft **Paper** and **Folia** servers. Written primarily in Kotlin with Gradle, it uses **PacketEvents** for packet-level analysis and sends player tick data to a remote inference API for AI-based cheating checks rather than relying only on heuristic packet rules. Optional **SQLite**, **MySQL**, or **MariaDB** storage and **Redis**-backed cross-server alerts support multi-network deployments. Operators get monitoring, profiling, violation history, configurable punishment rules, **WorldGuard** region exemptions, and **Geyser**-related integrations. Targets Minecraft server admins who want modern anti-cheat tooling with AI-assisted detection. (source: wiki/sources/descriptions/KaelusAI__Shard.md)

## Detection stack

PacketEvents packet-level analysis; player tick data forwarded to remote AI inference API; optional SQLite/MySQL/MariaDB violation storage; Redis cross-server alerts; monitoring and profiling; violation history; punishment rules; WorldGuard region and Geyser Bedrock exemptions.

## Links

- Repo: https://github.com/KaelusAI/Shard

## Related

[[guardac]] · [[react]] · [[mlanticheat]] · [[minecraft-anti-cheat]] · [[minecraft-anticheatai]] · [[uagc]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
