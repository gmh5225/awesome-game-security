---
title: MobSentry
kind: entity
topics: [mobile-security, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/ohmk1811__MobSentry.md
  - wiki/sources/README-categories.md
updated: 2026-10-06
confidence: medium
---

# MobSentry

**Evidence-first static analyzer** for **Android APK** and **iOS IPA** files (ohmk1811/MobSentry). Python with a Flask web UI and headless CLI; uses androguard and Mach-O/plist parsing to collect located snippets before grading findings with confidence labels and optional AI-assisted correlation over the evidence database. (source: wiki/sources/descriptions/ohmk1811__MobSentry.md)

## Capabilities

| Area | Coverage |
|------|----------|
| Transport trust | SSL pinning stack identification |
| Device integrity | Root and jailbreak detection routines |
| Instrumentation defense | Anti-debug and Frida instrumentation checks |
| Secrets / config | Hardcoded secrets, Firebase exposure |
| Platform policy | Manifest and network-security misconfigurations |
| Binary hygiene | Obfuscation, signing issues, third-party trackers |
| Bypass guidance | Stack-aware Frida and objection snippets tied to located evidence |
| Reporting | Interactive web reports and PDF exports |

## Architecture

| Layer | Role |
|-------|------|
| **Static parsers** | androguard (APK/DEX) + Mach-O/plist (IPA) snippet extraction |
| **Evidence database** | Located code snippets indexed before finding synthesis |
| **Finding engine** | Graded findings with confidence labels; optional AI-assisted correlation |
| **Interfaces** | Flask web UI for interactive review; headless CLI for automation |
| **Outputs** | Web report viewer + PDF export for authorized assessment workflows |

## Positioning

**Anti Cheat / Analysis Framework** lane beside authorized validation pipelines such as [[blc-gamesec-lab]] — aimed at penetration testers, reverse engineers, and researchers evaluating mobile app and game protections without replacing dynamic instrumentation.

Complements [[jadx]]/[[apktool]] static triage, runtime risk scanners such as [[security-risk-android]], and dynamic hooks via [[frida]] and [[root-detection-low-level]].

## Links

- Repo: https://github.com/ohmk1811/MobSentry

## Related

[[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[mobile-anti-cheat]] · [[blc-gamesec-lab]]
