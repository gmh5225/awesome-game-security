---
title: MCBotMod
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/xuanfeng0316__MCBotMod.md
updated: 2026-10-17
confidence: medium
---

# MCBotMod

**MCBotMod** (xuanfeng0316/MCBotMod) is a **Fabric** mod for **Minecraft Java Edition** that exposes the **live, fully rendered game client** over a **TCP/JSON remote API** instead of simulating protocol packets or running a headless client. External programs in any language with socket support can drive movement, camera, blocks, entities, inventory, chat, server connection, and related actions by invoking the game’s native client methods while rendering and UI remain intact. Built mainly in **Kotlin** and **Java** with **Fabric Mixins**, it includes **A\*** pathfinding, concurrent task handling, and coexistence of human keyboard input with automated commands on the same session. Sample Python and shell scripts demonstrate AI-driven control via an OpenAI-compatible tool interface. Targets developers researching bot behavior, client automation, and how real-client automation interacts with multiplayer game security and anti-cheat systems. (source: wiki/sources/descriptions/xuanfeng0316__MCBotMod.md)

README category: Cheat / game:minecraft.

## Architecture

| Component | Role |
|-----------|------|
| Fabric Mixins | In-process hooks into native client methods for movement, world, and UI state |
| TCP/JSON API | Language-agnostic remote control of the running client |
| Pathfinding & tasks | A* navigation and concurrent automation queue |
| Human + bot coexistence | Manual input and API commands on one live session |

## Anti-cheat interaction

Because actions originate from a **legitimate modded client** (not a pure protocol bot), server-side plugins see vanilla-style packets from a real session—useful for contrasting headless probes such as [[ghostjoin]] and mineflayer stacks such as [[eafe]] with **in-process automation** that still passes client-mod fingerprinting on hosts using [[faircount]], [[seiun-ac]], or [[key-value-checker]]. Movement and combat heuristics on plugins such as [[windfall-anticheat]], [[grim]], and [[h-ac]] remain the primary enforcement surface. (source: wiki/sources/descriptions/xuanfeng0316__MCBotMod.md)

## Links

- Repo: https://github.com/xuanfeng0316/MCBotMod

## Related

[[eafe]] · [[ghostjoin]] · [[jsaclient]] · [[vortex-client]] · [[dino-printer]] · [[anticheat-qa]] · [[faircount]] · [[windfall-anticheat]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
