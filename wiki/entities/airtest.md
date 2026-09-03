---
title: Airtest
kind: entity
topics: [game-engine, mobile-security]
sources:
  - wiki/sources/descriptions/AirtestProject__Airtest.md
updated: 2026-09-03
confidence: medium
---

# Airtest

Cross-platform **UI automation framework** for games and mobile apps. Written primarily in Python, it locates UI elements through **image recognition** rather than injecting into the target process. Provides device control APIs, scalable execution on device farms, command-line and Python interfaces, HTML reporting, and integration with an IDE plus object-hierarchy tooling (Poco) for advanced UI interaction. Aimed at QA engineers and game or app teams building repeatable end-to-end automation across Android, iOS, and desktop environments. (source: wiki/sources/descriptions/AirtestProject__Airtest.md)

Non-injection image matching contrasts with Appium- or instrumentation-first mobile QA stacks that rely on in-game logs or accessibility trees — useful for black-box regression on builds where internal hooks are unavailable, but more sensitive to resolution, theme, and localization drift than structured instrumentation.

## Links

- Repo: https://github.com/AirtestProject/Airtest

## Related

[[games-test-automation-example]] · [[unity-automated-qa-examples]] · [[fastlogs]] · [[lamda]] · [[overviews/game-engine]] · [[overviews/mobile-security]]
