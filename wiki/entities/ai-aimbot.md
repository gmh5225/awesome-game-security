---
title: AI-Aimbot
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/RootKit-Org__AI-Aimbot.md
updated: 2026-08-21
confidence: medium
---

# AI-Aimbot

**AI-powered aimbot** (RootKit-Org) in the cheat / Machine Learning YOLOv5 lane. Uses machine-learning object detection on screen-captured frames to locate targets, then applies mouse aim adjustments—without classic in-process memory reads or injection. Supports custom YOLO-based models per title (including Fortnite and Rust), Conda-managed Python environments, and configurable detection sensitivity plus aiming parameters. Aimed at game security researchers studying AI-based cheat detection and ML-driven automated game interaction. (source: wiki/sources/descriptions/RootKit-Org__AI-Aimbot.md)

Sits in the external screen-capture → YOLO → HID pipeline beside [[ai-fps-b00m-h3adsh0t]], [[yolov5-pubg]], and [[nuremx]]; defensive ML counterparts include [[waldo]] and [[aimbot-detection-prototype]] via [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/RootKit-Org/AI-Aimbot

## Related

[[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[ai-fps-b00m-h3adsh0t]] · [[yolov5-pubg]] · [[rust-auto-weapon-detection-opencv-example]] · [[hardware-input-injection]] · [[waldo]]
