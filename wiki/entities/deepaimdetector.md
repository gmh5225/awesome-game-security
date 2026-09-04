---
title: DeepAimDetector
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/87andrewh__DeepAimDetector.md
updated: 2026-09-04
confidence: medium
---

# DeepAimDetector

**Prototype machine-learning detector** (87andrewh) that classifies whether a gunfight was assisted by a legit aimbot. Go tooling parses **SourceTV demo** data into training features; Python notebooks train and evaluate an **LSTM** model. Core signals include view-angle deltas and crosshair-to-target angular relationships sampled around attack events. Intended as an anti-cheat research experiment—not a production-ready detector. (source: wiki/sources/descriptions/87andrewh__DeepAimDetector.md)

Complements replay-based demo ML detectors such as [[dlac]] and [[cs2guard]] under [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/87andrewh/DeepAimDetector

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[dlac]] · [[cs2guard]] · [[aimbot-detection-prototype]] · [[research-rigor]]
