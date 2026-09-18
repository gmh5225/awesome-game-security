---
title: NoWiFi Wireless Debugging
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/iflyabd__nowifi-adb.md
  - wiki/sources/README-categories.md
updated: 2026-09-18
confidence: medium
---

# NoWiFi Wireless Debugging

**NoWiFi Wireless Debugging** is an LSPosed module for rooted Android devices that enables standard wireless ADB debugging without requiring WiFi or a mobile hotspot. Written in Kotlin, it hooks the Android system framework and Settings app to bypass network checks that normally block wireless debugging when no local network is available. The module supports connections over mobile data or VPN overlays such as Tailscale, optionally exposes a fixed IP and port through a TCP proxy, and retains hotspot-based wireless debugging from its upstream project. It requires Magisk with Zygisk enabled and targets Android 15 through 16. (source: wiki/sources/descriptions/iflyabd__nowifi-adb.md)

Listed in the README under **Cheat → Android Terminal Emulator** as `[LSPosed module enabling Android wireless debugging over mobile data or Tailscale without WiFi or hotspot]`.

Complements on-device ADB utilities such as [[ashellyou]] and desktop stacks such as [[scrcpy]], [[moabille]], and [[lamda]] by removing the WiFi/hotspot prerequisite for remote shell and instrumentation during mobile game analysis, anti-cheat testing, and Android security research.

## Links

- Repo: https://github.com/iflyabd/nowifi-adb

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[ashellyou]] · [[termux-app]] · [[moabille]] · [[scrcpy]] · [[usb-detection-bypass]] · [[zygisk]]
