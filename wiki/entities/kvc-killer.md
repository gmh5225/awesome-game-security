---
title: KvcKiller
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__kvcKiller.md
updated: 2026-11-09
confidence: medium
---

# KvcKiller

Windows x64 process-management tool (C++; GUI and headless CLI) that terminates antivirus and EDR processes that resist user-mode `TerminateProcess`. Uses a **dual-stage signed-kernel pipeline**: one driver supplies kernel memory read/write and lowers target **Process Protection Level (PPL)**, then a second issues IOCTL-based ring-0 termination; drivers ship in an embedded cabinet and load as demand-start services. Adds **IFEO offline-hive paralyze**, SCM restore, configurable target lists, and user-mode fallback when kernel kills are rejected. (source: wiki/sources/descriptions/wesmar__kvcKiller.md)

Positioned for authorized security research, malware analysis, and penetration testing when studying self-protected AV/EDR behavior—adjacent to same-author [[kvc]] DSE/PPL work, Defender neutralization via [[windefctl]], and BYOVD terminate/PPL-strip samples such as [[pplkiller]] and [[av-edr-killer]].

## Links

- Repo: https://github.com/wesmar/kvcKiller

## Related

[[kvc]] · [[kvcforensic]] · [[windefctl]] · [[byovd]] · [[pplkiller]] · [[av-edr-killer]] · [[process-killer-byovd]] · [[forceio]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
