---
title: molt-DEX
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/ReSo7200__molt-dex.md
updated: 2026-10-17
confidence: medium
---

# molt-DEX

**Staged, evidence-first Claude skill and documentation pipeline** for reverse engineering, modding, and security assessment of Android applications—from plain APKs through heavily obfuscated builds. Workflows move from acquisition and [[apktool]]-based smali decoding through static mapping, secrets sweeps, and optional on-device confirmation with **adb**, **scrcpy**, **DexKit** runtime resolution, and hooking via the Xposed API with **LSPosed**, **LSPatch**, or [[frida]]. (source: wiki/sources/descriptions/ReSo7200__molt-dex.md)

Core technique: resolve code by **stable strings**, method shape, and class relationships rather than obfuscated names. Helper shell and Python scripts support string indexing, manifest summaries, and device workflows. Supporting references cover authorization boundaries, an obfuscation ladder from **R8** through packers and anti-tamper, and report templates for verified findings. Targets practitioners doing authorized Android reverse engineering, vulnerability assessment, and resilient modding against name and string obfuscation. Listed in the README under **Cheat > Guide**.

## Pipeline stages

| Stage | Focus |
|-------|--------|
| Acquisition | APK pull/install; artifact inventory |
| Static | [[apktool]] smali decode; mapping; secrets sweeps |
| Runtime | DexKit resolution; adb/scrcpy confirmation |
| Instrumentation | LSPosed / LSPatch / [[frida]] hooks |
| Reporting | Verified-finding templates; obfuscation ladder context |

## Links

- Repo: https://github.com/ReSo7200/molt-dex

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[apktool]] · [[jadx]] · [[dexkit-android]] · [[frida]] · [[android-security-wizard]] · [[mobile-re-skill]] · [[research-rigor]] · [[obfuscapk]]
