---
title: GDDumper
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/palepine__GDDumper.md
updated: 2026-07-28
confidence: medium
---

# GDDumper

Cheat Engine Lua script that dumps and inspects Godot 3.x/4.x runtime data on Windows x86-64 and x32. Resolves offsets automatically, dumps SceneTree/nodes into Cheat Engine Address Lists, and dissects root-node structures. Includes a structure-based GDScriptFunction disassembler plus experimental GDFunction calling and GDScript/ScriptInstance hot-reload, with a basic GD-to-Cheat Engine API. Aimed at GDScript-heavy Godot apps for educational RE, modding, and debugging. (source: wiki/sources/descriptions/palepine__GDDumper.md)

Fills the Godot side of the engine-explorer lane opposite Unity tooling such as [[unityexplorer]] / [[il2cpp-runtime-dumper]] and Unreal dumpers such as [[ts-ue4dumper]]. Sits beside general Cheat Engine workflows ([[memmcp]], [[cedetector]]) when the target is live Godot process memory rather than offline asset unpack.

## Links

- Repo: https://github.com/palepine/GDDumper

## Related

[[unityexplorer]] · [[il2cpp-runtime-dumper]] · [[ts-ue4dumper]] · [[memmcp]] · [[cedetector]] · [[game-engine-detector]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
