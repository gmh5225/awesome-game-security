---
title: BE Emulator
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__BE-Emulator.md
updated: 2026-08-14
confidence: medium
---

# BE Emulator

BattlEye **client-side emulator** (gmh5225): simulates [[battleye]]'s in-process behavior without the real anti-cheat stack running. It emulates the BE communication protocol, heartbeat responses, and module-loading interface so protected games can launch and interact with a fake BE client while protection stays inactive—useful for analyzing how titles integrate with BattlEye and for protocol/integration RE. (source: wiki/sources/descriptions/gmh5225__BE-Emulator.md)

Complements service/install/launch emulation such as [[fakeeye]] by focusing on runtime client protocol and module-load contracts rather than SCM `BEService` startup.

## Links

- Repo: https://github.com/gmh5225/BE-Emulator

## Related

[[battleye]] · [[fakeeye]] · [[be-forcer-fortnite]] · [[bedaisy-bypass]] · [[overviews/anti-cheat]]
