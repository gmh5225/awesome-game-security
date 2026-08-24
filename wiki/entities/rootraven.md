---
title: RootRaven
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/Kakaxh1__RootRaven.md
updated: 2026-08-24
confidence: medium
---

# RootRaven

Self-hosted **web command center** for Android and iOS mobile penetration testing that unifies device management, dynamic analysis, and static reconnaissance in a single browser dashboard. Python/Flask backend with vanilla JavaScript frontend. (source: wiki/sources/descriptions/Kakaxh1__RootRaven.md)

Integrates ADB orchestration, [[frida]] instrumentation, [[jadx]] APK decompilation, SSH shell access, Burp Suite proxy setup, and live logcat streaming. Pre-built Frida hooks cover SSL pinning bypass, root and jailbreak detection bypass, anti-debug evasion, biometric bypass, and crypto sniffing. Additional modules provide manifest scanning, SharedPreferences secret discovery, deep link fuzzing, and an OWASP MASVS compliance tracker with evidence vault export.

Targets mobile security researchers, red teamers, and reverse engineers who need a fast, scriptable tooling surface for authorized assessment of mobile applications — including game clients and anti-cheat protections.

## Links

- Repo: https://github.com/Kakaxh1/RootRaven

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[jadx]] · [[lamda]] · [[nightowl]] · [[auto-generate-frida-bypass-scripts-for-ssl-pinning-root-detection-on-android-ios]] · [[mobile-anti-cheat]]
