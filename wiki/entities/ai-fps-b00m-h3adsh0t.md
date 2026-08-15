---
title: AI-FPS-b00m-h3adsh0t
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__AI-FPS-b00m-h3adsh0t.md
updated: 2026-08-15
confidence: medium
---

# AI-FPS-b00m-h3adsh0t

Python/C++ **AI-powered FPS aimbot** (gmh5225) in the cheat / Neural Network lane. Captures game frames externally via screen capture, runs object detection (typically YOLO-based) to locate enemy player models, computes target coordinates, and moves the mouse to aim at detections—without in-process memory reads or injection. Aimed at game security researchers studying AI/ML-based cheat detection and computer-vision aimbot architectures. (source: wiki/sources/descriptions/gmh5225__AI-FPS-b00m-h3adsh0t.md)

Sits in the external screen-capture → YOLO → HID pipeline beside title-specific samples such as [[yolov5-pubg]] and classical CV triggerbots such as [[opencv-smart-aimbot]]; defensive ML counterparts include [[waldo]] and [[aimbot-detection-prototype]] via [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/gmh5225/AI-FPS-b00m-h3adsh0t

## Related

[[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[yolov5-pubg]] · [[opencv-smart-aimbot]] · [[pine]] · [[human-mouse-movement]] · [[hardware-input-injection]] · [[waldo]]
