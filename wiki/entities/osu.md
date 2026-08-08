---
title: osu!
kind: entity
topics: [game-engine]
sources:
  - wiki/sources/descriptions/ppy__osu.md
  - wiki/sources/descriptions/ppy__osu-framework.md
updated: 2026-08-08
confidence: medium
---

# osu!

Open-source rhythm game (osu!) written in C# on [[osu-framework]]. Implements multiple modes (osu!standard, osu!taiko, osu!catch, osu!mania) with beatmap parsing, hit-object rendering, scoring, replay recording, online multiplayer, and skinning—plus custom UI, audio pipeline, input handling, and interpolation. Aimed at rhythm-game developers, C# game programmers, and the osu! modding community. (source: wiki/sources/descriptions/ppy__osu.md)

Sits in the Game Develop / source lane as a large managed C# title tree—useful for studying beatmap/replay formats, multiplayer, and framework-backed client architecture rather than as a cheat or anti-cheat artifact. Built on [[osu-framework]] (drawable scene graph / OpenGL abstraction / input·audio·UI). (source: wiki/sources/descriptions/ppy__osu-framework.md) Offensive AC analysis/bypass research such as [[osu-aac]] targets the proprietary osu! client's bot/input/time/memory checks from the opposite lane. Adjacent to other managed .NET engine/source samples ([[flatredball]], [[stride]]) and Game Develop remakes ([[zelda3]], [[mobademo]]).

## Links

- Repo: https://github.com/ppy/osu (README tag: [osu])

## Related

[[overviews/game-engine]] · [[overviews/overview]] · [[osu-framework]] · [[osu-aac]] · [[flatredball]] · [[stride]] · [[zelda3]] · [[mobademo]] · [[raylib]]
