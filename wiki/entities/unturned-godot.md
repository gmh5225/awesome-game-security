---
title: unturned-godot
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/jlucaso1__unturned-godot.md
updated: 2026-08-03
confidence: medium
---

# unturned-godot

Experimental Godot 4.7 port that loads real Unturned maps, terrain, objects, audio, and characters from a local Steam install and renders them in a playable runtime. The project re-implements Unturned and Unity asset formats from scratch in C#—master bundle extraction, DAT parsing, heightmaps, navmeshes, compressed meshes, and FSB5 audio decoding—validated byte-for-byte against official game data using the U3-SDK as a serialization reference. (source: wiki/sources/descriptions/jlucaso1__unturned-godot.md)

Includes an engine-independent core library with extensive xUnit coverage, a Godot front end for world building and multiplayer, and editor tooling to preview maps and warm asset caches. Aimed at researchers and developers studying Unturned file formats, Unity bundle structures, and game data extraction—not at shipping a standalone game.

Complements Cheat Engine Godot runtime dumpers such as [[gddumper]] and authoring MCP such as [[better-godot-mcp]] on the Godot lane; sits beside Unity/UE offline asset explorers such as [[paksmith]] and [[jmap]] when the goal is title-specific serialized-format RE rather than live-process dumps.

## Links

- Repo: https://github.com/jlucaso1/unturned-godot

## Related

[[gddumper]] · [[better-godot-mcp]] · [[godot-sandbox]] · [[paksmith]] · [[jmap]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
