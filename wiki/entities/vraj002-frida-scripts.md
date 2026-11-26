---
title: Frida-Scripts (vraj002)
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/vraj002__Frida-Scripts.md
updated: 2026-11-26
confidence: medium
---

# Frida-Scripts (vraj002)

Curated **Frida JavaScript agents** for dynamic instrumentation of **hardened Android and iOS** clients. The main **Android harness** masks **root**, **emulator**, and **Frida** artifacts through native **filesystem** and **`/proc/maps`** hooks, **anti-debug** counters, optional **Play Integrity** hooks, and broad **TLS pinning** bypasses for **Conscrypt**, **OkHttp**, and related stacks (including **Flutter** per README curation). A companion **iOS** script applies the same source-masking pattern to **jailbreak** checks and **certificate pinning** on **arm64** devices. Additional scripts pair **SSL bypass** with **proxy-oriented VAPT** workflows and **anti-exit** crash mitigation for specific app targets. Targets **Frida 16 and 17** for reverse engineers, penetration testers, and mobile security researchers analyzing client-side protections. (source: wiki/sources/descriptions/vraj002__Frida-Scripts.md)

Distinct from [[frida-scripts]] (smartdone/Frida-Scripts; editor tooling / hooking snippets) and [[0xdea-frida-scripts]] (0xdea; cross-platform trace/discovery snippets).

## Links

- Repo: https://github.com/vraj002/Frida-Scripts

## Related

[[frida]] · [[frida-mobile-kit]] · [[android-frida-bypass-suite]] · [[ssl-bypass]] · [[frida-scripts]] · [[0xdea-frida-scripts]] · [[anti-frida-bypass]] · [[overviews/mobile-security]] · [[overviews/reverse-engineering]]