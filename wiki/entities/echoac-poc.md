---
title: echoac-poc
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__echoac-poc.md
updated: 2026-08-09
confidence: medium
---

# echoac-poc

Writeup-backed proof of concept for vulnerabilities in **echo.ac**'s **`echo_driver.sys`**. The bundled example demonstrates privilege escalation to **NT AUTHORITY\SYSTEM** via the driver's read-memory IOCTL: leak `PsInitialSystemProcess`, walk `ActiveProcessLinks`, recover the SYSTEM token from `EPROCESS`, then overwrite the token of a newly spawned `cmd.exe`. (source: wiki/sources/descriptions/gmh5225__echoac-poc.md)

echo.ac is a commercial screensharing tool used in competitive communities; the repository doubles as a case study in how an anti-cheat-adjacent signed driver becomes an exploitation surface. Useful for Windows kernel researchers studying vulnerable-driver token theft, kernel read primitives, and real-world LPE chains built on third-party anti-cheat software. (source: wiki/sources/descriptions/gmh5225__echoac-poc.md)

## Links

- Repo: https://github.com/gmh5225/echoac-poc

## Related

[[byovd]] · [[kur]] · [[windows-kernel-exploits]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
