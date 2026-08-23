---
title: DLAC
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/LaihoE__DLAC.md
updated: 2026-08-23
confidence: medium
---

# DLAC

**Deep-learning anti-cheat package** (LaihoE) for **CS:GO demo analysis** that predicts suspicious aim behavior on a per-shot basis. Combines Python inference code with a Go-based demo parser and supports ONNX runtime models in different size and accuracy profiles. Users can export predictions to terminal output, CSV, or in-memory lists and tune confidence thresholds for practical workflows. Targets anti-cheat experimentation and research on replay-based behavioral detection—not a live client or server AC product. (source: wiki/sources/descriptions/LaihoE__DLAC.md)

Distinct from gmh5225's [[deep-learning-anti-cheat-csgo]] OSS AC pipeline (memory/code-integrity/process checks). Complements CS2 deep-learning detectors such as [[waldo]], mouse-movement classifiers such as [[delbot-mouse]], and academic ML-aimbot baselines such as [[gan-aimbots]] via [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/LaihoE/DLAC

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[deep-learning-anti-cheat-csgo]] · [[waldo]] · [[delbot-mouse]] · [[gan-aimbots]] · [[pine]] · [[csgo-ac]]
