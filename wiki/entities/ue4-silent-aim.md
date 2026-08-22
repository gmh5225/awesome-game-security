---
title: UE4-Silent-Aim
kind: entity
topics: [game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/N-T33__UE4-Silent-Aim.md
updated: 2026-08-22
confidence: medium
---

# UE4-Silent-Aim

Minimal **Unreal Engine 4 silent-aim** technique example (N-T33/UE4-Silent-Aim) demonstrating **viewpoint function hooks** in C++. The sample hooks player camera and view APIs to alter aim direction while preserving visible on-screen view behavior, focusing on rotation and target-bone selection logic during input-triggered execution. Primary use case: **game security research** and understanding aim-manipulation vectors in UE4 titles. (source: wiki/sources/descriptions/N-T33__UE4-Silent-Aim.md)

Sits in the UE4 camera/view-hook lane beside [[ue4-freecam]] and title-specific `GetViewpoint` samples such as [[fortnite-camera-cache-pov]] and [[fortnite-virtual-offsets]].

## Links

- Repo: https://github.com/N-T33/UE4-Silent-Aim

## Related

[[ue4-freecam]] · [[ue4-base]] · [[fortnite-camera-cache-pov]] · [[fortnite-virtual-offsets]] · [[unrealengine4-swissknife]] · [[world-to-screen]] · [[ai-aimbot-detection]] · [[overviews/game-engine]] · [[overviews/game-hacking]]
