---
title: HideMyAndroid
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Xposed-Modules-Repo__com.wowsoftware.hidemyandroid.md
updated: 2026-08-28
confidence: medium
---

# HideMyAndroid

**Privacy-focused Xposed/LSPosed module** for rooted **Android 9+** devices that intercepts identifier and environment queries from target apps and returns **profile-based spoofed values** to reduce tracking and device fingerprinting. (source: wiki/sources/descriptions/Xposed-Modules-Repo__com.wowsoftware.hidemyandroid.md)

**Masking:** Android ID, GAID, IMEI, Widevine DRM ID; root, LSPosed, VPN, proxy, and developer-mode hiding; SIM, Wi-Fi, Bluetooth, GPS, timezone, and browser fingerprint spoofing; per-profile account and proxy isolation with backup, restore, and device simulation.

Built on the **Xposed hooking framework** with a profile-based configuration system — each target app can receive a distinct spoofed environment without reflashing or rebooting. README category: Cheat / Xposed.

Useful for studying app-level anti-detection and fingerprinting checks — including mobile game security, anti-cheat evasion, and Android reverse-engineering research on identifier probes.

## Links

- Repo: https://github.com/xposed-modules-repo/com.wowsoftware.hidemyandroid

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[anywhere]] · [[locusmimic]] · [[xposed-module-kit]] · [[mobile-anti-cheat]] · [[spoofing-collection]]
