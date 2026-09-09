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

Detailed **Markdown issue report** documenting a Rainbow Six Siege (Steam) launch failure after the **Y11S3** update: the client terminates during the **BattlEye** and **Ubisoft Sentinel** anti-cheat handshake on standard launch paths but runs normally when started via `RainbowSixHelper.exe`. Compiles Windows System event logs, Ubisoft Connect launcher and game-starter logs, BattlEye service and **BEDaisy** kernel driver telemetry, byte-identical executable checksum comparisons, and a structured troubleshooting timeline including service re-registration and quickboot staging clears. Hypothesizes standard launch-path bootstrapping and possible server-side security or version negotiation rejection rather than corrupted game files or blocked drivers. (source: wiki/sources/descriptions/brandenbailey23__r6-siege-battleye-launch-bug.md)

Useful for studying dual-AC launch regressions, launch-path divergence, and BEDaisy load evidence—not a bypass toolkit.

## Evidence collected

| Source | Content |
|--------|---------|
| **Windows System** | Event log timeline around failed launches |
| **Ubisoft Connect** | Launcher and game-starter logs |
| **BattlEye** | Service and BEDaisy kernel driver telemetry |
| **Binaries** | Checksum comparisons across launch paths |
| **Workarounds** | Documented bypass via `RainbowSixHelper.exe` |

## Links

- Repo: https://github.com/brandenbailey23/r6-siege-battleye-launch-bug

## Related

[[battleye]] · [[battleye-re]] · [[bedaisy-bypass]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[research-rigor]]
