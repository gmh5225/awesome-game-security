---
title: Controller Mode
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/cheat-engine__ControllerMode.md
updated: 2026-08-17
confidence: medium
---

# Controller Mode

Official **Cheat Engine Lua add-on** (cheat-engine/ControllerMode) that maps Xbox-style gamepad input to the full Cheat Engine desktop UI so researchers can navigate and operate [[cheat-engine]] without a keyboard and mouse while attached to a target process. D-pad controls move through lists, tree views, and hex editors; A/B confirm and cancel; additional bindings cover tab switching, opening processes, and loading cheat tables. On-screen controller hint panels annotate forms, a controller-friendly file picker simplifies loading `.CT` tables, and experimental **Steam Deck on-screen keyboard** support is implemented via embedded C and the Steam API. (source: wiki/sources/descriptions/cheat-engine__ControllerMode.md)

Targets reverse engineers and memory analysts running CE on handheld or couch setups—especially Steam Deck—during game-security research and live memory editing.

## Links

- Repo: https://github.com/cheat-engine/ControllerMode

## Related

[[cheat-engine]] · [[unreal-engine-tools]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
