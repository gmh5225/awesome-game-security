---
title: VioletWing
kind: entity
topics: [game-hacking, graphics-api]
sources:
  - wiki/sources/descriptions/Jesewe__VioletWing.md
updated: 2026-08-24
confidence: medium
---

# VioletWing

**External Counter-Strike 2 helper** (Jesewe; cheat / game:cs2 Python external). Python project that reads CS2 process memory out-of-process and exposes TriggerBot, ESP overlay, bunnyhop, and NoFlash through a **customtkinter** desktop GUI. Uses **PyMeow** for overlay rendering and runs **cs2-dumper** against the live CS2 process at startup to refresh memory offsets after game updates. Feature set includes crosshair-based auto-fire with per-weapon delays, ESP with boxes, skeletons, snaplines, health bars, bomb timer, and spectator list, plus ground-flag-synchronized bunnyhop and flash-duration clamping. Positioned for CS2 reverse-engineering and game-security experimentation on offline or private servers—not online matchmaking. (source: wiki/sources/descriptions/Jesewe__VioletWing.md)

## Architecture highlights

| Component | Role |
|-----------|------|
| PyMeow | Cross-process memory access and overlay draw |
| customtkinter | Desktop feature and configuration GUI |
| cs2-dumper | Startup offset refresh against live CS2 process |
| TriggerBot | Crosshair-gated auto-fire with weapon-specific delays |
| ESP | Boxes, skeletons, snaplines, health, bomb timer, spectators |

Sits in the Python external CS2 lane beside [[pythoncs2]]; offset bootstrap via [[cs2-dumper]] matches C#/C++ externals such as [[titled-gui-cs2]] and [[overlayai]].

## Links

- Repo: https://github.com/Jesewe/VioletWing

## Related

[[overviews/game-hacking]] · [[overviews/graphics-api]] · [[pythoncs2]] · [[cs2-dumper]] · [[titled-gui-cs2]] · [[overlayai]] · [[aimstar]] · [[tkazer-cs2-external]] · [[yolov8-overlay-cs2]] · [[meowsense]]
