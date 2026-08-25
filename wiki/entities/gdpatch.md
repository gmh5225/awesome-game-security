---
title: GDPatch
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/GDPatch__GDPatch.md
updated: 2026-08-25
confidence: medium
---

# GDPatch

**GDPatch** (GDPatch/GDPatch) is a **cross-platform, cross-version mod loader** for **Godot Engine** games built around **runtime script patching and hooking**. Written primarily in **Rust**, it injects into game processes through a native loader and intercepts filesystem access to serve modified or virtualized game assets. The project includes **GDScript parsers and tokenizers** for Godot 3.x and 4.x, **Lua-based mod scripting**, and **usermode API hooks** on Windows, Linux, and macOS. Primary audience: Godot mod developers and reverse engineers who need to patch shipped GDScript, override pack files, and extend closed-source Godot titles at runtime without modifying game files on disk. (source: wiki/sources/descriptions/GDPatch__GDPatch.md)

Sits in the Godot runtime-modding lane beside Cheat Engine RE tooling such as [[gddumper]] (SceneTree / GDScript dump) and defensive sandbox addons such as [[godot-sandbox]]. Cross-engine mod-loader parallels include [[unreal-mod-loader]] and live-scripting stacks such as [[re-ue4ss]] on Unreal.

## Links

- Repo: https://github.com/GDPatch/GDPatch (Mod Loader)

## Related

[[godot]] · [[gddumper]] · [[godot-sandbox]] · [[gdmaim]] · [[better-godot-mcp]] · [[unreal-mod-loader]] · [[re-ue4ss]] · [[overviews/game-engine]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
