---
title: S2Arm Cheat HUD
kind: entity
topics: [game-hacking]
sources:
  - wiki/sources/descriptions/Lariya-aa__s2arm-cheat-hud.md
updated: 2026-11-20
confidence: medium
---

# S2Arm Cheat HUD

Standalone **macOS** application that provides a lightweight, non-intrusive in-game cheat overlay for **S2Arm**, the native Switch **ARM64→Metal** runtime on Apple Silicon. Built in **Swift** with AppKit, SwiftUI, **GameController**, and Carbon hotkey registration, it stays fully **external** to S2Arm—no process injection or binary tampering. The HUD uses a non-activating **NSPanel** summoned during fullscreen play via **L3+R3** or **Option+Z**, syncs cheat toggles with S2Arm’s cheat engine through `enabled.txt` and `status.txt`, and supports safer one-shot **pulse** injection plus hook-address conflict detection for Atmosphere-style cheat files. Specialized injectors include dynamic pointer chains for *The Legend of Zelda: Ocarina of Time*; a small Python utility normalizes cheat definitions. Targets players and researchers who want console-style in-game cheat menus on macOS while managing S2Arm cheats in real time, akin to classic handheld overlays such as CWCheat, VitaCheat, and EdiZon. (source: wiki/sources/descriptions/Lariya-aa__s2arm-cheat-hud.md)

## Links

- Repo: https://github.com/Lariya-aa/s2arm-cheat-hud (README: macOS non-activating floating cheat menu; gamepad/keyboard summon; live toggles; one-shot pulse injections)

## Related

[[overviews/game-hacking]] · [[openfpga-gbc-cheats-ui]] · [[smo-recomp]] · [[savage-wind-recomp]]