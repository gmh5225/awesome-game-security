---
title: android-touch
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__android_touch.md
updated: 2026-08-09
confidence: medium
---

# android-touch

C/C++ **Android touch-input driver** development project aimed at game-security researchers and reverse engineers studying offensive **triggerbot** and **aimbot** input paths on mobile. Focuses on kernel/driver-level touch injection rather than userspace uinput or Magisk record/replay modules. (source: wiki/sources/descriptions/gmh5225__android_touch.md)

Complements [[android-virtual-touch]] (ARM64 NDK uinput virtual touch) and [[event-replay]] (Magisk `/dev/input` record/replay) in the Android input-simulation lane; differs by centering on driver development for programmatic touch delivery.

## Links

- Repo: https://github.com/gmh5225/android_touch

## Related

[[android-virtual-touch]] · [[event-replay]] · [[compile-android-driver]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[human-mouse-movement]]
