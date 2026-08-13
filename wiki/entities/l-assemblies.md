---
title: L-Assemblies
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__L-Assemblies.md
updated: 2026-08-12
confidence: medium
---

# L-Assemblies

Collection of **C# LeagueSharp plugin assemblies** for League of Legends (gmh5225; cheat / game:lol). Ships automated champion scripts for Annie, Cassiopeia, Cho'Gath, Darius, Evelynn, and Katarina plus a ward/summoner spell cooldown tracker with minimap overlay—aimed at game security researchers studying scripting platform plugin architectures and automated gameplay logic under [[vanguard]]. (source: wiki/sources/descriptions/gmh5225__L-Assemblies.md)

Each champion module implements combo logic, spell casting sequences, and target selection via the LeagueSharp SDK **Orbwalker**, **TargetSelector**, and **Spell prediction** APIs; the tracker draws cooldown indicators and ward positions on the HUD through **Drawing.OnDraw** callbacks. Complements the [[leaguesharp]] platform and [[leaguesharp-loader]] bootstrap rather than cheat bases or dump tooling.

## Links

- Repo: https://github.com/gmh5225/L-Assemblies

## Related

[[leaguesharp]] · [[leaguesharp-loader]] · [[elobuddy-addons]] · [[league-base]] · [[lviewlol]] · [[vanguard]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
