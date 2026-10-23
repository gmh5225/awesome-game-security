---
title: Ultimate Mortal Kombat 3 iOS Decompiled
kind: entity
topics: [game-hacking, reverse-engineering, mobile-security, graphics-api]
sources:
  - wiki/sources/descriptions/MaryNCRT__Ultimate-Mortal-Kombat-3-iOS-Decompiled.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: medium
---

# ultimate-mortal-kombat-3-ios-decompiled

Clean-room Ghidra decompilation of *Ultimate Mortal Kombat 3* (**iOS v1.2.59**, armv7) into verified C, plus a native cross-platform desktop port—documenting the LIME 3D engine, arcade fight logic, and proprietary binary formats while requiring a user-supplied IPA (no copyrighted assets in the repository). (source: wiki/sources/descriptions/MaryNCRT__Ultimate-Mortal-Kombat-3-iOS-Decompiled.md)

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
