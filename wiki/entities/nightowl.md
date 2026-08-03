---
title: NightOwl
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/moaaz01__nightowl.md
updated: 2026-08-03
confidence: medium
---

# NightOwl

Unified Python CLI for Android APK security analysis that orchestrates [[jadx]], apktool, androguard, Semgrep, and [[frida]] into a nine-section scan covering permissions, secrets, endpoints, manifest components, vulnerabilities, and decompiled source. Detects mobile frameworks (Flutter, React Native, Cordova, Unity), profiles runtime self-protection (RootBeer, SafetyNet, Frida-hooking checks), and can emit tailored Frida bypass scripts per detection profile. Adds OWASP MASTG-aligned Semgrep rules, CVSS scoring, Shannon-entropy secret filtering, and structured JSON for automation pipelines. (source: wiki/sources/descriptions/moaaz01__nightowl.md)

Complements static triage peers ([[apkid]], [[game-engine-detector]], [[obfu-de-scate]]) and agent-facing decompile MCPs ([[apktool-mcp-server]], [[delamain]]) with a single end-to-end assessment + bypass-script lane for pentesters and mobile game RE.

## Links

- Repo: https://github.com/moaaz01/nightowl

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[frida]] · [[mobile-anti-cheat]] · [[jadx]] · [[apkid]] · [[game-engine-detector]] · [[unflutter]]
