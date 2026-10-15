---
title: axis-web
kind: entity
topics: [reverse-engineering, game-engine, graphics-api]
sources:
  - wiki/sources/descriptions/reikop__axis-web.md
updated: 2026-10-15
confidence: medium
---

# axis-web

Browser port of the 2005 Korean 3D action game **AXIS**, built by reverse-engineering the original OpenGL client and reimplementing its logic in **C** compiled to **WebAssembly**, with **WebGL**, **WebAudio**, and **WebSocket** platform layers. The project maintains a living reverse-engineering spec for file formats and networking, ships Python and JavaScript tooling, and includes eight **byte-exact decoders** (archives, encryption, textures, meshes, maps, skeletons, replays, match RNG) verified against a legally owned install. A walkable WebGL engine, local viewers, and a WebSocket relay support real-protocol multiplayer, with movement kinematics and **RNG lockstep** reconstruction checked against recorded matches. Targets researchers studying classic clients, proprietary asset pipelines, and deterministic online play; **no copyrighted assets** ship in the repo—users supply their own game copy. (source: wiki/sources/descriptions/reikop__axis-web.md)

## Links

- Repo: https://github.com/reikop/axis-web (README: reverse-engineered AXIS client as WebAssembly/WebGL with byte-exact asset decoders and multiplayer protocol research)

## Related

[[overviews/reverse-engineering]] · [[overviews/game-engine]] · [[overviews/graphics-api]] · [[zelda3]] · [[webcheat]] · [[awesome-game-file-format-reversing]]
