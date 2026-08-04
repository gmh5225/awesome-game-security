---
title: Goldberg Steam Emulator
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/inflation__goldberg_emulator.md
updated: 2026-08-04
confidence: medium
---

# Goldberg Steam Emulator

C++ **Steamworks API compatibility layer** that emulates Steam API calls without connecting to Steam servers. Replaces `steam_api.dll` / `steam_api64.dll` to run Steam-dependent games offline, with local emulation of achievements, leaderboards, matchmaking, overlay, and DLC ownership checks. Supports LAN multiplayer via direct network broadcasting. Aimed at game preservation, modding, and researchers studying Steam DRM and API dependencies. (source: wiki/sources/descriptions/inflation__goldberg_emulator.md)

Sits in the Cheat → **Steam emulator** / Launcher Abuser lane beside [[mini-launcher]] (lighter launcher stub) and platform-overlay research such as [[steam-overlay-x64]]. Complements VAC-focused tooling ([[vacation3-emu]], [[vac3-inhibitor]]) when the research target is **Steamworks client API surface** rather than anti-cheat modules.

## Links

- Repo: https://github.com/inflation/goldberg_emulator

## Related

[[mini-launcher]] · [[steam-overlay-x64]] · [[steam-anti-anti-debug]] · [[vacation3-emu]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
