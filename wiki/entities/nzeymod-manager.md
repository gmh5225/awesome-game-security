---
title: NZeyMod Manager
kind: entity
topics: [mobile-security, game-hacking]
sources:
  - wiki/sources/descriptions/KiZakiXD__NZeyMod-Manager.md
updated: 2026-11-23
confidence: medium
---

# NZeyMod Manager

Lightweight **Android companion launcher** written in Java without Gradle (manual Android SDK build; optional HTML + service-worker web prototype) that prepares, verifies, and imports the **NZeyMod** custom ROM into **NZey Master**—a repackaged Virtual Master environment running Android 11 with a Pixel 5 device profile. Targets researchers and advanced users who operate rooted or Magisk-equipped **virtual** Android instances for integrity-bypass testing, modding, and related mobile security experimentation—not a standalone emulator or hypervisor. (source: wiki/sources/descriptions/KiZakiXD__NZeyMod-Manager.md)

## Capabilities

- **ROM pipeline** — SHA-256 validation of full or split ROM images; merge multi-part archives before import.
- **Identity profiles** — generate and persist spoofed device identities with Luhn-valid IMEIs.
- **Magisk profiles** — toggle Magisk-related modules per profile.
- **Keyboxes** — manage keyboxes for Play Integrity workflows on lab guests.

Listed in the README as an Android companion launcher for NZeyMod ROM on NZey Master (Virtual Master).

## Links

- Repo: https://github.com/KiZakiXD/NZeyMod-Manager

## Related

[[overviews/mobile-security]] · [[concepts/mobile-trust-boundaries]] · [[jerrymanager]] · [[tee-forge-cd]] · [[zamr]] · [[magisk]] · [[mobile-anti-cheat]]