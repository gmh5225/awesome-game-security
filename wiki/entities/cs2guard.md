---
title: CS2Guard
kind: entity
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/Driw0x__CS2Guard.md
  - wiki/sources/README-categories.md
updated: 2026-09-03
confidence: medium
---

# CS2Guard

**CS2Guard** is an experimental Python machine-learning project that detects suspicious cheating behavior in Counter-Strike 2 by analyzing gameplay telemetry instead of scanning client systems. Parses CS2 demo files for match, player, and tick-level data; engineers behavioral features (aim movement, crosshair placement, target tracking, reaction time, angular velocity); and trains unsupervised anomaly or supervised classification models toward a real-time server-side anti-cheat pipeline. (source: wiki/sources/descriptions/Driw0x__CS2Guard.md)

## Capabilities

- **Demo parsing** — extract tick-level player and match telemetry from CS2 demos.
- **Feature engineering** — aim, tracking, reaction-time, and angular-velocity signals for cheat-like behavior.
- **Dataset builder** — reproducible pipelines with adapters for labeled datasets such as CS2CD.
- **Visualization & tests** — aim-analysis plots and unit tests for detector iteration.
- **Server-side goal** — behavioral detection without client memory scans or kernel drivers.

Peers with server-side CS2 plugins such as [[cs2ac]] / [[cs2kac]], hybrid judge/honeypot proposals such as [[cs2-hybrid-anticheat-proposal]], and ML aimbot research such as [[dlac]] and [[aimbot-detection-prototype]].

## Links

- Repo: https://github.com/Driw0x/CS2Guard

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[cs2ac]] · [[cs2kac]] · [[dlac]] · [[ai-aimbot-detection]] · [[cs2-hybrid-anticheat-proposal]]
