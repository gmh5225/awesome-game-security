---
title: GDMaim
kind: entity
topics: [game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/cherriesandmochi__gdmaim.md
updated: 2026-08-17
confidence: medium
---

# GDMaim

**GDMaim** is a Godot Engine 4.x editor plugin that automatically obfuscates GDScript when a project is exported, raising reverse-engineering cost for shipped builds without modifying the original project sources. Written primarily in GDScript, it renames identifiers, inlines constants and enums, strips comments and formatting, and can shuffle top-level declarations. It ships a source-map generator and viewer for debugging obfuscated builds, preprocessor hints for fine-grained control, and export-template feature tags to filter or disable obfuscation per platform. The plugin integrates the GDBC native library for additional string protection and targets Godot developers who need to deter decompilation tools and slow cheat authors analyzing client-side multiplayer logic. (source: wiki/sources/descriptions/cherriesandmochi__gdmaim.md)

Defensive reference under `Game Engine Protection:Godot` — export-time script hardening opposite live-process Godot RE tooling such as [[gddumper]] and complementary to engine authoring bridges like [[better-godot-mcp]].

## Links

- Repo: https://github.com/cherriesandmochi/gdmaim

## Related

[[gddumper]] · [[godot]] · [[better-godot-mcp]] · [[obfuz]] · [[static-variables-obfuscator-ue4]] · [[overviews/game-engine]] · [[overviews/reverse-engineering]]
