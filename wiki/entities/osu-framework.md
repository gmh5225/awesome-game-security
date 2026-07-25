---
title: osu!framework
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/ppy__osu-framework.md
updated: 2026-07-25
confidence: medium
---

# osu!framework

C# game framework built for [[osu]] but usable as a general-purpose 2D game engine. Provides a scene graph with drawable hierarchies, input handling, audio management, threading model, smooth interpolation, text rendering, texture atlasing, and platform abstraction over OpenGL—plus game-loop timing, resource management, and UI layout. Aimed at C# game developers wanting a well-tested 2D framework with modern .NET features. (source: wiki/sources/descriptions/ppy__osu-framework.md)

Sits in the Game Engine / managed 2D framework lane beside [[flatredball]] and [[stride]]—useful for studying drawable trees, input/audio pipelines, and OpenGL-backed client architecture rather than as a cheat or anti-cheat artifact. Powers the open-source [[osu]] rhythm-game client (Game Develop / source).

## Links

- Repo: https://github.com/ppy/osu-framework (README tag: [osu])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[osu]] · [[flatredball]] · [[stride]] · [[raylib]] · [[mojoc]]
