---
title: saphire
kind: entity
topics: [game-hacking, graphics-api, game-engine]
sources:
  - wiki/sources/descriptions/M3351AN__saphire.md
updated: 2026-08-23
confidence: medium
---

# saphire

C++ **internal CS:GO cheat framework** from M3351AN with an **ImGui-based DirectX 9 overlay menu**, a **built-in code editor**, and a **modular cheat interface** with configuration support. The codebase integrates **FreeType** font rendering, **custom ImGui widgets**, and a menu layer aimed at Source engine games. Useful for game-security researchers studying cheat UI frameworks and ImGui overlay implementations on Source 1—not a production cheat guide. (source: wiki/sources/descriptions/M3351AN__saphire.md)

README-tagged `[Internal]`. Not to be confused with [[sapphire]] (FFXIV private-server emulator).

## Architecture highlights

| Component | Role |
|-----------|------|
| DirectX 9 + ImGui | In-process overlay menu on the game render path |
| FreeType | Custom font rendering in the ImGui UI |
| Custom ImGui widgets | Extended menu controls beyond stock Dear ImGui |
| Built-in code editor | In-menu scripting or config editing surface |
| Modular cheat interface | Pluggable feature modules with configuration support |

See [[csgo-cheat-base]], [[csgo-main-internal]], and [[kakhack]] for comparable internal CS:GO ImGui scaffolds; [[present-hook]] for the underlying D3D9 Present/EndScene overlay lane.

## Links

- Repo: https://github.com/M3351AN/saphire

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/game-engine]] · [[csgo-cheat-base]] · [[csgo-main-internal]] · [[csgo-ormbunke-x86]] · [[kakhack]] · [[imgui-advanced-cheat-menu]] · [[present-hook]]
