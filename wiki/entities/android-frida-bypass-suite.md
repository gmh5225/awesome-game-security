---
title: Android Frida Bypass Suite
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/mrmtwoj__android-frida-bypass-suite.md
  - wiki/sources/README-categories.md
updated: 2026-10-23
confidence: high
---

# Android Frida Bypass Suite

**android-frida-bypass-suite** (mrmtwoj/android-frida-bypass-suite) is a **Frida-based Android pentest toolkit** listed under README **Cheat / Frida**. Hooks inject at runtime **without modifying the target APK**—suited to intercepting HTTPS, surfacing crypto material, and running root- or integrity-gated Android apps (including games) on rooted or instrumented devices. (source: wiki/sources/descriptions/mrmtwoj__android-frida-bypass-suite.md)

## Capabilities

| Layer | Behavior |
|-------|----------|
| Root / integrity | Java-layer and native **libc** root-detection bypass |
| TLS / pinning | Defeat certificate pinning on **OkHttp**, **TrustKit**, **Conscrypt**, **WebView**, and related stacks |
| Crypto | Hook **AES key material** and cipher I/O for visibility into app crypto |
| Proxy | Companion **Python forward proxy** with protocol/domain allow-block lists and live traffic logging |
| Integration | **Burp Suite** workflow plus **adb reverse** tunneling; targets **Android 5 through 14** |

(source: wiki/sources/descriptions/mrmtwoj__android-frida-bypass-suite.md)

## Workflow

Typical authorized assessment flow: attach or spawn with the bundled Frida script to neutralize root checks and stack-specific pinning, route device traffic through the Python proxy (optionally into Burp via adb reverse), and correlate decrypted or logged bodies with AES hook output. Pair capture discipline with [[mobile-network-trust-evidence]]—document which TLS stack hooks applied and what remained unobserved.

Complements categorized hook kits such as [[frida-mobile-kit]] and universal scripts such as [[ssl-bypass]] with a single bundled script plus proxy-oriented traffic capture.

## Links

- Repo: https://github.com/mrmtwoj/android-frida-bypass-suite (README `Cheat` / Frida)

## Related

[[frida]] · [[frida-mobile-kit]] · [[ssl-bypass]] · [[mobile-network-trust-evidence]] · [[root-detection-low-level]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]
