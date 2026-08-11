---
title: LeagueSharp
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__LeagueSharp.md
  - wiki/sources/descriptions/gmh5225__LeagueSharp.Loader.md
updated: 2026-08-11
confidence: medium
---

# LeagueSharp

**League of Legends scripting and modding platform** with multiple tool modules (gmh5225; cheat / game:lol). Ships **JungleTimerHax** for spectator-based jungle timers, **SkinHax** for in-game skin changes, and champion resize utilities that call **LoL internal APIs**—aimed at game security researchers studying modular in-guest scripting and cosmetic/mod manipulation under [[vanguard]]. (source: wiki/sources/descriptions/gmh5225__LeagueSharp.md)

Complements cheat bases such as [[league-base]], external script platforms such as [[ayaya-league-external]], and skin changers such as [[league-skin-changer]] and [[r3nzskin-tft]] rather than dump-only or wire/protocol client tooling. Bootstrap/injection is handled by companion loader samples such as [[leaguesharp-loader]] (C#; DirectX + hooking; gmh5225). (source: wiki/sources/descriptions/gmh5225__LeagueSharp.Loader.md)

## Links

- Repo: https://github.com/gmh5225/LeagueSharp

## Related

[[vanguard]] · [[leaguesharp-loader]] · [[league-base]] · [[ayaya-league-external]] · [[league-skin-changer]] · [[r3nzskin-tft]] · [[lol-offset-dumper]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
