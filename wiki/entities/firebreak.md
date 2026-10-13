---
title: Firebreak
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/bboe__firebreak.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: medium
---

# Firebreak

**Firebreak** (bboe/firebreak) is a Python command-line tool that unlocks and reflashes the Amazon Echo Dot (2nd Generation, codename *biscuit*) over USB from macOS, Linux, or Windows. It automates transitions between stock Fire OS builds and several amonet-based rooted targets with custom bootloaders and TWRP recovery, using fastboot, adb, MediaTek bootrom USB download, and partition writes under recovery or bootrom. (source: wiki/sources/descriptions/bboe__firebreak.md)

Plugin-driven unlock plans cover GPT and boot image handling, OTA-aware layouts, and optional hardware recovery via eMMC shorting when the device shows no boot indication. Diagnostic modes support support reporting and cable versus eMMC failure isolation; a simulator exercises flows without physical hardware. Listed under README **Cheat → IoT / Smart devices** for embedded device security, bootloader trust, and practical unlock or restore workflows on MediaTek-based smart speakers.

## Links

- Repo: https://github.com/bboe/firebreak

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[sjcam]] · [[xiaomi-c400-pwn]] · [[embedded-hacking]]
