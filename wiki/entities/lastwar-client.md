---
title: Last War Client (Go)
kind: entity
topics: [game-engine, reverse-engineering, mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/ljagiello__lastwar-client.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: high
---

# Last War Client (Go)

**lastwar-client** (ljagiello/lastwar-client) is a from-scratch Go reimplementation of the Last War: Survival Game mobile client network stack, built by reverse engineering the decompiled APK so sessions can run over TCP without the Unity app. (source: wiki/sources/descriptions/ljagiello__lastwar-client.md)

## Stack

| Piece | Role |
|-------|------|
| **GSL bootstrap** | RSA and AES session cryptography |
| **SFS2X framing** | SmartFoxServer wire format and compression |
| **SFSObject codec** | Binary object serialization matching production clients |
| **CLI automation** | Login, resource collection, alliance actions, and related account tasks |
| **PCAP tooling** | Decode captured login traffic into reusable session JSON |

Extensive documentation catalogs the wire protocol, command set, entity IDs, ShuMei anti-fraud fields, and session recovery workflows, with behavior **live-validated against production servers**—useful for **mobile game protocol RE** and headless client research (not proof of server authorization). Listed under README **Game Network / Source**. (source: wiki/sources/descriptions/ljagiello__lastwar-client.md)

## Research audience

Game security and reverse-engineering researchers who need a **compatible headless client** and a detailed reference for Unity mobile TCP/SmartFoxServer-style sessions without running the official app. PCAP-derived session JSON supports repeatable login replay beside CLI automation for account-oriented tasks. (source: wiki/sources/descriptions/ljagiello__lastwar-client.md)

## Links

- Repo: https://github.com/ljagiello/lastwar-client

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[mobile-network-trust-evidence]] · [[frida]] · [[spirit-ptcgo]]
