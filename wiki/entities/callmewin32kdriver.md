---
title: CallMeWin32kDriver
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__CallMeWin32kDriver.md
updated: 2026-08-14
confidence: medium
---

# CallMeWin32kDriver

Driver loader that loads unsigned kernel drivers through the **win32k.sys session-driver loading mechanism** instead of the standard `NtLoadDriver` / PiDDBCache path. Originally reverse-engineered from a PUBG cheat driver; advertises resistance to direct memory dumps by anti-rootkit tooling and bypass of **MmCopyMemory**-based cheat detection. (source: wiki/sources/descriptions/gmh5225__CallMeWin32kDriver.md)

Sits in the same unsigned-driver map lane as session-space mappers such as [[driver-session-mapper]] and BYOVD-backed loaders such as [[capcomlib]], but routes through the GUI-subsystem session-driver load path modeled on **win32k.sys** rather than hooking generic `ntoskrnl` callbacks or exploiting a vulnerable signed driver.

## Links

- Repo: https://github.com/gmh5225/CallMeWin32kDriver

## Related

[[overviews/windows-kernel]] · [[overviews/anti-cheat]] · [[driver-session-mapper]] · [[win32k-file-collection]] · [[win32k-file-collection2]] · [[capcomlib]] · [[known-driver-mappers]] · [[cheat-driver]] · [[readphys]]
