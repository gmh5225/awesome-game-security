---
title: KCP
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/descriptions/skywind3000__kcp.md
updated: 2026-07-22
confidence: medium
---

# KCP

Fast, reliable ARQ (Automatic Repeat reQuest) protocol in C that provides TCP-like reliability over UDP. Trades 10–20% more bandwidth for 30–40% lower latency versus TCP via aggressive retransmission, selective ACK, and fast recovery without TCP congestion-control overhead. Single-file, protocol-agnostic library usable over any transport; aimed at low-latency real-time multiplayer networking. (source: wiki/sources/descriptions/skywind3000__kcp.md)

Sits under README `Game Network` as a study surface for reliable-UDP game transport rather than client-side cheat tooling.

## Links

- Repo: https://github.com/skywind3000/kcp

## Related

[[overviews/game-engine]] · [[overviews/overview]] · [[uwebsockets]] · [[socket-io]] · [[pitaya]] · [[jwt-tool]]
