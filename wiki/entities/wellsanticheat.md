---
title: Wells Anti Cheat
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/somewhatpublicacc__wellsanticheat.md
updated: 2026-07-22
confidence: medium
---

# Wells Anti Cheat

Host-side BepInEx moderation plugin for Among Us that protects lobbies with automatic detection and optional kick or ban. Written in C# for .NET 6 with Harmony patches; inspects player RPCs for offensive names, chat spam, crash attempts, RPC floods, illegal vents, lobby teleports, task spoofing, and related cheat patterns. (source: wiki/sources/descriptions/somewhatpublicacc__wellsanticheat.md)

Only the host can discard RPCs or punish players; the host is always exempt, and non-hosts still receive notifications without enforcement. Also offers meeting grace timing, a modded-lobby mode to reduce false positives with role mods, and host tools such as map hotswap and force win. Aimed at lobby hosts who want lightweight anti-cheat and moderation without kernel or server-authoritative products such as [[easy-anti-cheat]], [[certael]], or [[magnetite]].

## Links

- Repo: https://github.com/somewhatpublicacc/wellsanticheat

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[certael]] · [[magnetite]]
