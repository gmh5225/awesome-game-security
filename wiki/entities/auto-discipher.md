---
title: auto-discipher
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/hashblen__auto-discipher.md
updated: 2026-11-02
confidence: medium
---

# auto-discipher

**hashblen/auto-discipher** — Rust library for parsing and decrypting **live network traffic** between a specific anime-style gacha online game client and its servers. Stacks Ethernet, IP, and UDP parsing with a customized **KCP** transport, connection handshake handling, and **XOR-protected** command payloads validated and decoded as **Protocol Buffer** messages. Recovers session keys by brute-forcing time-windowed seeds with Mersenne Twister–style derivation and protobuf-oracle checks, optionally using bundled RSA material where the protocol requires it. Exposes a sniffer-oriented API that turns raw captures into structured connection events and game commands for reverse engineers and community tooling authors maintaining wire-protocol research after client updates. (source: wiki/sources/descriptions/hashblen__auto-discipher.md)

Complements static protobuf recovery such as [[protobuf-finder]], published schema dumps such as [[protobufs]], and generic wire decryptors such as [[packet-sniffer]].

## Links

- Repo: https://github.com/hashblen/auto-discipher (README: Rust library; live packet parse/decrypt; auto session tokens, achievement payloads, XOR keys)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[protobuf-finder]] · [[protobufs]] · [[packet-sniffer]]
