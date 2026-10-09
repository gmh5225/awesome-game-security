---
title: Sky-CotL-Scripts
kind: entity
topics: [game-hacking, mobile-security]
sources:
  - wiki/sources/descriptions/thatskymod__Sky-CotL-Scripts.md
  - wiki/sources/README-categories.md
updated: 2026-10-09
confidence: medium
---

# Sky-CotL-Scripts

**Sky-CotL-Scripts** (thatskymod/Sky-CotL-Scripts) is a curated hub for modifying and researching **Sky: Children of the Light** on Android and PC—not a single shipped cheat binary. (source: wiki/sources/descriptions/thatskymod__Sky-CotL-Scripts.md)

README category: Cheat / **Memory Explorer** — Sky: Children of the Light mod/script hub (Canvas Android modloader, GameGuardian, Lua scripts, PC/Steam assets, virtual-space setups).

## Capabilities

Bundles **GameGuardian Lua** for runtime memory editing: teleports, map coordinates, cosmetics, winged light, game speed, FPS tweaks, and related client-side cheats. Documents the **Canvas** Android mod-loader workflow, ships native helpers such as **libTSM**, and includes helper APKs for app cloning and virtual multi-account spaces. Preserves legacy Lua with documented memory offsets plus educational notes on **server-side outfit validation** and mod safety. On PC, a **Frida JavaScript** hook intercepts the game’s HTTP traffic for protocol and live-service analysis. (source: wiki/sources/descriptions/thatskymod__Sky-CotL-Scripts.md)

## Architecture

Resource collection rather than one build artifact: Lua script packs (GameGuardian + historical offset tables), mod-loader docs, native libraries, virtualization APKs, and PC-side Frida JS sit beside Steam/Android asset references. Android paths assume rooted GameGuardian or Canvas injection; PC paths pair Steam client analysis with Frida attach for TLS/HTTP visibility. (source: wiki/sources/descriptions/thatskymod__Sky-CotL-Scripts.md)

## Positioning

Targets reverse engineers, security researchers, and advanced players studying **live-service** client behavior, memory layout, and anti-abuse limits—contrasts with generic Android memory platforms such as [[ace-the-game]] and [[charlyengine]] by focusing on one title’s mod ecosystem, virtual-space multi-account setups, and documented server validation edges. PC Frida HTTP hooks complement mobile memory edits for end-to-end client–server RE.

## Links

- Repo: https://github.com/thatskymod/Sky-CotL-Scripts

## Related

[[frida]] · [[charlyengine]] · [[ace-the-game]] · [[android-mod-loader]] · [[virtual-app]] · [[mobile-anti-cheat]] · [[overviews/game-hacking]] · [[overviews/mobile-security]]
