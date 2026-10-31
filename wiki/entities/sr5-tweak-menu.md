---
title: SR5 Tweak Menu
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/00xJS__SR5-Tweak-Menu.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: medium
---

# SR5 Tweak Menu

In-game tweak and cheat menu for **Saints Row (2022)** on PC (Epic **DirectX 12** build), modeled after earlier Saints Row tweak menus. A C host built as **dinput8.dll** loads beside the game executable, detours the main loop, and runs a **Lua 5.4** menu that drives the title’s own Lua interface through injected scripts while exposing memory read/write helpers for live tuning. Covers player stats, weapons, vehicles, teleport, world/AI controls, visuals, and built-in phone cheats, with optional persistence and a save-clean mode that avoids marking saves when using certain in-game cheat flags. Python utilities and research notes document reflection offsets, vtables, archive extraction, and probing workflows for single-player modding and security research. (source: wiki/sources/descriptions/00xJS__SR5-Tweak-Menu.md)

Illustrates **proxy-DLL main-loop detour** + in-engine Lua scripting beside D3D12 hook stacks in the DirectX Hook lane.

## Links

- Repo: https://github.com/00xJS/SR5-Tweak-Menu

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[draw-call-hook]] · [[present-hook]]
