---
title: NEXUS
kind: entity
topics: [mobile-security, game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/AtawurRahmanTanvir__NEXUS.md
updated: 2026-09-01
confidence: medium
---

# NEXUS

**NEXUS** (AtawurRahmanTanvir/NEXUS) is a root-required Android runtime utility written in Kotlin with a Jetpack Compose UI. It orchestrates privileged system operations for device identity control, environment sanitization, and live runtime observability via a macro-execution architecture: six command modules trigger bundled root engines through `su`. (source: wiki/sources/descriptions/AtawurRahmanTanvir__NEXUS.md)

**Engines:** `DeviceSpoofingEngine` and `BuildPropEngine` for Android ID, MAC, IMEI, and `build.prop` spoofing; `NetworkEngine` and `DnsTunnelEngine` for IP resets and iptables DNS routing; `MemoryPurgeEngine` for cache purging; `GmailAutomationEngine` for Google telemetry cleanup. A **Ghost Module** shortcut can silently run multi-layer stealth operations in the background without opening the main UI. A live terminal console fed by ViewModel state provides real-time feedback on each privileged action.

Targets rooted Android environments for game security research, device fingerprint evasion, anti-ban identity rotation, and ethical security experimentation. README category: Cheat / Android.

## Links

- Repo: https://github.com/AtawurRahmanTanvir/NEXUS

## Related

[[overviews/mobile-security]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[mobile-anti-cheat]] · [[hidemyandroid]] · [[spoofing-collection]] · [[kernelsu]] · [[magisk]] · [[rooturk-kernel]]
