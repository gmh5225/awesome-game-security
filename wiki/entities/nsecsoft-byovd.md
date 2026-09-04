---
title: NSecSoft BYOVD
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/ANYLNK__NSecSoftBYOVD.md
updated: 2026-09-04
confidence: medium
---

# NSecSoft BYOVD

Windows [[concepts/byovd|BYOVD]] proof of concept for **process termination**: a user-mode executable loads the signed vulnerable third-party driver **`NSecKrnl.sys`** and uses it to perform privileged actions against a target PID. The repository frames the technique against real-world abuse patterns and references its assigned CVE entry. Primarily relevant to Windows kernel security research, offensive tooling analysis, and anti-cheat or endpoint defense hardening. (source: wiki/sources/descriptions/ANYLNK__NSecSoftBYOVD.md)

## Links

- Repo: https://github.com/ANYLNK/NSecSoftBYOVD

## Related

[[concepts/byovd]] · [[process-killer-byovd]] · [[terminator]] · [[watchdog-killer]] · [[edr-xdr-av-killer]] · [[loldrivers]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
