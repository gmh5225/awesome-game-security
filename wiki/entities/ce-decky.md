---
title: CE Decky
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/goooroooX__CE-Decky.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: high
---

# CE Decky

**CE Decky** (goooroooX/CE-Decky) is a **Decky Loader** plugin that brings **Cheat Engine** to Steam Deck and SteamOS by managing cheat tables and launching official or user-imported Windows Cheat Engine inside each game’s Proton prefix. A Python backend, TypeScript/JavaScript Game Mode UI, and Lua bridge into Cheat Engine support community table search/download, local library management, compatibility review, and in-session toggles from the Quick Access Menu without Desktop Mode. (source: wiki/sources/descriptions/goooroooX__CE-Decky.md)

## Architecture

| Layer | Role |
|-------|------|
| Python backend | Table library, Proton-prefix CE lifecycle, Steam metadata validation |
| TypeScript/JavaScript UI | Decky **Game Mode** panel (not Desktop Mode) |
| Lua bridge | Drives in-process CE for scan/toggle workflows from the plugin |

Community sources feed table search and download; a local library holds `.CT` assets with compatibility review before attach. Cheat exposure is surfaced as Quick Access Menu toggles for the active session.

## Integration

The plugin uses Steam library and launch metadata to validate targets and attach to the correct Windows executable without modifying Steam configuration. Features include auto-load, table repair for mismatched game builds, Authenticode-checked managed installs, and strict session lifecycle controls—oriented toward players and researchers who want structured memory editing and `.CT` workflows on handheld Linux gaming hardware (Proton/SteamOS). (source: wiki/sources/descriptions/goooroooX__CE-Decky.md)

## Positioning

Listed under **Cheat → Cheat Engine Plugins** beside official CE Lua extensions such as [[unreal-engine-tools]], [[controller-mode]], and [[aitools]]. [[controller-mode]] improves in-CE gamepad navigation when CE runs inside the prefix; CE Decky wraps install, table curation, and QAM toggles around that stack. Complements Linux-native memory UIs such as [[pince]], Proton trainer panels such as [[archmod]], and external MCP bridges such as [[cheatengine-mcp-bridge]] when researchers need full CE semantics on Deck-class devices.

## Links

- Repo: https://github.com/goooroooX/CE-Decky

## Related

[[cheat-engine]] · [[aitools]] · [[unreal-engine-tools]] · [[controller-mode]] · [[archmod]] · [[cheatengine-mcp-bridge]] · [[pince]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
