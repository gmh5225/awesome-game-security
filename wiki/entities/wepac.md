---
title: WepAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wepposs__WepAC.md
updated: 2026-10-25
confidence: high
---

# WepAC

**WepAC** (wepposs/WepAC) is an open-source **Paper/Spigot** server plugin (**1.21+**) for **Minecraft** operators who want a **hybrid** anti-cheat: deterministic violation checks plus a **self-learning neural network** implemented entirely in Java on the authoritative server—no external inference service. (source: wiki/sources/descriptions/wepposs__WepAC.md)

## Detection pipeline

- **Packet path** — an embedded **Netty** packet handler inspects player traffic inline before normal plugin processing. (source: wiki/sources/descriptions/wepposs__WepAC.md)
- **Heuristics** — **movement physics simulation** catches subtle fly and speed cheats; modular checks cover combat (KillAura, reach, auto-clicker), movement, blocks (scaffold), inventory, and x-ray-style mining behavior. (source: wiki/sources/descriptions/wepposs__WepAC.md)
- **ML layer** — a small **MLP** scores per-player cheat probability, **adapts check thresholds individually**, and **learns online** from punishments, staff labels, and filtered legitimate PvP sessions; model weights **persist across restarts**. (source: wiki/sources/descriptions/wepposs__WepAC.md)
- **Client signals** — flags suspicious **client brands** from the Minecraft channel handshake. (source: wiki/sources/descriptions/wepposs__WepAC.md)
- **Operations** — staff alerts, recordings, and configurable punishments for server-local adaptive enforcement. (source: wiki/sources/descriptions/wepposs__WepAC.md)

Hybrid heuristic + embedded online-learning ML beside rotation-focused plugins such as [[powerac]], remote-engine collectors such as [[eigen-anticheat]] and [[thorium-minecraft-plugin]], and ensemble trainers such as [[mlanticheat]]. Operational patterns: [[detector-operations]] · [[ai-aimbot-detection]] · [[minecraft-anticheat-docs]].

## Links

- Repo: https://github.com/wepposs/WepAC

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[powerac]] · [[mlanticheat]] · [[eigen-anticheat]] · [[minecraft-anticheat-list]] · [[ai-aimbot-detection]] · [[detector-operations]]
