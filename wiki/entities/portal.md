---
title: Portal
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/Lecheeel__Portal.md
updated: 2026-11-21
confidence: medium
---

# Portal

Android **virtual location and environment spoofing** app (Lecheeel; Kotlin/Java, optional native C++ hooks). Drives fake positions, scripted routes, and broader device context into target apps without physical movement. Deployment paths include standard **mock-location** mode, **LSPosed/Xposed** (libxposed API 102), or an experimental **root + native hook** stack. (source: wiki/sources/descriptions/Lecheeel__Portal.md)

**Capabilities:** GPS, network, and fused-location simulation with **route playback** and floating joystick controls; multi-constellation **GNSS** and **NMEA** synthesis; Wi-Fi and cellular environment **capture or replay**; experimental carrier/SIM identity spoofing. **Anti-detection** helpers include stack-trace cleaning and mock-flag handling. A companion **detector** module reports what location and sensor APIs actually expose to apps—useful for validating anti-cheat probes on rooted or Xposed-enabled hardware.

**Use cases:** authorized security research, reverse engineering, and benchmarking location-based game protections and mobile anti-cheat checks.

## Links

- Repo: https://github.com/Lecheeel/Portal

## Related

[[locusmimic]] · [[anywhere]] · [[smalipatcher-reborn]] · [[xposed-module-kit]] · [[overviews/mobile-security]] · [[concepts/mobile-anti-cheat]] · [[overviews/game-hacking]]