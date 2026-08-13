---
title: FakerAndroid
kind: entity
topics: [mobile-security, reverse-engineering, game-engine, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__FakerAndroid.md
updated: 2026-08-13
confidence: medium
---

# FakerAndroid

APK-to-Android-Studio project translator with native `.so` hook scaffolding — including [[il2cpp]] C++ scaffolding — for secondary development on decompiled game packages. (source: wiki/sources/descriptions/gmh5225__FakerAndroid.md)

Typical workflow: open the generated Gradle project, debug or run it, then extend behavior via **javaScaffolding** — add Java under `app/src/main/java` with class and package names matching the original app so smali rebuilds stay consistent. Native hooks use a **fakeCpp** API for JNI interception of `.so` methods; IL2CPP titles combine IL2CPP scaffolding with fakeCpp for managed-script modification through JNI.

Primary audience: game-security researchers and reverse engineers studying offensive techniques in the cheat / game engine explorer:Unity lane.

## Links

- Repo: https://github.com/gmh5225/FakerAndroid

## Related

[[il2cpp]] · [[android-modding]] · [[apktool]] · [[jadx]] · [[il2cpp-hook-scripts]] · [[frida-il2cpp-bridge]] · [[android-cheat-template]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-engine]]
