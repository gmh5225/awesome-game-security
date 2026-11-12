---
title: Ban-Hammer
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/AadityaPokhriyal__Ban-Hammer.md
updated: 2026-11-12
confidence: medium
---

# Ban-Hammer

**Ban-Hammer** (AadityaPokhriyal/ban-hammer) is a **Counter-Strike 2** machine-learning research pipeline that flags suspicious play from **match telemetry**—per-player behavioral and combat statistics—rather than client-side hooks or kernel scans. It is implemented in **Python** with Jupyter notebooks and a feature-extraction script: labeled datasets are built from **Parquet tick data** and companion **JSON event logs** (cheater ground truth), with derived signals such as kills/deaths per round, K/D, headshot rate, movement speed, accuracy penalty, damage per round, and contextual kill ratios (through smoke, while blinded, in air). Training uses **scikit-learn** pipelines with logistic regression, random forest, and **XGBoost** classifiers, group-aware validation, and threshold tuning; serialized models are evaluated on held-out matches. It targets researchers and anti-cheat practitioners who want a reproducible, statistics-driven way to surface aimbot-like or spinbot-like patterns from in-game data. (source: wiki/sources/descriptions/AadityaPokhriyal__Ban-Hammer.md)

Complements other CS2 **offline / demo-telemetry ML** stacks such as [[cs2guard]], [[yaacs-anticheat]], [[cs2-overwatch]], and [[nullcs]], and dedicated-server rule plugins such as [[cs2ac]]—but focuses on **tabular match-stat features** from tick Parquet + JSON rather than live server plugins or demo-only pitch/yaw kinematics alone.

## Links

- Repo: https://github.com/aadityapokhriyal/ban-hammer (Anti Cheat / Machine Learning)

## Related

[[cs2guard]] · [[yaacs-anticheat]] · [[cs2-overwatch]] · [[nullcs]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
