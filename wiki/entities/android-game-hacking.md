---
title: Android Game Hacking (Droid-arsenal)
kind: entity
topics: [mobile-security, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/zezindozap__android-game-hacking.md
  - wiki/sources/README-categories.md
updated: 2026-11-24
confidence: medium
---

# Android Game Hacking (Droid-arsenal)

**Droid-arsenal** (`zezindozap/android-game-hacking`) is a reproducible **on-device toolkit** for analyzing and modifying Android applications—especially games—while keeping interference low by avoiding APK patches, system changes, and unnecessary [[frida]] use where possible. A Python **`dops` CLI** orchestrates reconnaissance, backup and restore, live memory scanning, save-file sniffing, [[il2cpp]] dumping, in-app purchase testing with FakeBinder-style billing hooks, [[lsposed-universal-template|LSPosed]] module scoping, and selective TLS interception via mitmproxy with per-app SNI routing. Per-application settings live in small TOML target files; runbooks and declarative recipes document workflows for memory edits, IAP forgery, MITM validation bypass, and clean rollback on rooted devices using [[kernelsu]] or [[magisk]]. (source: wiki/sources/descriptions/zezindozap__android-game-hacking.md)

Listed under Cheat — reproducible on-device Android game analysis (`dops` CLI).

## CLI scope

- **Recon & state** — target discovery, backup/restore, rollback-oriented evidence preservation.
- **Runtime edit lanes** — live memory scan, save-file sniffing, IL2CPP dump hooks.
- **Billing & modules** — FKIAB/LSPosed IAP tooling beside multi-store billing research such as [[com-fuck-iab]].
- **Network trust** — selective mitmproxy interception with per-app SNI routing for pinning/validation study.

## Audience

Security researchers and advanced players who need structured, repeatable Android game reverse engineering and anti-cheat or billing research on hardware they control.

## Links

- Repo: https://github.com/zezindozap/android-game-hacking

## Related

[[vd-backup]] · [[mobile-harness]] · [[inject-hooks-android-rs]] · [[com-fuck-iab]] · [[il2cpp]] · [[mobile-network-trust-evidence]] · [[overviews/mobile-security]] · [[overviews/game-hacking]]