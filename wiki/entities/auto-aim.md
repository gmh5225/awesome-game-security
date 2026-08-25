---
title: Auto_aim
kind: entity
topics: [game-hacking, anti-cheat, graphics-api]
sources:
  - wiki/sources/descriptions/Fragmentaim__Auto_aim.md
updated: 2026-08-25
confidence: medium
---

# Auto_aim

**Real-time AI aiming assistant core** (Fragmentaim) in the DXGI + TensorRT + driver-level input lane. C++ pipeline combining **DXGI Desktop Duplication** for low-latency screen capture, **ONNX Runtime with TensorRT** for YOLO object detection, and **OpenCV** for vision processing. Detections drive relative cursor movement through a **driver-level mouse simulation** interface rather than classic in-process memory reads or injection. Primary use case is technical research into real-time computer-vision-driven game automation. (source: wiki/sources/descriptions/Fragmentaim__Auto_aim.md)

Sits in the screen-capture → YOLO → driver-input pipeline beside [[rookieai-yolov8]], [[ai-aimbot]], [[yolov8-overlay-cs2]], and [[ai-fps-b00m-h3adsh0t]]; defensive ML and analyst counterparts include [[waldo]] and [[aimbot-detection-prototype]] via [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/Fragmentaim/Auto_aim

## Related

[[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[hardware-input-injection]] · [[rookieai-yolov8]] · [[ai-aimbot]] · [[yolov8-overlay-cs2]] · [[screencapture]] · [[waldo]]
