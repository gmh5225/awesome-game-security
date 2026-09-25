---
title: cs2-overwatch
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/magicnothief__cs2-overwatch.md
  - wiki/sources/README-categories.md
updated: 2026-09-25
confidence: medium
---

# cs2-overwatch

**cs2-overwatch** (magicnothief/cs2-overwatch) is an **offline CS2 demo review pipeline** that ranks suspicious gameplay moments with calibrated suspicion scores and written explanations. Written in Python, it runs demos through hard rule checks, geometry-based visibility analysis, a machine-learning behavior scorer trained on the CS2CD dataset, and an optional fine-tuned LLM judge for human-readable verdicts. A browser web UI, CLI tooling, demo parsing, optional YOLO vision cross-checks, ONNX inference, and llama.cpp support local-only review without sending data off-machine. (source: wiki/sources/descriptions/magicnothief__cs2-overwatch.md)

README category: Anti Cheat / Analysis Framework.

## Pipeline

- Demo parsing with hard rule checks for blatant cheats
- Ray-cast visibility analysis and ML behavior scoring (CS2CD-trained)
- Calibrated suspicion scoring with optional local LLM evidence summaries
- Browser UI + CLI; privacy-preserving offline review posture

## Peers

[[yaacs-anticheat]] · [[cs2-tracker]] · [[cs2guard]] · [[deepaimdetector]] · [[jevcraft-bench]]

## Links

- Repo: https://github.com/magicnothief/cs2-overwatch

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[input-provenance]] · [[detector-operations]] · [[research-rigor]]
