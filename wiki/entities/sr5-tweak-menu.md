---
title: SR5 Tweak Menu
kind: entity
topics: [game-hacking, graphics-api, reverse-engineering]
sources:
  - wiki/sources/descriptions/00xJS__SR5-Tweak-Menu.md
  - wiki/sources/README-categories.md
updated: 2026-10-31
confidence: high
---

# SR5 Tweak Menu

In-game tweak and cheat menu for **Saints Row (2022)** on PC, modeled after earlier Saints Row tweak menus and targeting the Epic **DirectX 12** build (00xJS). A **C** host shipped as **dinput8.dll** loads beside the game executable, **detours the main loop**, and hosts a **Lua 5.4** menu layer. That layer drives the title’s **native Lua interface** through injected scripts while exposing **memory read/write helpers** for live tuning—player stats, weapons, vehicles, teleport, world and AI controls, visuals, and built-in phone cheats, with optional persistence and a **save-clean** mode that avoids marking saves when certain in-game cheat flags are used. Bundled **Python** utilities and research notes document reflection **offsets**, **vtables**, **archive extraction**, and probing workflows for extending behavior in single-player modding and client reverse-engineering. (source: wiki/sources/descriptions/00xJS__SR5-Tweak-Menu.md)

Contrasts with Present-hook overlay stacks ([[present-hook]], [[directxhook]]) by combining **proxy-DLL injection**, **frame-loop detour**, and **in-engine Lua orchestration** rather than a standalone ImGui-on-swap-chain menu—closer in spirit to multi-API proxy frameworks such as [[gameplug]] but title-specific and script-driven.

## Architecture

| Layer | Role |
|-------|------|
| `dinput8.dll` proxy | Transparent load beside EXE; hooks main loop |
| C host | Detour + Lua 5.4 VM + memory R/W bridge |
| In-game Lua API | Script injection into the game’s own Lua surface |
| Python / notes | Offset, vtable, archive RE and extension probes |

## Links

- Repo: https://github.com/00xJS/SR5-Tweak-Menu (dinput8.dll host and in-game tweak/cheat menu for Saints Row (2022) DX12 (Epic))

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/graphics-api]] · [[present-hook]] · [[directxhook]] · [[gameplug]] · [[generic-game-detour-api-hook]] · [[xlua]]
