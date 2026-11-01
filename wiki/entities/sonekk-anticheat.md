---
title: Sonekk Anti-Cheat
kind: entity
topics: [anti-cheat, mobile-security, game-engine]
sources:
  - wiki/sources/descriptions/sonekkdev__sonekk-anticheat.md
  - wiki/sources/README-categories.md
updated: 2026-11-01
confidence: high
---

# Sonekk Anti-Cheat

**Sonekk Anti-Cheat** ([sonekkdev/sonekk-anticheat](https://github.com/sonekkdev/sonekk-anticheat)) is a **modular integrity and anti-cheat stack** for standalone **Android VR** titles—especially Gorilla Tag–style fan games on Quest- and Pico-class headsets. Four optional layers deploy independently; **JavaScript** powers server modules and CLI tooling, **Unity** packages integrate on-device reporting, and **ban/enforcement policy stays on the operator backend** rather than trusting the client. No kernel drivers or hosted third-party telemetry. (source: wiki/sources/descriptions/sonekkdev__sonekk-anticheat.md)

## Layers

| Layer | Role |
|-------|------|
| **Guard** | C++ native library in the APK: root, **Frida**, debuggers, code hooks; **HMAC-signed** reports to a Node reference server that scores findings and can verify **Android Keystore** attestation |
| **Motion** | Server-side movement validation: impossible speed, flight, teleports |
| **Seal** | Build and verify **ZIP manifest fingerprints** of shipped APKs (repacks, injected libraries) |
| **AntiADB** | Mid-session settings changes suggesting **ADB** tampering without punishing developer mode alone |

## Architecture

- **Client** — Unity packages wire Guard evidence collection and movement reporting into the game loop.
- **Reference server** — Optional Node stack validates signed telemetry, attestation, and movement payloads; operators define watch/review/block and ban logic server-side.
- **Audience** — Small studios wanting practical layered game security on standalone VR without commercial RASP or platform AC replacement.

Guard overlaps the earlier [[sonekk-guard1]] client-server integrity design; this repo is the umbrella modular stack listed in README **Anti Cheat**. (source: wiki/sources/descriptions/sonekkdev__sonekk-anticheat.md)

## Links

- Repo: https://github.com/sonekkdev/sonekk-anticheat

## Related

[[sonekk-guard1]] · [[overviews/anti-cheat]] · [[overviews/mobile-security]] · [[mobile-anti-cheat]] · [[mobsentry]] · [[frida]] · [[keyattestation]] · [[com-sipvlib-anticheat]]
