---
title: com.sipvlib.anticheat
kind: entity
topics: [anti-cheat, mobile-security, game-engine]
sources:
  - wiki/sources/descriptions/phajmvawnsix__com.sipvlib.anticheat.md
updated: 2026-07-26
confidence: medium
---

# com.sipvlib.anticheat

Unity UPM package (C#) providing soft anti-cheat signals for rewards, cooldowns, daily resets, and similar cheat-sensitive gameplay. **GameTime** fetches UTC from a fallback chain of public time APIs, advances between fetches with `Time.deltaTime` instead of re-reading the device clock, and re-verifies on an interval and when the app regains focus. **IntegrityChecker** runs heuristic checks for an attached debugger, Android/iOS root or jailbreak paths, Android emulators, and clock drift against the verified time. Integrates with other SiPVLib modules and UniTask. (source: wiki/sources/descriptions/phajmvawnsix__com.sipvlib.anticheat.md)

Sits in the Unity mobile soft-AC / integrity lane beside [[free-rasp-unity-poc]] and Android RASP [[droidshield]] — lighter than kernel AC products; aimed at not trusting the device clock alone.

## Links

- Repo: https://github.com/phajmvawnsix/com.sipvlib.anticheat

## Related

[[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[free-rasp-unity-poc]] · [[droidshield]] · [[anti-emulator]] · [[il2cpp]]
