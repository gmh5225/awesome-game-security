---
title: EDRSandblast
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md
updated: 2026-07-18
confidence: medium
---

# EDRSandblast

C tool that blinds EDR/ETW detection on Windows via [[byovd]]: patches kernel callback routines, removes process/thread notify callbacks, disables ETW Threat-Intelligence provider feeds, and unhooks ntdll syscall stubs in user mode. Automates per-build offset resolution, driver load/cleanup, and ships a credential-dumping payload as a red-team / research demo. (source: wiki/sources/descriptions/wavestone-cdt__EDRSandblast.md)

README highlights `KernellandBypass/ETWThreatIntel.c` under the ETW Testing lane—useful opposite-side study to consumers such as [[tietwagent]] and provider browsers such as [[etw-explorer]]. Callback-removal research peers include [[bustercall]].

## Links

- Repo: https://github.com/wavestone-cdt/EDRSandblast
- ETW TI bypass sample: https://github.com/wavestone-cdt/EDRSandblast/blob/master/EDRSandblast/KernellandBypass/ETWThreatIntel.c

## Related

[[byovd]] · [[kernel-callbacks]] · [[tietwagent]] · [[etw-explorer]] · [[bustercall]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
