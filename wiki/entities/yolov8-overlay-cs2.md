---
title: YOLOv8 Overlay CS2
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Leksa667__YOLOv8-Overlay-CS2.md
updated: 2026-08-23
confidence: medium
---

# YOLOv8 Overlay CS2

**CS2 computer-vision overlay** (Leksa667) in the cheat / game:cs2 [YOLOv8 in CS2] lane. Python project that runs real-time enemy-player detection with a **YOLOv8 ONNX** model, using **ONNX Runtime** for inference, **mss** for screen capture, and **Pygame** plus Win32 APIs to render a transparent topmost overlay window. Optional CUDA acceleration, confidence filtering, hotkeys, and a smooth aim-assist routine. Primary use case is computer-vision cheat prototyping and anti-cheat research on AI-assisted detection behavior—no in-process memory reads or injection. (source: wiki/sources/descriptions/Leksa667__YOLOv8-Overlay-CS2.md)

Sits in the screen-capture → YOLO → overlay/HID pipeline beside [[rookieai-yolov8]], [[ai-aimbot]], and [[gan-aimbots]]; CS2 memory-reading externals such as [[aimstar]], [[overlayai]], and [[tkazer-cs2-external]] cover the complementary offset/RPM lane. Defensive ML and analyst counterparts include [[waldo]], [[aimbot-detection-prototype]], and [[cs2-tracker]] via [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/Leksa667/YOLOv8-Overlay-CS2

## Related

[[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[rookieai-yolov8]] · [[ai-aimbot]] · [[gan-aimbots]] · [[aimstar]] · [[overlayai]] · [[tkazer-cs2-external]] · [[waldo]] · [[aimbot-detection-prototype]] · [[cs2-tracker]] · [[hardware-input-injection]]
