---
title: chess-anti-cheat
kind: entity
topics: [anti-cheat]
sources:
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/MaksymSakundiak__chess-anti-cheat.md
updated: 2026-10-14
confidence: medium
---

# chess-anti-cheat

**chess-anti-cheat** (MaksymSakundiak) is a Python **TensorFlow/Keras** pipeline that scores likely **engine-assisted** online chess from move sequences, think times, and player color. A multi-modal model combines move embeddings, bidirectional LSTM layers, and Conv1D pattern extraction; supporting scripts ingest Lichess PGN, build labeled HDF5 datasets, train with player-level train/validation splits to limit leakage, and run interactive or programmatic predictions with risk-factor explanations. Targets platform operators and AC researchers who want a reproducible baseline for data collection, training, and screening—not an arbiter verdict engine. (source: wiki/sources/descriptions/MaksymSakundiak__chess-anti-cheat.md)

README category: Anti Cheat / Machine Learning (engine-assistance detection).

Complements federation-scale arbiter platforms such as [[sentinel-anticheat-chess]] and browser Gomoku triage such as [[gomoku-anti-cheat-detector]]; pairs [[ai-aimbot-detection]] timing/telemetry ML framing and [[research-rigor]] labeled-session discipline.

## Links

- Repo: https://github.com/MaksymSakundiak/chess-anti-cheat

## See also

[[sentinel-anticheat-chess]] · [[gomoku-anti-cheat-detector]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[research-rigor]]
