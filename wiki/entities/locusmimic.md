---
title: LocusMimic
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/wchunlin1006__LocusMimic.md
updated: 2026-07-29
confidence: medium
---

# LocusMimic

Android **location-simulation** module for rooted devices (Android 11+). Injects configurable GPS coordinates into selected apps via **Xposed** or **LSPosed**. Kotlin + Jetpack Compose UI with map-based point selection, place search, saved favorites, and fine-grained latitude/longitude/accuracy/altitude/speed/random-offset control. (source: wiki/sources/descriptions/wchunlin1006__LocusMimic.md)

**Operating modes:** per-app hooks, system-level hooks, and a non-root **Mock Provider** fallback. Builds on forks of XposedFakeLocation and HideMockLocation to conceal mock-location indicators from targeted apps. Optional external broadcast control supports adb or local-intent automation for scripted testing.

**Use cases:** authorized app debugging, location-based anti-cheat evaluation, and Android security research.

## Links

- Repo: https://github.com/wchunlin1006/LocusMimic

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[anywhere]] · [[magisk]] · [[detection]] · [[droidshield]]
