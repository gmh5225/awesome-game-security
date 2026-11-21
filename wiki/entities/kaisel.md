---
title: Kaisel
kind: entity
topics: [mobile-security, anti-cheat]
sources:
  - wiki/sources/descriptions/0xdhanesh__Kaisel.md
updated: 2026-11-21
confidence: medium
---

# Kaisel

Open-source **iOS Runtime Application Self-Protection (RASP)** reference implementation (0xdhanesh/Kaisel). Ships as a Swift package with a C detection core, two sideloadable demo apps for on-device trials, and an optional Python server that verifies Apple App Attest assertions, re-scores sealed reports, and returns allow, step-up, or deny decisions. Coverage spans syscall and mount-table jailbreak probes, dyld image classification, Frida and debugger signals, code-signing and entitlement checks, hook and trampoline analysis, weighted risk scoring, and tamper-evident self-protection for iOS 15 through 27. Aimed at security researchers, red teams, and engineers who need a lab baseline to evaluate or compare commercial anti-tamper and RASP approaches for mobile games and high-assurance apps—not as a sole production control. (source: wiki/sources/descriptions/0xdhanesh__Kaisel.md)

Sits in the iOS mobile RASP lane beside Talsec [[free-rasp-ios]], Android modular RASP samples such as [[mobshield-android]], and consent-based mobile integrity workflows such as [[abbys-anti-cheat]].

## Links

- Repo: https://github.com/0xdhanesh/Kaisel

## Related

[[overviews/mobile-security]] · [[overviews/anti-cheat]] · [[frida]] · [[free-rasp-ios]] · [[mobshield-android]] · [[mobsentry]] · [[abbys-anti-cheat]]