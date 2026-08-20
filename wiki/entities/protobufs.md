---
title: protobufs
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/SteamDatabase__Protobufs.md
updated: 2026-08-20
confidence: medium
---

# protobufs

**SteamDatabase/Protobufs** — continuously tracked collection of **protobuf definitions** used by Steam and Valve games. The repository is mostly `.proto` files generated from update pipelines and automated protobuf dumpers, helping researchers keep message schemas current for protocol analysis, tooling maintenance, and game network reverse engineering. Primarily a data resource for developers working with Steam ecosystem internals. (source: wiki/sources/descriptions/SteamDatabase__Protobufs.md)

Complements transport-level references such as [[game-networking-sockets]], wire-capture tooling such as [[packet-sniffer]], and title-specific protocol emulators such as [[ds3os]]. README highlights a CS:GO schema subtree; adjacent Valve engine/runtime study includes [[source-sdk-2013]], [[proton]], and [[vac]].

## Links

- Repo: https://github.com/SteamDatabase/Protobufs (README tag: [Protobuf])
- CS:GO schemas: https://github.com/SteamDatabase/Protobufs/tree/master/csgo

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[game-networking-sockets]] · [[packet-sniffer]] · [[ds3os]] · [[source-sdk-2013]] · [[proton]] · [[vac]]
