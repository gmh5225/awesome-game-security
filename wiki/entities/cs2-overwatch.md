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

**cs2-overwatch** (magicnothief/cs2-overwatch) is a **CPU-friendly, offline CS2 demo review system** that analyzes Counter-Strike 2 demo files and ranks suspicious gameplay moments with calibrated suspicion scores and written explanations. Written in Python, it targets anti-cheat researchers, game security developers, and learners exploring demo-based cheat detection without sending data off the local machine. (source: wiki/sources/descriptions/magicnothief__cs2-overwatch.md)

README category: Anti Cheat / Analysis Framework.

## Detection layers

The pipeline stacks complementary reviewers on parsed demo telemetry:

- **Hard rule checks** — flag blatant cheat signatures before deeper analysis.
- **Geometry-based visibility** — ray-cast visibility analysis to contextualize aim and tracking against line-of-sight.
- **ML behavior scoring** — machine-learning behavior scorer trained on the **CS2CD** dataset.
- **Optional LLM judge** — fine-tuned local LLM for human-readable verdicts and evidence summaries. (source: wiki/sources/descriptions/magicnothief__cs2-overwatch.md)

## Tooling and inference

Browser-based web UI, CLI tooling, and demo parsing support local-only workflows. Inference runs on **ONNX** models and **llama.cpp** for CPU-friendly deployment; optional **YOLO** vision cross-checks add a computer-vision corroboration lane. Calibrated suspicion tiers rank flagged moments with written explanations rather than binary labels alone.

## Positioning

Complements demo-telemetry research such as [[yaacs-anticheat]] (pitch/yaw feature engineering + classifier benchmarks) and ML behavioral stacks such as [[cs2guard]] (CS2CD-trained anomaly/supervised models) with a **multi-layer review workbench**—rules, visibility geometry, behavior ML, and optional LLM narration—in one offline pipeline beside explainable scoring tools such as [[cs2-tracker]].

## Peers

[[yaacs-anticheat]] · [[cs2guard]] · [[cs2-tracker]] · [[deepaimdetector]] · [[jevcraft-bench]]

## Links

- Repo: https://github.com/magicnothief/cs2-overwatch

## Related

[[overviews/anti-cheat]] · [[ai-aimbot-detection]] · [[input-provenance]] · [[detector-operations]] · [[research-rigor]]
