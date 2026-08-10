---
title: Terminator
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__Terminator.md
updated: 2026-08-10
confidence: medium
---

# Terminator

Windows BYOVD tool that terminates protected processes—antivirus, EDR, and anti-cheat—that resist standard user-mode APIs because of kernel-level protections. It loads the signed Zemana anti-malware driver **`zam64.sys`** and issues its arbitrary process-termination IOCTL to kill targets from an unprivileged client. Aimed at red-team operators and security researchers studying BYOVD-based security-product termination. (source: wiki/sources/descriptions/gmh5225__Terminator.md)

## Links

- Repo: https://github.com/gmh5225/Terminator

## Related

[[byovd]] · [[zam64-zemina]] · [[watchdog-killer]] · [[av-edr-killer]] · [[phantomkiller]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
