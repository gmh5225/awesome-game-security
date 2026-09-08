---
title: UsbDetectionBypass
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/RytterMohn__UsbDetectionBypass.md
  - wiki/sources/README-categories.md
updated: 2026-09-08
confidence: medium
---

# UsbDetectionBypass

**LSPosed/Xposed module** that bypasses in-app **USB connection and USB debugging detection** inside scoped target applications. (source: wiki/sources/descriptions/RytterMohn__UsbDetectionBypass.md)

**Hooks:** Kotlin Java hooks plus a native C++ component mask `SystemProperties`, `UsbManager` APIs, USB and battery broadcasts, `getprop`/`dumpsys` command checks, and native file reads on USB-related sysfs paths so the target process sees a disconnected, non-debuggable USB state.

**Diagnostics:** LSPosed module logs, logcat, and per-app log files for authorized testing workflows.

README category: Cheat / Xposed. Intended for security research, reverse engineering, and anti-cheat testing on rooted devices where apps enforce USB or ADB-based integrity checks.

## Links

- Repo: https://github.com/RytterMohn/UsbDetectionBypass

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[concepts/mobile-anti-cheat]] · [[xiaomi-usb-security-bypass]] · [[device-reset-spoofer]] · [[hidemyandroid]] · [[root-detection-low-level]] · [[xposed-module-kit]]
