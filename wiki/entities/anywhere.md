---
title: AnyWhere
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/cxOrz__AnyWhere.md
updated: 2026-08-23
confidence: medium
---

# AnyWhere

Lightweight **Android mock-location** app for simulating GPS coordinates. Java + Gradle build aimed at debugging location-based services (LBS) and testing how apps handle geographic data. (source: wiki/sources/descriptions/cxOrz__AnyWhere.md)

**Features:** OpenStreetMap map picker; floating overlay **joystick** to simulate walking, running, or cycling speeds; location history with optional IP-based coordinate lookup.

**Stealth module:** Bundled **LSPosed/Xposed** module hooks the system to hide mock-location flags and bypass common spoofing checks—useful for studying mock-GPS detection and location-based anti-cheat in mobile games and LBS apps.

## Links

- Repo: https://github.com/cxOrz/AnyWhere

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[locusmimic]] · [[xposed-module-kit]] · [[mobile-anti-cheat]] · [[ios-location-spoofer]] · [[wloc]]
