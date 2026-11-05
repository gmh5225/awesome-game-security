---
title: wow-live
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Ltz-lab__wow-live.md
updated: 2026-11-05
confidence: medium
---

# wow-live

**wow-live** extracts live **World of Warcraft** game state from the stock client’s encrypted network traffic without process injection or reading game memory. The stack is mainly **Go**, with a **Rust** rotation helper and **Python** overlays. It relays **Battle.net** login to capture world-key material, incrementally decrypts growing **tcpdump** captures, and decodes opcodes, combat events, auras, cooldowns, and world-object updates into **JSON lines**. Built-in tooling includes a **WebSocket** combat feed hub, a **Hekili**-style rotation suggester driven by **SimulationCraft APLs**, radar views (web and overlay), and an **MCP** server for external agents. Targets researchers and tool builders reverse engineering and monitoring **retail** and **WoW Forever** client–server protocols for analysis, automation, and live situational awareness. (source: wiki/sources/descriptions/Ltz-lab__wow-live.md)

Contrasts with in-process WoW cheat samples such as [[ohack]] and Warden research such as [[x14-08-coverstory-blizzard]] by staying outside the game process; complements client-binary workflows like [[dumpwow]] and [[wow-iat-fix]] for full-stack WoW security study.

## Links

- Repo: https://github.com/Ltz-lab/wow-live

## Related

[[dumpwow]] · [[wow-iat-fix]] · [[x14-08-coverstory-blizzard]] · [[ohack]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
