---
title: Minecraft AntiCheatAI
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/llsgllsg__Minecraft_AntiCheatAI.md
updated: 2026-07-31
confidence: medium
---

# Minecraft AntiCheatAI (DeepGuard)

DeepGuard is an AI-powered Minecraft Paper anti-cheat plugin that detects suspicious player behavior, especially mechanical scaffold-style bridging cheats. It combines traditional movement checks with on-server ONNX Runtime inference over short behavior sequences built from look angles, position, block placement, and movement flags. (source: wiki/sources/descriptions/llsgllsg__Minecraft_AntiCheatAI.md)

## Pipeline

- **DeepGuard plugin** — Paper server plugin; timed silent scans, manual report analysis, configurable alert and punish thresholds.
- **BehaviorRecorder** — companion plugin collecting labeled normal and cheat samples for training.
- **Training stack** — Python scripts prepare data and train a 1D CNN (PyTorch), exported as ONNX for live on-server inference.

Targets Minecraft server operators and researchers exploring machine-learning-based anti-cheat, in the same Java-server operator lane as [[avaanticheat]] and [[oomph]] (Bedrock proxy), distinct from kernel products such as [[easy-anti-cheat]].

## Links

- Repo: https://github.com/llsgllsg/Minecraft_AntiCheatAI

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[avaanticheat]] · [[oomph]] · [[cs2-hybrid-anticheat-proposal]] · [[waldo]]
