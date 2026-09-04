---
title: Android Security Wizard
kind: entity
topics: [mobile-security, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/savagedamage__android-security-wizard.md
  - wiki/sources/README-categories.md
updated: 2026-09-04
confidence: medium
---

# Android Security Wizard

**Integrated Android security research corpus** pairing one operational **SKILL.md** guide with **twenty companion documents** on the full mobile assessment workflow. Covers static and dynamic analysis of APKs, DEX, and native libraries using **Frida**, **Objection**, **Ghidra**, and **ADB/Shizuku**, plus commercial packer and protector bypass techniques for **DexGuard**, **Bangcle**, and similar schemes. Also documents exploit identification workflows, **ARM64 kernel exploit development**, malware detection and C2 attribution, and platform security changes across **Android 14–18**. (source: wiki/sources/descriptions/savagedamage__android-security-wizard.md)

Aimed at reverse engineers, mobile security researchers, and practitioners assessing app protections, instrumentation defenses, and threat behavior on Android devices — listed under README **Cheat > Guide** beside curated Android security indexes such as [[awesome-android-security]].

## Structure

One integrated **SKILL.md** operational guide anchors **twenty companion documents** that walk the full assessment lifecycle: triage → static decode → dynamic instrumentation → native RE → protector bypass → exploit/malware follow-up. (source: wiki/sources/descriptions/savagedamage__android-security-wizard.md)

## Toolchain

| Layer | Tools / focus |
|-------|----------------|
| Static | APK/DEX decode, native `.so` disassembly in [[ghidra]] |
| Dynamic | [[frida]], **Objection**, **ADB/Shizuku** attach and scripting |
| Protectors | DexGuard, Bangcle, and similar commercial packer bypass |
| Kernel | ARM64 exploit identification and development methodology |
| Threat intel | Malware detection patterns and C2 attribution |

## Coverage areas

- **Static/dynamic APK analysis** — DEX, native `.so`, and runtime instrumentation
- **Commercial protector bypass** — DexGuard, Bangcle, and related packers
- **Kernel exploit methodology** — ARM64 development and triage workflows
- **Malware triage** — detection patterns and C2 attribution
- **Platform deltas** — Android 14 through 18 security changes

## Links

- Repo: https://github.com/savagedamage/android-security-wizard

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[frida]] · [[ghidra]] · [[apklab]] · [[appsealing-reversal]] · [[g-presto-anti-cheat-reverse-engineered]] · [[mobile-anti-cheat]] · [[research-rigor]]
