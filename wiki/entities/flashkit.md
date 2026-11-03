---
title: FlashKit
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/chakradhartode__flashkit.md
  - wiki/sources/README-categories.md
updated: 2026-11-03
confidence: medium
---

# FlashKit

**flashkit** (chakradhartode/flashkit) is a **Termux:GUI** Android application that turns a **Magisk or KernelSU rooted** host phone into a pocket flashing station for a second device over OTG—without a PC. Python and shell installers drive **adb** and **fastboot** through a Termux:GUI interface with live logs, confirmations, and cancelable jobs. Operators can sideload ROM zips, flash partition images, run staged GSI installs, repair adb/fastboot links, fix common recovery black-screen issues, and manage files on both phones including in-archive zip editing. One-line setup bundles signature-matched Termux:GUI and Termux:API plugins plus CLI helpers (`doctor`, `update`, plugin checks). (source: wiki/sources/descriptions/chakradhartode__flashkit.md)

Listed under README **Cheat → Android ROM** beside [[flashwright]], [[rom-shifter]], and [[tool-tree]].

## Surfaces

| Component | Role |
|-----------|------|
| **Host** | Rooted Android handset running Termux + Termux:GUI |
| **Target** | Second device over USB OTG |
| **Operations** | ROM sideload, partition flash, GSI staging, link repair |
| **UX** | Live logs, confirmations, cancelable long jobs |

## Links

- Repo: https://github.com/chakradhartode/flashkit

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[flashwright]] · [[rom-shifter]] · [[tool-tree]] · [[android-kernel-kit]]
