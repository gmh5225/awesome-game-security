---
title: Firebreak
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/bboe__firebreak.md
  - wiki/sources/README-categories.md
updated: 2026-10-13
confidence: high
---

# Firebreak

**Firebreak** (bboe/firebreak) is a Python command-line tool that unlocks and reflashes the Amazon Echo Dot (2nd Generation, codename *biscuit*) over USB from macOS, Linux, or Windows. It automates transitions between stock Fire OS builds and several amonet-based rooted targets with custom bootloaders and TWRP recovery. (source: wiki/sources/descriptions/bboe__firebreak.md)

## Architecture

| Layer | Role |
|-------|------|
| **Plugin-driven unlock plans** | Orchestrate multi-step stock ↔ rooted transitions |
| **GPT / boot images** | Partition layout and boot image handling, OTA-aware layouts |
| **USB tooling** | fastboot, adb, MediaTek bootrom USB download, partition writes under recovery or bootrom |
| **Diagnostics** | Support reporting; isolate eMMC vs cable failures |
| **Simulator** | Exercise unlock/reflash flows without physical hardware |

## Capabilities

- Cross-platform CLI for **unlock, root, and reflash** on MediaTek-based Echo Dot 2nd gen hardware.
- Optional **eMMC shorting** hardware recovery when the device shows no boot indication.
- Aimed at researchers and enthusiasts studying **embedded device security**, **bootloader trust**, and practical unlock or restore workflows on smart speakers.

Listed under README **Cheat → IoT / Smart devices**.

## Links

- Repo: https://github.com/bboe/firebreak

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[sjcam]] · [[xiaomi-c400-pwn]] · [[embedded-hacking]]
