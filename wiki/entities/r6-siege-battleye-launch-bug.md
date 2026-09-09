---
title: R6 Siege BattlEye Launch Bug
kind: entity
topics: [anti-cheat, battleye]
sources:
  - wiki/sources/descriptions/brandenbailey23__r6-siege-battleye-launch-bug.md
  - wiki/sources/README-categories.md
updated: 2026-09-09
confidence: medium
---

# R6 Siege BattlEye Launch Bug

Detailed **Markdown issue report** documenting a Rainbow Six Siege (Steam) launch failure after the **Y11S3** update: the client terminates during the **BattlEye** and **Ubisoft Sentinel** dual-anti-cheat handshake on standard launch paths but runs normally when started via `RainbowSixHelper.exe`. (source: wiki/sources/descriptions/brandenbailey23__r6-siege-battleye-launch-bug.md)

Aimed at game security researchers, anti-cheat analysts, and support engineers investigating BattlEye and dual-AC launch regressions on Windows—not a bypass toolkit.

Sits in the Cheat **Explore AntiCheat System:BE** lane as structured launch-path regression evidence beside emulator and client-interface samples such as [[fakeeye]] and [[beclient]].

## Scope

| Area | Focus |
|------|-------|
| **Failure mode** | Client exit during BattlEye + Ubisoft Sentinel handshake after Y11S3 |
| **Launch paths** | Standard Ubisoft Connect / Steam launch vs working `RainbowSixHelper.exe` path |
| **Evidence** | Windows System events, Ubisoft Connect logs, BEService + **BEDaisy** telemetry, byte-identical checksums |
| **Troubleshooting** | Structured timeline incl. service re-registration and quickboot staging clears |
| **Hypothesis** | Standard launch-path bootstrapping or server-side security/version negotiation—not corrupt binaries or blocked drivers |

## Evidence collected

| Source | Content |
|--------|---------|
| **Windows System** | Event log timeline around failed launches |
| **Ubisoft Connect** | Launcher and game-starter logs |
| **BattlEye** | Service and BEDaisy kernel driver telemetry |
| **Binaries** | Checksum comparisons across launch paths (byte-identical executables) |
| **Workarounds** | Documented working path via `RainbowSixHelper.exe` |

## Links

- Repo: https://github.com/brandenbailey23/r6-siege-battleye-launch-bug

## Related

[[battleye]] · [[bedaisy]] · [[battleye-re]] · [[fakeeye]] · [[beclient]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[research-rigor]]
