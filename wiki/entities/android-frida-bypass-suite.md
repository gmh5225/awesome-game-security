---
title: Android Frida Bypass Suite
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrmtwoj__android-frida-bypass-suite.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: medium
---

# Android Frida Bypass Suite

**android-frida-bypass-suite** (mrmtwoj/android-frida-bypass-suite) is a **Frida-based Android pentest toolkit** listed under README **Cheat / Frida**. A main Frida script bypasses **root detection** at Java and native libc layers, hooks **AES key material and cipher I/O**, and defeats **SSL certificate pinning** across OkHttp, TrustKit, Conscrypt, WebView, and related stacks. A companion **Python forward proxy** adds protocol and domain allow/block filtering with live traffic logging; the workflow integrates with **Burp Suite** and **adb reverse** tunneling on Android 5 through 14. Targets security researchers and reverse engineers who need HTTPS interception, crypto visibility, and protected Android apps—including games—on rooted or instrumented devices. (source: wiki/sources/descriptions/mrmtwoj__android-frida-bypass-suite.md)

Complements categorized hook kits such as [[frida-mobile-kit]] and universal scripts such as [[ssl-bypass]] with a single bundled script plus proxy-oriented traffic capture.

## Links

- Repo: https://github.com/mrmtwoj/android-frida-bypass-suite (README `Cheat` / Frida)

## Related

[[frida]] · [[frida-mobile-kit]] · [[ssl-bypass]] · [[mobile-network-trust-evidence]] · [[root-detection-low-level]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
