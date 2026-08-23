---
title: League-of-Legends-Visuals-Cheat
kind: entity
topics: [game-hacking, graphics-api, anti-cheat]
sources:
  - wiki/sources/descriptions/Vatrials__League-of-Legends-Visuals-Cheat.md
updated: 2026-08-19
confidence: medium
---

# League-of-Legends-Visuals-Cheat

**Internal League of Legends cheat** (Vatrials; cheat / game:lol). C++ **Visual Studio** solution with a Windows **injector** (C++/CLI UI) that loads a DLL such as [[r3nzskin]] into `League of Legends.exe`. Ships a **skin changer** with skin database, **orbwalker** automated attack targeting, **spell prediction**, champion-specific scripting (for example Morgana), and a **zoom hack** that adjusts camera limits. Rendering and overlays use **ImGui** with **DirectX 9**; memory interaction relies on hardcoded game offsets, **Microsoft Detours**, and **VMT-style hooks**. Primary use case is reverse engineering and studying LoL client internals, injection, and cheat techniques for game-security research. (source: wiki/sources/descriptions/Vatrials__League-of-Legends-Visuals-Cheat.md)

Complements upstream skin changers such as [[r3nzskin]], skin-only samples such as [[r3nzskin-tft]] and [[league-skin-changer]], cheat bases such as [[league-base]], and scripting platforms such as [[leaguesharp]] and [[elobuddy-addons]] rather than dump-only or external tooling.

## Architecture highlights

| Component | Role |
|-----------|------|
| Injector (C++/CLI UI) | Loads internal DLL into LoL client process |
| Skin changer + DB | Client-side cosmetic swaps with champion skin data |
| Orbwalker | Automated attack-move targeting |
| Spell prediction / scripts | Champion-specific automation (e.g. Morgana) |
| Zoom hack | Camera limit adjustment |
| ImGui + DirectX 9 | In-process overlay rendering |
| Detours + VMT hooks | Function interception on game/engine paths |
| Hardcoded offsets | Direct memory reads/writes against client layouts |

## Links

- Repo: https://github.com/Vatrials/League-of-Legends-Visuals-Cheat

## Related

[[vanguard]] · [[r3nzskin]] · [[r3nzskin-tft]] · [[league-skin-changer]] · [[league-base]] · [[league-directx11-internal]] · [[leaguesharp]] · [[elobuddy-addons]] · [[present-hook]] · [[imgui]] · [[overviews/game-hacking]] · [[overviews/graphics-api]] · [[overviews/anti-cheat]]
