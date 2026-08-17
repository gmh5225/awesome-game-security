---
title: cs2-sdk
kind: entity
topics: [game-hacking, game-engine, reverse-engineering, graphics-api]
sources:
  - wiki/sources/descriptions/gmh5225__cs2_sdk.md
  - wiki/sources/descriptions/gmh5225__cs2-sdk.md
  - wiki/sources/descriptions/bruhmoment21__cs2-sdk.md
updated: 2026-08-17
confidence: medium
---

# cs2-sdk

Multiple Counter-Strike 2 Source 2 SDK repos share this name in the curated list. They supply C/C++ headers and scaffolding for cheat / game:cs2 research—entity classes, engine interfaces, and hook-oriented type systems.

## gmh5225/cs2_sdk

C/C++ **Counter-Strike 2** SDK focused on **SDK generation** for the **Source 2** engine—headers and scaffolding for entity classes, engine interfaces, and cheat-oriented type systems. Emphasis areas include **driver development**, **rendering**, and **networking**. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / game:cs2 lane. (source: wiki/sources/descriptions/gmh5225__cs2_sdk.md)

## gmh5225/cs2-sdk

Simplified CS2 SDK written as close as possible to **Source 2** code, supporting both **DirectX 11** and **Vulkan** graphical APIs. Aimed at game-security researchers and reverse engineers studying offensive techniques in the cheat / game:cs2 lane. (source: wiki/sources/descriptions/gmh5225__cs2-sdk.md)

## bruhmoment21/cs2-sdk

Cross-platform C++ CS2 SDK for **Windows** and **Linux** with **DirectX 11** and **Vulkan** rendering backends. Simplified **Source 2** layout kept close to original engine code; includes game-manipulation hooks and an **ImGui** menu. Injection via `LoadLibrary` on Windows and `dlopen` on Linux; manual mapping requires specific compiler flags. Useful for studying Source 2 engine internals and CS2 SDK structures across platforms. (source: wiki/sources/descriptions/bruhmoment21__cs2-sdk.md)

Sits beside generated SDK tooling such as [[source2gen]] and [[source2sdk]], maintained offset feeds such as [[cs2-offsets]], and research collections such as [[cs2-things]] as a CS2 layout and interface artifact.

## Links

- Repo (cs2_sdk): https://github.com/gmh5225/cs2_sdk
- Repo (cs2-sdk, gmh5225): https://github.com/gmh5225/cs2-sdk
- Repo (cs2-sdk, bruhmoment21): https://github.com/bruhmoment21/cs2-sdk

## Related

[[cs2-cheat-base]] · [[cs2-things]] · [[cs2-offsets]] · [[cs2-offsets-ro0ti]] · [[source2gen]] · [[source2sdk]] · [[csgo-sdk]] · [[source-netvars]] · [[overviews/game-hacking]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[overviews/reverse-engineering]]
