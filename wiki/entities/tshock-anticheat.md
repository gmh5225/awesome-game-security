---
title: TShock AntiCheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Ghou133__TShock-AntiCheat.md
updated: 2026-09-22
confidence: medium
---

# TShock AntiCheat

**TShock AntiCheat** is a server-side anti-cheat **plugin** for **Terraria 1.4.5.8** [[tshock]] servers that validates player network packets and game actions before they affect the world. Written in **C#** for **.NET 9**, it uses a modular design with separate core engine, rule, persistence, and TShock adapter layers to enforce checks on combat, inventory, progression, world editing, summons, and protocol abuse. (source: wiki/sources/descriptions/Ghou133__TShock-AntiCheat.md)

## Detection and enforcement

- **Packet readers and safety guards** — intercept and validate Terraria protocol traffic before world mutation
- **Combat and progression** — abnormal damage (butcher), unauthorized summons, progression abuse
- **World editing** — map-brush and tile-manipulation cheats
- **Inventory and economy** — item duplication and item-abuse vectors
- **Protocol abuse** — unauthorized messaging and health-lock exploits
- **Operator tooling** — optional account banning and enforcement journaling

Ships as development source in **ObserveOnly** mode rather than a production-ready release—intended for Terraria server operators and game-security researchers who need deep, packet-level server protection against common cheat clients, complementing [[tshock]]'s built-in **Bouncer** layer.

## Links

- Repo: https://github.com/Ghou133/TShock-AntiCheat

## Related

[[tshock]] · [[7dtd-anticheatmod]] · [[fusion-anti-cheat]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
