---
title: TFG AntiCheat ServerSide
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Alexramirezzz__TFG-AntiCheat-ServerSide.md
  - wiki/sources/README-categories.md
updated: 2026-10-11
confidence: medium
---

# TFG AntiCheat ServerSide

Thesis-grade **server-side anti-cheat** for **Minecraft Paper/Spigot 1.18.2** (Alexramirezzz/TFG-AntiCheat-ServerSide). A Java plugin records **labelled sessions**, cleans swing and interact event streams, and scores timing windows with explainable rules plus ML models trained in a companion **Python** pipeline—under a man-at-the-end model where the client cannot be trusted. (source: wiki/sources/descriptions/Alexramirezzz__TFG-AntiCheat-ServerSide.md)

## Detection focus

Primary target is **click automation / autoclicker** patterns observable from server-side event timing (CPS and interaction cadence), not kernel or client-memory integrity. (source: wiki/sources/descriptions/Alexramirezzz__TFG-AntiCheat-ServerSide.md)

## ML and fail-safe design

Research stack compares threshold rules, **isolation forest** and **one-class SVM** baselines, gradient-boosted and random forest classifiers, and a **sequence CNN**, with adversarial and lag robustness studies. Models export to **ONNX** for off-thread inference; hardened plugin logic **falls back** to the original CPS rule if ML inference fails—aligning with [[detector-operations]] fail-safe rollout discipline. (source: wiki/sources/descriptions/Alexramirezzz__TFG-AntiCheat-ServerSide.md)

## Links

- Repo: https://github.com/Alexramirezzz/TFG-AntiCheat-ServerSide

## Related

[[overviews/anti-cheat]] · [[concepts/detector-operations]] · [[concepts/ai-aimbot-detection]] · [[mlanticheat]] · [[virgola-anticheat]] · [[h-ac]]
