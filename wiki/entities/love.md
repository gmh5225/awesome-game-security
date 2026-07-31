---
title: LOVE (Love2D)
kind: entity
topics: [game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/love2d__love.md
updated: 2026-07-31
confidence: medium
---

# LOVE (Love2D)

Free open-source 2D game framework: C++ core with Lua scripting, OpenGL/Metal graphics, Box2D physics, audio, windowing, input, threading, and filesystem modules exposed through a simple Lua API. Games ship as `.love` archive files (ZIP containers of Lua scripts and assets) aimed at indie developers and hobbyists prototyping 2D titles with minimal boilerplate. (source: wiki/sources/descriptions/love2d__love.md)

## Security-relevant surfaces

- **Lua runtime** — gameplay logic lives in interpreted Lua; modding, hooking, and script injection are straightforward compared to compiled-only titles.
- **`.love` packaging** — plain ZIP distribution makes asset/script extraction and repackaging trivial for RE and tampering workflows.
- **Graphics backends** — OpenGL/Metal render paths align with standard [[present-hook]] and overlay research on desktop targets.

Sits in the Game Engine / 2D source lane beside [[macroquad]], [[raylib]], and [[orx]] — an approachable OSS framework rather than a cheat or anti-cheat artifact.

## Links

- Repo: https://github.com/love2d/love (README: [2D game framework for Lua])

## Related

[[overviews/game-engine]] · [[overviews/graphics-api]] · [[macroquad]] · [[raylib]] · [[orx]] · [[present-hook]]
