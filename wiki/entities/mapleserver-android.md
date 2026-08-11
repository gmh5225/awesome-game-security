---
title: MapleServer Android
kind: entity
topics: [game-hacking, game-engine, mobile-security]
sources:
  - wiki/sources/descriptions/gmh5225__MapleServerAndroid.md
updated: 2026-08-11
confidence: medium
---

# MapleServer Android

**MapleStory GMS-083** private-server implementation designed to run on **Android** devices (gmh5225): provides server-side game logic, character management, and world simulation for hosting MapleStory gameplay on mobile platforms. (source: wiki/sources/descriptions/gmh5225__MapleServerAndroid.md)

Useful for game security researchers studying how authoritative MMO server stacks port to mobile hardware, and for private-server developers comparing desktop emulators with on-device hosting—not client-side cheat tooling.

Complements desktop GMS-083 stacks such as [[maplestory-v83-maplestory-cpp]] (C++; editor tooling / modding / SDK generation), HeavenMS-based server emulators such as [[maplestory-server]] (player auth / character progression / quest / party / world simulation), and other MapleStory private-server emulators such as [[rustms]] (Rust), [[rebirth]] (GMS-095 C#), and [[maplestory-v113-server-eimulator]] (TMS-113).

## Links

- Repo: https://github.com/gmh5225/MapleServerAndroid (README tag: GMS 083 server on Android)

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/mobile-security]] · [[maplestory-v83-maplestory-cpp]] · [[maplestory-server]] · [[rustms]] · [[rebirth]] · [[maplestory-v113-server-eimulator]]
