---
title: QtScrcpy
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/barry-ran__QtScrcpy.md
updated: 2026-08-18
confidence: medium
---

# QtScrcpy

**QtScrcpy** is a Qt-based desktop GUI for displaying and controlling Android devices from a PC over USB or TCP/IP. It reuses the upstream **scrcpy** server on the device: MediaCodec captures the screen, streams H.264 to the host with low latency, and forwards keyboard/mouse input back to Android. Features include file drag-and-drop, screen recording, and multi-device management. The C++ client does not require root on the Android side. Primary audiences are Android developers, QA testers, and researchers who need a visual, interactive mirror for debugging, automation prep, or mobile security workflows. (source: wiki/sources/descriptions/barry-ran__QtScrcpy.md)

## Links

- Repo: https://github.com/barry-ran/QtScrcpy

## Related

[[scrcpy]] · [[lamda]] · [[droidrun]] · [[adb-file-manager]] · [[android-terminal-emulator]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]
