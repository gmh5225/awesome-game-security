---
title: apexdream
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/CasualX__apexdream.md
updated: 2026-08-29
confidence: medium
---

# apexdream

Rust library and Win32 example for an **external Apex Legends cheat** that attaches to the game process and drives features from live memory. Includes aim assist with per-weapon trigger settings, ESP and radar overlays, recoil control, player highlighting, and projectile prediction backed by a game SDK for entities, weapons, and related state. The companion **apexdumper** tool uses pelite-based PE analysis to recover offsets such as classes, convars, datamaps, recv tables, and interfaces into `gamedata.ini`. Aimed at game-hacking and reverse-engineering research on Respawn/Source-style Apex Legends internals and external memory tooling (cheat / game:apex legends [External]; embeddable API). (source: wiki/sources/descriptions/CasualX__apexdream.md)

Sits beside live-process Apex offset dumpers such as [[apex-legends-offset-dumper]] and static SDK trees such as [[apex-legends-sdk]] / [[apex-legends-sdk-remaster]]. Same author family as [[apexbot]] (backend-embeddable modular Rust external framework) and [[obfstr]] (Rust compile-time string obfuscation).

## Links

- Repo: https://github.com/CasualX/apexdream

## Related

[[apexbot]] · [[easy-anti-cheat]] · [[apex-legends-offset-dumper]] · [[apex-legends-sdk]] · [[apex-legends-sdk-remaster]] · [[apex-external]] · [[obfstr]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
