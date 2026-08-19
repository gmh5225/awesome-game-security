---
title: NuremX
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Zurek0x__NuremX.md
updated: 2026-08-19
confidence: medium
---

# NuremX

Python **Apex Legends** cheat (Zurek0x) in the cheat / [AI] lane. Uses **YOLOv5** computer-vision models with bundled trained weights to detect enemies from screen capture, then drives overlay and aiming features through configurable runtime parameters and update/version-control logic. The design emphasizes AI-driven detection and control instead of direct process memory hooking, with scripts for both Windows and Linux-style workflows—aimed at machine-learning-assisted game automation and anti-cheat-aware experimentation. (source: wiki/sources/descriptions/Zurek0x__NuremX.md)

Sits in the external screen-capture → YOLO → HID pipeline beside title-agnostic FPS samples such as [[ai-fps-b00m-h3adsh0t]] and other title-specific YOLO cheats such as [[yolov5-pubg]]; Apex memory/SDK samples such as [[apex-legends-sdk]] and [[apex-linux]] cover complementary in-process or kernel paths under [[easy-anti-cheat]]. Defensive ML counterparts include [[waldo]] and [[aimbot-detection-prototype]] via [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/Zurek0x/NuremX

## Related

[[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[yolov5-pubg]] · [[ai-fps-b00m-h3adsh0t]] · [[apex-legends-sdk]] · [[apex-linux]] · [[easy-anti-cheat]] · [[hardware-input-injection]] · [[waldo]]
