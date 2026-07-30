---
title: FakeEye
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/mexploitui__FakeEye.md
updated: 2026-07-30
confidence: medium
---

# FakeEye

BattlEye **initialization emulator**: mimics BE’s startup sequence by managing the `BEService` process, installing the service via Windows SCM APIs, reading external configuration files, and launching the game process with BattlEye-style launch parameters—so protected titles start as if [[battleye]] were present without the real anti-cheat stack. (source: wiki/sources/descriptions/mexploitui__FakeEye.md)

Useful for researchers studying BE service/install/launch contracts and for offline client workflow around BE-gated executables—not a kernel bypass.

## Links

- Repo: https://github.com/mexploitui/FakeEye

## Related

[[battleye]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
