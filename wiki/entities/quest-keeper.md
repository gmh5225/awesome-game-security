---
title: QuestKeeper
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/agvmdsa__QuestKeeper.md
updated: 2026-11-09
confidence: medium
---

# QuestKeeper

**QuestKeeper** (agvmdsa/QuestKeeper) is an unofficial **Windows** companion for **AdventureQuest Worlds** that passively listens to local **TCP** game traffic and surfaces **character profile**, **faction reputation**, and **inventory** data in an **Avalonia** dashboard. It is implemented in **C#** on **.NET**, captures live packets via **Npcap**, and decodes server messages through frame parsing, TCP stream reassembly, and structured game-data extraction with **LiteDB** persistence. Operation is **read-only** toward the game client: it avoids client-to-server login payloads, supports optional local data forgetting, and does not send telemetry—suited to progress tracking and **MMORPG passive wire-protocol** study on Windows. (source: wiki/sources/descriptions/agvmdsa__QuestKeeper.md)

README lists a read-only AQW companion that captures local client traffic via Npcap and parses character, faction, and inventory data (Cheat / Packet Capture&Parse). (source: wiki/sources/descriptions/agvmdsa__QuestKeeper.md)

## Links

- Repo: https://github.com/agvmdsa/QuestKeeper

## Related

[[npcap]] · [[packet-sniffer]] · [[reliquary-archiver]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
