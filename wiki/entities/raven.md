---
title: Raven
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/tieqianhao__raven.md
  - wiki/sources/README-categories.md
updated: 2026-11-22
confidence: medium
---

# Raven

**Raven** (tieqianhao/raven) is a **reproducible content risk-control engine** for gaming and anime (ACG) communities. It targets black-market forum and chat posts—cheat sales, boosting services, account trading, and off-platform solicitation—rather than in-game client integrity. Python is the main implementation; a browser-side JavaScript demo ships for interactive trials. Dependencies are limited to **NumPy** and **Pillow**, so synthetic data generation, training, evaluation, reporting, and simulation can run **offline on CPU** from a single entry script. (source: wiki/sources/descriptions/tieqianhao__raven.md)

## Text pipeline

Adversarial spellings are folded into a canonical form through a **traceable normalization** pipeline, then scored with **character n-gram** features, a hand-rolled **SGD logistic regression** model, and **rule fusion** with confidence-based tiered enforcement. The design supports studying evasion such as zero-width insertion, homophones, and per-character obfuscation. (source: wiki/sources/descriptions/tieqianhao__raven.md)

## Image forensics

A complementary module applies **ELA**, **noise-residual**, and **JPEG-ghost** heuristics with block-level localization for coarse screenshot or attachment tamper screening. (source: wiki/sources/descriptions/tieqianhao__raven.md)

## Positioning

Community **trust and safety** and **anti-abuse** research lane beside business risk-control playbooks such as [[anti-cheating-assistant]] and statistical integrity tooling—not kernel AC or live game telemetry.

## Links

- Repo: https://github.com/tieqianhao/raven

## Related

[[anti-cheating-assistant]] · [[tf2bd-database]] · [[unicode-based-source-code-obsfucation-study-2026]] · [[overviews/anti-cheat]]