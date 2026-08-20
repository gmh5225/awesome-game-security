---
title: Pink-Eye
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/SurgeGotTappedAgain__Pink-Eye.md
updated: 2026-08-20
confidence: medium
---

# Pink-Eye

Windows **kernel-mode proof of concept** focused on **anti-cheat callback and integrity-hook manipulation**. Demonstrates redirecting **object callbacks** through **code caves** and tampering with selected **integrity-check paths**. Implemented as a KMDF-style C/C++ driver targeting low-level system internals — aimed at anti-cheat research, defensive testing, and understanding kernel detection and hardening strategies. (source: wiki/sources/descriptions/SurgeGotTappedAgain__Pink-Eye.md)

Adjacent to codecave callback hiding such as [[mapped-callback]] and notify-routine hijack PoCs such as [[notify-routine-hijack-thread]] on the offensive [[kernel-callbacks]] research lane.

## Links

- Repo: https://github.com/SurgeGotTappedAgain/Pink-Eye

## Related

[[kernel-callbacks]] · [[mapped-callback]] · [[notify-routine-hijack-thread]] · [[bustercall]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
