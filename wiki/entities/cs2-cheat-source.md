---
title: cs2-cheat-source
kind: entity
topics: [game-hacking, graphics-api, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/bootmgfw__CS2-Cheat-Source.md
updated: 2026-08-17
confidence: medium
---

# cs2-cheat-source

**cs2-cheat-source** (bootmgfw/CS2-Cheat-Source) is a C++ **internal** cheat for **Counter-Strike 2** that injects into the game process and modifies client-side cosmetic and input behavior. It implements weapon skin, glove, and knife changers backed by reverse-engineered Source 2 interfaces, schema data, and protobuf network message definitions. The project hooks game and DirectX 11 functions using MinHook and VMT detours, including Present and swap-chain callbacks for a Dear ImGui overlay menu and JSON-backed configuration system. Intended for game security researchers, anti-cheat developers, and reverse engineers studying CS2 client internals, hooking techniques, and how cosmetic cheats interact with the economy and rendering pipeline. (source: wiki/sources/descriptions/bootmgfw__CS2-Cheat-Source.md)

Sits in the in-process Source 2 internal cosmetic lane beside SDK scaffolds such as [[cs2-cheat-base]], feature samples such as [[cs2-cheat]] and [[asphyxia-cs2]], and header kits such as [[cs2-sdk]] and [[cs2-internal-sdk]]. Other bootmgfw title-specific samples include externals such as [[apex-external-cheat]], [[rust-external-cheat]], and [[valorant-external-cheat]] on [[lithium-kernel]], plus Unity internals such as [[eft-tarkov-internal-cheat]].

## Links

- Repo: https://github.com/bootmgfw/cs2-cheat-source (Internal CS2 cheat with skin/glove changer, DirectX hooks, and Source 2 SDK headers)

## Related

[[present-hook]] · [[source2gen]] · [[cs2-cheat-base]] · [[cs2-cheat]] · [[cs2-internal]] · [[cs2internal]] · [[asphyxia-cs2]] · [[cs2-sdk]] · [[cs2-internal-sdk]] · [[cs2-offsets]] · [[apex-external-cheat]] · [[eft-tarkov-internal-cheat]] · [[lithium-kernel]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
