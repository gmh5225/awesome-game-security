---
title: Konzte Faceit (KONZTE GUARD)
kind: entity
topics: [anti-cheat, game-hacking, windows-kernel]
sources:
  - wiki/sources/descriptions/sr-star-trek__konzte-faceit.md
updated: 2026-11-10
confidence: medium
---

# Konzte Faceit (KONZTE GUARD)

Published **Konzte Faceit** desktop client and **KONZTE GUARD** source (sr-star-trek) for the **Combat Master** third-party competitive platform: a **user-mode** anti-cheat stack bundled with a matchmaking client rather than a commercial kernel AC product. Researchers can study how the client installer deploys a background guard on Windows and what detection surfaces it documents. (source: wiki/sources/descriptions/sr-star-trek__konzte-faceit.md)

## Architecture

| Component | Role |
|-----------|------|
| **Desktop shell** | Rust + Tauri host with HTML/CSS/JavaScript UI |
| **KONZTE GUARD service** | Native Rust Windows background service monitoring Combat Master |
| **Optional C# scanners** | Deeper Windows scanning paths beside the Rust guard |
| **Updater / installer** | ed25519-verified self-updates; admin-privilege hooks register the guard service |

## Detection surfaces

- Kernel-related **misconfiguration** checks on the host
- Known **cheat modules and injectors**
- **Executable memory** signature matching
- **Tampered game file** integrity signals
- **Signature databases** with **HWID binding**
- Telemetry plus **limited guarded file uploads** for staff review (not full kernel enforcement)

Sits beside other published third-party client AC stacks such as [[phoenix-ac]] (FiveM) and session usermode tooling such as [[deadlock-anti-cheat]], and complements commercial FACEIT-kernel exploration samples such as [[ec-pro-lan]] / [[faceoff]]—here the emphasis is **documented usermode guard deployment** for a non-Steam competitive title.

## Links

- Repo: https://github.com/sr-star-trek/konzte-faceit

## Related

[[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/windows-kernel]] · [[phoenix-ac]] · [[ultimate-anti-cheat]] · [[cheatguard]] · [[hwid-spoofing]]
