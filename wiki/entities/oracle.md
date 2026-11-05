---
title: Oracle (Arkham Knight)
kind: entity
topics: [game-hacking]
sources:
  - wiki/sources/descriptions/XeTrinityz__Oracle.md
updated: 2026-11-05
confidence: medium
---

# Oracle (Arkham Knight)

**Oracle Trinity Edition** is a modular in-game cheat and tweak menu for **Batman: Arkham Knight** on PC, built as a **BmSDK-AK** mod and opened with **F3** or a controller. The project is primarily **C#**, a ground-up rebuild of the original Oracle mod: a small kernel, per-feature modules, **guarded game hooks** that log failures instead of crashing, and **clean unload** that restores changed values. The menu adds searchable pages, favourites on a radial wheel, combat automation (including a trainable auto-fight brain), teleport and world controls, an in-world editor, free camera and Batmobile tooling, save management, and optional custom music playback via `settings.toml`. It targets players and mod developers who want deep runtime control in a **single-player** Arkham Knight session—not online anti-cheat or live-service tooling. (source: wiki/sources/descriptions/XeTrinityz__Oracle.md)

Architecturally it sits beside other title-specific PC tweak menus such as [[sr5-tweak-menu]] (proxy-DLL + in-engine scripting) but uses the **BmSDK-AK** mod host and a modular C# feature kernel rather than a Lua proxy loop.

## Links

- Repo: https://github.com/XeTrinityz/Oracle (MIT; BmSDK-AK Trinity Edition)

## Related

[[overviews/game-hacking]] · [[sr5-tweak-menu]] · [[cheat-attack-surface]]
