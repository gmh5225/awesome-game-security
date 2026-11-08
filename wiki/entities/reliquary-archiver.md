---
title: Reliquary Archiver
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/IceDynamix__reliquary-archiver.md
updated: 2026-11-08
confidence: medium
---

# Reliquary Archiver

**Reliquary Archiver** (IceDynamix/reliquary-archiver) is a **Rust** tool that captures and parses **Honkai: Star Rail** client–server traffic to export **relic** and **light cone** inventories as **JSON**. It ships a GUI or headless **CLI**, supports **live capture** through **Npcap** / **libpcap** (and Windows Packet Monitor on Windows), and can replay **.pcap**, **.pcapng**, or **.etl** captures offline. Game payloads decode via the **reliquary** protobuf library; export shape matches **HSR-Scanner**, and an optional **WebSocket** server streams updates for live import into **Fribbels HSR Optimizer**. The workflow targets gear-optimization automation and illustrates **passive wire-protocol inspection** and protobuf-oriented protocol RE on a live online title—without in-process injection. (source: wiki/sources/descriptions/IceDynamix__reliquary-archiver.md)

README lists live capture or uploaded pcaps to export Honkai Star Rail relic JSON for external optimizers (Cheat / networking lane). (source: wiki/sources/descriptions/IceDynamix__reliquary-archiver.md)

## Links

- Repo: https://github.com/IceDynamix/reliquary-archiver

## Related

[[star-rail]] · [[starrailcopilot]] · [[auto-simulated-universe]] · [[npcap]] · [[packet-sniffer]] · [[auto-discipher]] · [[protobufs]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
