---
title: Pubg-Lite-ESP
kind: entity
topics: [game-hacking, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/gmh5225__Pubg-Lite-ESP.md
updated: 2026-08-10
confidence: medium
---

# Pubg-Lite-ESP

External **PUBG Lite** ESP cheat (gmh5225; cheat / game:pubg). Reads game memory out-of-process via **RPM**, resolves **UE4** engine structures (`GWorld`, `GameInstance`, `PlayerController`, `AcknowledgedPawn`) using hardcoded offsets, and performs **world-to-screen** projection via the camera view matrix. Renders player boxes, names, health bars, and distance indicators through a **Direct2D** overlay (Coltonon's D2DOverlay library) on a transparent window positioned over the game. Configurable render distance, bone ESP, and a hotkey-driven menu system. (source: wiki/sources/descriptions/gmh5225__Pubg-Lite-ESP.md)

Useful for game security researchers studying external overlay-based ESP with Direct2D rendering and UE4 offset-based entity enumeration—complementing broader PUBG external samples such as [[pubg-external-cheat]] and offset/SDK tooling such as [[pubg-dump-offset]] / [[pubg-dumper]].

## Links

- Repo: https://github.com/gmh5225/Pubg-Lite-ESP

## Related

[[world-to-screen]] · [[unreal-object-model]] · [[pubg-external-cheat]] · [[pubg-dump-offset]] · [[pubg-dumper]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/game-engine]]
