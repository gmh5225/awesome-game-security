---
title: MapleStory Server (HeavenMS)
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__MapleStory-Server.md
updated: 2026-08-11
confidence: medium
---

# MapleStory Server (HeavenMS)

**MapleStory** private-server emulator based on **HeavenMS Server** (gmh5225): implements authoritative game-server functionality including player authentication, character progression, quest management, party systems, and world simulation for hosting custom MapleStory gameplay. (source: wiki/sources/descriptions/gmh5225__MapleStory-Server.md)

Useful for game security researchers and private-server developers studying MapleStory server architecture, protocol handling, and authoritative game systems—not client-side cheat tooling.

Complements the from-scratch HeavenClient such as [[maplestory-heavenclient]] (game protocol / rendering / UI; open-source private-server client), modified HeavenMS client builds such as [[maplestory-client]] (rendering / network protocol / UI; private-server connectivity), GM/admin clients such as [[maplestory-gm-client]] (map editing / NPC spawn / item creation / GM commands), and other MapleStory private-server emulators such as [[rebirth]] (GMS-095 C#), [[maplestory143]] (CMS-143 Java/Kotlin), [[maplestory-v83-maplestory-cpp]] (GMS-083 C++), [[mapleserver-android]] (GMS-083 on Android), [[maplestory-v113-server-eimulator]] (TMS-113), [[jmsv186]] (JMS-186), [[azurev316]] (KMS-316), [[mnwvs196]] (TMS-196 C++ research stack), and [[rustms]] (Rust).

## Links

- Repo: https://github.com/gmh5225/MapleStory-Server (README tag: HeavenMS Server)

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[maplestory-heavenclient]] · [[maplestory-client]] · [[maplestory-gm-client]] · [[rebirth]] · [[maplestory143]] · [[maplestory-v83-maplestory-cpp]] · [[mapleserver-android]] · [[maplestory-v113-server-eimulator]] · [[jmsv186]] · [[azurev316]] · [[mnwvs196]] · [[rustms]]
