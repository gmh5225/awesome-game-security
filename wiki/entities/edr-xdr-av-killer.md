---
title: EDR-XDR-AV-Killer
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/EvilBytecode__EDR-XDR-AV-Killer.md
updated: 2026-08-25
confidence: medium
---

# EDR-XDR-AV-Killer

**EDR-XDR-AV-Killer** (EvilBytecode) is a **Go** reproduction of the **Spyboy Terminator** technique for terminating **EDR, XDR, and antivirus** processes. It loads the signed Zemana anti-malware driver **`zam64.sys`**, abuses an **IOCTL-based process-ID trust list** to bypass the driver’s access controls, then invokes **kernel-level process-termination primitives** to kill protected security software. Primary audience: security researchers studying **BYOVD** attacks and **EDR evasion** tradecraft. (source: wiki/sources/descriptions/EvilBytecode__EDR-XDR-AV-Killer.md)

Same **`zam64.sys`** backend as [[terminator]] and [[zam64-zemina]]; differs in Go implementation and explicit IOCTL trust-list bypass framing.

## Links

- Repo: https://github.com/EvilBytecode/EDR-XDR-AV-Killer

## Related

[[byovd]] · [[terminator]] · [[zam64-zemina]] · [[av-edr-killer]] · [[watchdog-killer]] · [[blackout]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
