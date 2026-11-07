---
title: ForceIO
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/wesmar__ForceIO.md
updated: 2026-11-07
confidence: medium
---

# ForceIO

Windows command-line tool for force-delete, rename, move, and copy on files and directories that user-mode APIs cannot touch because minifilters such as **WdFilter** block normal I/O. Loads a WHCP-signed third-party kernel driver (`IObitUnlocker.sys`) in a short-lived service session and issues buffered IOCTLs so operations run below the Filter Manager stack. Supports wildcards, lock enumeration, registry hive snapshots, and WOW64 System32 path handling. (source: wiki/sources/descriptions/wesmar__ForceIO.md)

Implementation is hand-coded C via the Win32 API without the CRT; the driver ships LZX-compressed in embedded CAB resources, with a runtime mathematical stager to satisfy the driver’s on-disk caller checksum checks while keeping the binary small. Positioned for authorized Windows kernel and anti-malware bypass study—e.g. manipulating protected logs, Defender artifacts, or locked game/system files on machines you own or may test. (source: wiki/sources/descriptions/wesmar__ForceIO.md)

## Links

- Repo: https://github.com/wesmar/ForceIO

## Related

[[byovd]] · [[windefctl]] · [[vaultguard]] · [[memfilter-fn-driver]] · [[file-recovery-tool]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
