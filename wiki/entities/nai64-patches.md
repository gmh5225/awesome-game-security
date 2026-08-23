---
title: Nai64Patches
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/Nai64__Nai64Patches.md
updated: 2026-08-23
confidence: medium
---

# Nai64Patches

**Nai's Patches** is a curated collection of roughly one hundred universal patches for the **Morphe** Android APK patcher. Implemented in **Kotlin** with **Gradle**, the patches tune, unlock, and declutter mobile games and apps. Coverage includes ad removal, license and **Play Integrity** bypass, root and emulator detection evasion, certificate pinning bypass, telemetry blocking, and extensive device or manifest spoofing. Users select optional patches inside Morphe to rebuild an APK with changes such as skipping rewarded ads, hiding debuggers, forcing orientations, making apps debuggable, or unlocking in-app purchases. Targets reverse engineers, mobile security researchers, and modders working on Android games that enforce licensing, integrity checks, anti-tamper protections, and other client-side security controls. (source: wiki/sources/descriptions/Nai64__Nai64Patches.md)

Sits in the APK rebuild lane beside [[apktool]], [[apk-sh]], and [[auto-android-app-modding-tool]], but as a **Morphe patch catalog** rather than a standalone patcher—patches compose inside Morphe's rebuild workflow.

## Links

- Repo: https://github.com/Nai64/Nai64Patches (README tag: Curated Morphe patch source for Android games — root/integrity bypass, license checks, Play Integrity spoof, and SSL pinning)

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[apktool]] · [[apk-sh]] · [[auto-android-app-modding-tool]] · [[frida]] · [[awesome-android-root]] · [[spoofing-collection]] · [[keyattestation]]
