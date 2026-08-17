---
title: Winlator
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/brunodev85__winlator.md
updated: 2026-08-17
confidence: medium
---

# Winlator

Android application that runs Windows x86/x64 applications and games on ARM-based Android devices. Combines **Box86/Box64** for x86-to-ARM binary translation with **Wine** for Windows API compatibility inside a **PRoot**-based Linux container, **Mesa Turnip** or **VirGL** for GPU acceleration, and a virtual desktop with touch controls. Targets Android users running Windows software on mobile hardware and researchers studying cross-architecture binary translation in the README `Windows Emulator` lane. (source: wiki/sources/descriptions/brunodev85__winlator.md)

Inverse direction to WSA/Android-on-Windows tooling such as [[wsapatch]] and [[win11-apk-installer]]; complements WHP-hosted Windows emulation such as [[winvisor]] and AOT PE translation such as [[levo]] on the compatibility-layer axis rather than hypervisor guests.

## Links

- Repo: https://github.com/brunodev85/winlator (README tag: Windows Emulator — Android application for running Windows applications with Wine and Box86/Box64)

## Related

[[winvisor]] · [[levo]] · [[crossover-patcher]] · [[termux-app]] · [[yuzu-android]] · [[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
