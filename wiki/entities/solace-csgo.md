---
title: solace-csgo
kind: entity
topics: [game-hacking, anti-cheat, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/emilyinure__solace-csgo.md
updated: 2026-08-15
confidence: medium
---

# solace-csgo

**Solace** is a modern C++ internal CS:GO cheat with a polished **ImGui** menu. It hooks the Source engine SDK in-process and ships ESP, aimbot, triggerbot, movement assistance (bunny hop, auto-strafe), skin changer, and visual modifications in a modular, well-structured codebase aimed at game-security researchers studying CS:GO cheat design patterns and anti-cheat detection surfaces. (source: wiki/sources/descriptions/emilyinure__solace-csgo.md)

README tags it `[Internal]`. Compare [[csgo-internal-base]] for a teaching-oriented scaffold, [[aqhax-csgo]] for a comparable feature-complete internal stack, and [[csgo-alphen]] for another SDK-backed ImGui internal sample.

## Feature stack

| Module | Role |
|--------|------|
| Source SDK hooking | In-process engine/client interface interception |
| ESP / aimbot / triggerbot | Combat and awareness features |
| Movement (bhop, auto-strafe) | Input and movement automation |
| Skin changer / visuals | Cosmetic and rendering modifications |
| ImGui menu | Polished in-game overlay for configuration |

## Links

- Repo: https://github.com/emilyinure/solace-csgo

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[csgo-internal-base]] · [[aqhax-csgo]] · [[csgo-alphen]] · [[csgosimple]] · [[source-netvars]] · [[imgui]] · [[vac3-inhibitor]]
