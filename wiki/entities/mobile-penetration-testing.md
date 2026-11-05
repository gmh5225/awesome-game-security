---
title: Mobile Penetration Testing
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/MarwaBoualam__Mobile_Penetration_Testing.md
updated: 2026-11-05
confidence: medium
---

# Mobile Penetration Testing

**mobile-penetration-testing** (MarwaBoualam/Mobile_Penetration_Testing) is a **collection of Frida JavaScript hook scripts** for authorized Android mobile security assessments and hands-on reverse engineering. Scripts target lab APKs such as **AndroGoat** and the **OWASP UnCrackable** series, with overlap to CTF-style client-side anti-tamper practice relevant to mobile games. (source: wiki/sources/descriptions/MarwaBoualam__Mobile_Penetration_Testing.md)

## Capabilities

| Layer | Behavior |
|-------|----------|
| TLS / pinning | SSL/TLS certificate pinning bypass for **OkHttp**, **TrustManager**, and native **BoringSSL** paths (including Flutter apps) |
| Root / integrity | Root and jailbreak detection bypass for common lab targets |
| Anti-instrumentation | Native **libc** hooks that mask **Frida** or **Xposed** strings from runtime checks |
| Validation | Network failure callback logging without altering app behavior—helps confirm pinning or TLS bypasses during dynamic analysis |

(source: wiki/sources/descriptions/MarwaBoualam__Mobile_Penetration_Testing.md)

## Workflow

Typical authorized flow: combine static triage (JADX/Ghidra) with Frida attach or spawn on a rooted device or emulator, apply stack-appropriate pinning and root scripts, then use the network-failure logging helpers to verify whether TLS interception succeeded. Document hooks and observation points per [[mobile-network-trust-evidence]].

Complements bundled kits such as [[android-frida-bypass-suite]] and categorized script libraries such as [[frida-mobile-kit]] with a lab-focused script collection rather than a proxy toolchain.

## Links

- Repo: https://github.com/marwaboualam/mobile_penetration_testing (README `Cheat` / Frida)

## Related

[[frida]] · [[ssl-bypass]] · [[frida-mobile-kit]] · [[android-frida-bypass-suite]] · [[anti-frida-bypass]] · [[mobile-network-trust-evidence]] · [[mobile-anti-cheat]] · [[overviews/mobile-security]]
