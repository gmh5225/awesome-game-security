---
title: ApplistDetector
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/Dr-TSNG__ApplistDetector.md
updated: 2026-08-26
confidence: medium
---

# ApplistDetector

**ApplistDetector** (Dr-TSNG) is an Android **detection library** and demo app for identifying suspicious software environments such as **Magisk** and **Xposed**. Built with **Kotlin** and native **C++**, it combines **package inspection**, **filesystem artifact checks**, **syscall-based file probing**, and **Xposed status detection**. The code also probes **dual/work profile** anomalies and known rooting-related traces. Primary use: mobile anti-cheat, root detection, and app-integrity research. (source: wiki/sources/descriptions/Dr-TSNG__ApplistDetector.md)

Complements package-launch probes such as [[root-app-detector]], multi-check offline inspectors such as [[advanced-root-checker]], and Magisk POC archives such as [[magisk-detection]]—opposite root/hide frameworks [[magisk]], [[kernelsu]], and Xposed/LSPosed stacks.

## Links

- Repo: https://github.com/Dr-TSNG/ApplistDetector

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[root-app-detector]] · [[advanced-root-checker]] · [[magisk-detection]] · [[detect-zygisk]] · [[magisk]] · [[zygisk-on-kernelsu]]
