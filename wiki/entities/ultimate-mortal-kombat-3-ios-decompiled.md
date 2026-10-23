---
title: Ultimate Mortal Kombat 3 iOS Decompiled
kind: entity
topics: [game-hacking, reverse-engineering, mobile-security, graphics-api]
sources:
  - wiki/sources/descriptions/MaryNCRT__Ultimate-Mortal-Kombat-3-iOS-Decompiled.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: high
---

# Ultimate Mortal Kombat 3 iOS Decompiled

**MaryNCRT/Ultimate-Mortal-Kombat-3-iOS-Decompiled** is a clean-room **Ghidra** decompilation of the 2011 iOS release of *Ultimate Mortal Kombat 3* (**v1.2.59**, armv7): all **2,572** game functions transcribed into verified C and wrapped in a playable native desktop port. The tree documents the **LIME 3D** engine, arcade fight logic, and proprietary binary formats; builds require a user-supplied **IPA** (no copyrighted assets shipped). (source: wiki/sources/descriptions/MaryNCRT__Ultimate-Mortal-Kombat-3-iOS-Decompiled.md)

## Positioning

Listed under **Cheat / Source** beside Switch static-recomp ports such as [[smo-recomp]] and [[letsgo-recomp]]—a preservation-oriented reference for recovering classic fighting-game logic from shipped **Mach-O** mobile binaries with differential verification rather than runtime hooks.

## Stack

- **Lift / verify:** Python unified build from IPA; Java and custom **armrecomp** tooling; differential tests against the shipped Mach-O binary (~2,572 functions transcribed).
- **Runtime:** C/CMake; Win32 and SDL2 hosts with **OpenGL**, **Vulkan**, and **D3D12** backends.
- **Workflow:** Electron launcher for mod and asset export paths beside preservation-oriented RE notes.

## Research hooks

Useful for studying iOS game binary recovery, static recompilation verification, and how classic fighting-game logic is separated from platform services when porting armv7 mobile builds to desktop GPUs. Pair lift claims with differential/oracle evidence per [[static-runtime-evidence]].

## Audience

Reverse engineers and preservationists; players who legally own the title and supply their own IPA.

## Links

- Repo: https://github.com/MaryNCRT/Ultimate-Mortal-Kombat-3-iOS-Decompiled

## Related

[[letsgo-recomp]] · [[smo-recomp]] · [[sf33rdsxbrecompo]] · [[static-runtime-evidence]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[overviews/mobile-security]] · [[overviews/graphics-api]]
