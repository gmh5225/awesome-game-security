---
title: AIMr
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/ai-aimbot__AIMr.md
updated: 2026-10-16
confidence: medium
---

# AIMr

**Python external AI aimbot** (ai-aimbot) in the screen-capture → computer-vision → HID lane. Uses YOLO-style object detection on captured frames (OpenCV stack) to locate human-shaped targets on screen, then drives aim automation for any title that renders such models—without classic in-process memory reads or injection. **bettercam** (and related capture paths) feeds inference; a **CustomTkinter** GUI plus CLI expose triggerbot, recoil control, silent aim, target prediction, smooth humanized aim, and configurable FOV or detection overlays. Optional **DirectML** acceleration and extended builds with **Arduino** or **KMBOX** hardware input sit beside software mouse paths. The project emphasizes evasion-oriented positioning; useful for researchers studying vision-based cheating, input injection, and defensive detection of external CV pipelines. (source: wiki/sources/descriptions/ai-aimbot__AIMr.md)

Sits beside [[ai-aimbot]], [[rookieai-yolov8]], [[ai-fps-b00m-h3adsh0t]], and [[opencv-smart-aimbot]] in the external YOLO/OpenCV pipeline; defensive counterparts include [[waldo]] and [[aimbot-detection-prototype]] via [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/ai-aimbot/AIMr

## Related

[[overviews/game-hacking]] · [[ai-aimbot-detection]] · [[hardware-input-injection]] · [[ai-aimbot]] · [[rookieai-yolov8]] · [[opencv-smart-aimbot]] · [[waldo]]
