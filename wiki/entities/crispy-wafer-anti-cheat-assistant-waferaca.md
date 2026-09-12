---
title: WaferACA
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/sodium-CrispyWafer__CrispyWafer-Anti-Cheat-Assistant-WaferACA.md
updated: 2026-09-12
confidence: medium
---

# WaferACA

**CrispyWafer Anti-Cheat Assistant (WaferACA)** is a Minecraft **Forge 1.20.1** client anti-cheat mod that detects cheating client mods installed by other players on multiplayer servers and alerts when known cheat mods (e.g., Gun Tracker) are present. Written in Java with Gradle. (source: wiki/sources/descriptions/sodium-CrispyWafer__CrispyWafer-Anti-Cheat-Assistant-WaferACA.md)

## Dual-mode architecture

- **Server-cooperative mode** — extracts accurate peer mod lists via Forge FML handshake data and custom network packets when the server participates.
- **Client-only fallback** — heuristic aimbot detection from rotation smoothness, flick patterns, and tracking behavior when server cooperation is unavailable.

## Operator features

- Public chat broadcast of cheat alerts
- Per-player mod lists via commands and key bindings
- Lightweight peer visibility for mod-based cheating and aim-assist on Forge multiplayer

Targets Minecraft server operators and players who need client-side awareness of peer cheat mods without full server-side physics AC such as [[grim]].

## Links

- Repo: https://github.com/sodium-CrispyWafer/CrispyWafer-Anti-Cheat-Assistant-WaferACA

## Related

[[katapult-anticheat]] · [[local-anticheat-1-8-9]] · [[seiun-ac]] · [[the-dreamers-guards]] · [[anticheat-qa]] · [[minecraft-anticheat-list]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
