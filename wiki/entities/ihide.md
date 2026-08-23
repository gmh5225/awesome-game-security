---
title: iHide
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/Kc57__iHide.md
updated: 2026-08-23
confidence: medium
---

# iHide

iOS jailbreak-hiding tweak that lets selected apps run as if the device were not jailbroken. Users enable or disable bypass behavior per application from the iOS Settings panel. The implementation uses MobileSubstrate-style hooking with Objective-C and related iOS tweak components, and attempts to defeat common jailbreak-detection checks. (source: wiki/sources/descriptions/Kc57__iHide.md)

Mainly used in mobile app and game security testing where analysts need to evaluate behavior behind jailbreak-detection gates — the offensive counterpart to jailbreak probes in SDKs such as [[free-rasp-ios]] and [[trustdevice-ios]].

## Links

- Repo: https://github.com/Kc57/iHide

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[shadow]] · [[free-rasp-ios]] · [[dopamine]] · [[opainject]] · [[ios-mod-menu-template-for-theos]]
