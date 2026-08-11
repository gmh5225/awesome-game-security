---
title: Overwatch2 Colorbot Cheats
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__Overwatch2-colorbot-Cheats.md
updated: 2026-08-11
confidence: medium
---

# Overwatch2 Colorbot Cheats

Python-based **Overwatch 2 colorbot** (gmh5225) that detects enemy outlines via screen **pixel color** (configured purple in-game), computes aim deltas, and sends mouse-move commands over **serial** (115200 baud) to an **Arduino Leonardo** running HID firmware. The Arduino emits protocol-conformant `Mouse.move()` events in 127-unit chunks for large deltas and accepts shoot / silent-aim / reset commands—aiming to bypass software mouse-input detection by presenting movement as legitimate hardware HID. Zero-memory visual pipeline: no injection or RPM; useful for researchers studying pixel-based color aimbots and Arduino hardware input spoofing. (source: wiki/sources/descriptions/gmh5225__Overwatch2-colorbot-Cheats.md)

Contrasts with internal Overwatch ESP such as [[ow-outlines]] (glow/outline memory writes) and ML capture pipelines such as [[pine]]; pairs with heuristic CV triggerbots such as [[camera-triggerbot]] and the [[hardware-input-injection]] device classes.

## Links

- Repo: https://github.com/gmh5225/Overwatch2-colorbot-Cheats

## Related

[[overviews/game-hacking]] · [[hardware-input-injection]] · [[ai-aimbot-detection]] · [[camera-triggerbot]] · [[ow-outlines]] · [[overwatch-iat-fixer]] · [[pine]] · [[human-mouse-movement]]
