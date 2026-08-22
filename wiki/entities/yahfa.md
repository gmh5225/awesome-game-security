---
title: YAHFA
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/PAGalaxyLab__YAHFA.md
updated: 2026-08-22
confidence: medium
---

# YAHFA

**YAHFA** (Yet Another Hook Framework for ART) is an **Android ART method hooking framework** for Java method replacement and interception. It combines Java and native components to provide **backup-and-hook** APIs, supports common Android ABIs, and ships examples for **static**, **virtual**, **JNI**, and **framework** method hooks. The repository includes a reusable library plus demo app and plugin modules that demonstrate real hook deployment workflows. Used for Android runtime instrumentation, security research, and dynamic behavior modification. (source: wiki/sources/descriptions/PAGalaxyLab__YAHFA.md)

Sits in the Java/ART hook lane beside [[canyie-pine]] and attach-based Java intercept via [[frida]]; complements native inline hooking via [[and64-inline-hook]] and [[adbi]] when analysts need managed-runtime method replacement rather than `.so` patching.

## Links

- Repo: https://github.com/PAGalaxyLab/YAHFA

## Related

[[canyie-pine]] · [[frida]] · [[frida-smali-trace]] · [[virtual-app]] · [[xposed-module-kit]] · [[and64-inline-hook]] · [[adbi]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]]
