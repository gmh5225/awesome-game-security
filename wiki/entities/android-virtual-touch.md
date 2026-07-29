---
title: android_virtualTouch
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/muchenspace__android_virtualTouch.md
updated: 2026-07-29
confidence: medium
---

# android_virtualTouch

ARM64 Android native binary (NDK) that injects virtual touch events into the Linux input subsystem via **uinput**, writing to `/dev/input/event*` device nodes. Supports programmatic tap, swipe, and multi-touch gestures for game automation and input testing on **rooted** devices. (source: wiki/sources/descriptions/muchenspace__android_virtualTouch.md)

Complements Magisk record/replay tooling such as [[event-replay]] in the mobile input-simulation lane; unlike replay modules, this synthesizes gestures directly rather than replaying captured traces.

## Links

- Repo: https://github.com/muchenspace/android_virtualTouch

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[event-replay]] · [[magisk]] · [[kernelsu]] · [[human-mouse-movement]]
