---
title: PTFakeTouch
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__PTFakeTouch.md
updated: 2026-08-11
confidence: medium
---

# PTFakeTouch

iOS library for **programmatic touch simulation** without user interaction. Uses private **IOKit** APIs or **UIKit** internals to inject synthetic touch events into the iOS event pipeline, enabling automated UI interaction and game input simulation for iOS automation developers and game bot builders. (source: wiki/sources/descriptions/gmh5225__PTFakeTouch.md)

Sits in the iOS input-simulation lane beside Android Magisk record/replay modules such as [[event-replay]] and native uinput injectors such as [[android-virtual-touch]]; complements non-jailbreak location spoofing via [[ios-location-spoofer]] when AC evaluates touch timing or gesture patterns.

## Links

- Repo: https://github.com/gmh5225/PTFakeTouch

## Related

[[event-replay]] · [[android-virtual-touch]] · [[android-touch]] · [[ios-location-spoofer]] · [[opainject]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
