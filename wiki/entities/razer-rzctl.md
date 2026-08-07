---
title: razer-rzctl
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__razer-rzctl.md
updated: 2026-08-07
confidence: medium
---

# razer-rzctl

BYOVD and ring-0 input research PoC abusing Razer’s signed peripheral driver **`rzctl.sys`**. The driver exposes privileged I/O operations usable to simulate mouse/keyboard input at kernel level—bypassing user-mode input telemetry that anti-cheat systems often monitor—or to obtain kernel memory access through vulnerable IOCTLs. Aimed at game-security researchers studying Razer driver exploitation for input simulation and BYOVD. (source: wiki/sources/descriptions/gmh5225__razer-rzctl.md)

## Links

- Repo: https://github.com/gmh5225/razer-rzctl

## Related

[[byovd]] · [[kernel-mouse]] · [[karlann]] · [[hardware-input-injection]] · [[loldrivers]] · [[vdk]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
