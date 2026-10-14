---
title: chess-anti-cheat
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/MaksymSakundiak__chess-anti-cheat.md
updated: 2026-10-14
confidence: high
---

# chess-anti-cheat

**chess-anti-cheat** (MaksymSakundiak) is a Python **TensorFlow/Keras** pipeline that scores likely **engine-assisted** online chess from move sequences, think times, and player color. A multi-modal model combines move embeddings, bidirectional **LSTM** layers, **Conv1D** pattern extraction, and player color to produce a cheating-risk score. Targets platform operators and AC researchers who want a reproducible baseline for data collection, training, and screening—not an arbiter verdict engine. (source: wiki/sources/descriptions/MaksymSakundiak__chess-anti-cheat.md)

README category: Anti Cheat / Machine Learning (engine-assistance detection).

## Pipeline

Scripts pull **PGN** games from the **Lichess API**, convert labeled honest and cheater samples into an **HDF5** dataset, preprocess move **vocabulary**, train the classifier, and expose **interactive or programmatic** predictions with detailed **risk-factor explanations**. Labels are **player-level**; train/validation splits are grouped by player to limit leakage. **Timing features** come from clock annotations to flag unnaturally consistent or **low-variance** think-time patterns alongside move-sequence signals. (source: wiki/sources/descriptions/MaksymSakundiak__chess-anti-cheat.md)

Complements federation-scale arbiter platforms such as [[sentinel-anticheat-chess]] and browser Gomoku triage such as [[gomoku-anti-cheat-detector]]; pairs [[ai-aimbot-detection]] timing/telemetry ML framing and [[research-rigor]] labeled-session discipline.

## Links

- Repo: https://github.com/MaksymSakundiak/chess-anti-cheat

## See also

[[sentinel-anticheat-chess]] · [[gomoku-anti-cheat-detector]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[research-rigor]]
