---
title: EFT MonoEFT
kind: entity
topics: [game-hacking, game-engine, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__EFT-MonoEFT.md
updated: 2026-08-13
confidence: medium
---

# EFT MonoEFT

**MonoEFT** is a Mono-based **internal** cheat for **Escape From Tarkov** written in C# that hooks the Unity/Mono runtime. It provides ESP (box, name, distance, health bars), silent aim, no-recoil, speed hacks, infinite stamina, and loot ESP through method hooking and direct game-object manipulation in the cheat / game:eft lane. Aimed at game security researchers studying Mono/.NET injection, Unity game-object introspection, and method-hooking attack surfaces on BattlEye-protected Unity titles. (source: wiki/sources/descriptions/gmh5225__EFT-MonoEFT.md)

## Implementation notes

- Enumerates players by walking `GameWorld.RegisteredPlayers`
- Reads `PlayerBones` for skeleton-based [[world-to-screen]] projection via `Camera.WorldToScreenPoint`
- Hooks shot pipeline methods such as `CreateShot`, `ApplyShot`, and `BulletMovement` for bullet manipulation
- Renders overlays with Unity `OnGUI` / `GUI.DrawTexture` and an ImGui-style menu

Complements discontinued Mono-era trainers such as [[escapefromtarkov-trainer]], IL2CPP memory-read frameworks such as [[eft-veil-eft]] and [[eft-newtarkov-cheatproject]], C++ internal samples such as [[eft-internal]], and external DMA radar stacks such as [[meatyeftrelease]] and [[eft-dma-radar-1]] for comparing Mono method-hooking internals vs post-[[il2cpp]] overlays and below-OS externals.

## Links

- Repo: https://github.com/gmh5225/EFT-MonoEFT

## Related

[[mono]] · [[escapefromtarkov-trainer]] · [[eft-veil-eft]] · [[eft-newtarkov-cheatproject]] · [[eft-internal]] · [[simple-eft-base]] · [[meatyeftrelease]] · [[eft-dma-radar-1]] · [[world-to-screen]] · [[il2cpp]] · [[battleye]] · [[overviews/game-hacking]] · [[overviews/game-engine]]
