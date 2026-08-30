---
title: Spirit-PTCGO
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Bratah123__Spirit-PTCGO.md
updated: 2026-08-30
confidence: medium
---

# Spirit-PTCGO

**Spirit** is a Python private-server reimplementation of **Pokémon Trading Card Game Online (PTCGO)** with a full game backend for local or self-hosted client connections. Implements card rules and effects across many sets, account and inventory databases, economy and shop systems, versus play, live tournaments, and custom cosmetics such as avatars, sleeves, and packs. The codebase includes an HTTP and game server stack, Protocol Buffer definitions for the client protocol, reverse-engineering helpers for card bundles, and nginx or Caddy deployment configs. Targets reverse engineers, private-server operators, and researchers studying PTCGO networking, game logic, and asset tooling. (source: wiki/sources/descriptions/Bratah123__Spirit-PTCGO.md)

Sits in the README **Private Server** / card-game lane beside protobuf-based server emulators such as [[ds3os]] and general protocol schema references such as [[protobufs]]; from the same author as MapleStory IDA packet tooling [[spirit-ida-plugin]].

## Links

- Repo: https://github.com/Bratah123/Spirit-PTCGO (README tag: Pokemon TCG Online private server emulator)

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[spirit-ida-plugin]] · [[protobufs]] · [[packet-sniffer]] · [[ds3os]]
