---
title: aqhax-csgo
kind: entity
topics: [game-hacking, game-engine]
sources:
  - wiki/sources/descriptions/krxdev-kaan__AqHax-CSGO.md
updated: 2026-08-01
confidence: medium
---

# aqhax-csgo

C++ internal CS:GO cheat (**AqHax**) that hooks the Source engine SDK in-process. Implements ESP, aimbot, triggerbot, movement hacks, and skin changer through interface capture, VMT hooking, and netvar dumping—the same patterns as typical CS:GO internal cheats. Aimed at game-security researchers studying CS:GO cheat implementations and Source 1 hooking workflows. (source: wiki/sources/descriptions/krxdev-kaan__AqHax-CSGO.md)

Feature-complete internal sample; compare [[csgo-internal-base]] for a teaching-oriented scaffold and [[csgo-kns]] for a comparable VMT-hook baseline.

## Hooking model

| Mechanism | Role |
|-----------|------|
| Interface capture | Resolve Source exports (`IVEngineClient`, entity list, etc.) via CreateInterface |
| VMT hooking | Intercept virtual methods on engine/client interfaces |
| Netvar dumping | Walk ClientClass/RecvTable chains for entity property offsets |

See [[source-netvars]] for the netvar workflow and [[csgosimple]] for another Internal CS:GO baseline.

## Links

- Repo: https://github.com/krxdev-kaan/AqHax-CSGO

## Related

[[overviews/game-hacking]] · [[overviews/game-engine]] · [[source-netvars]] · [[csgo-internal-base]] · [[csgo-kns]] · [[csgosimple]] · [[tiny-csgo-client]] · [[vac3-inhibitor]]
