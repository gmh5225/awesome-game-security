---
title: PPLKiller
kind: entity
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/descriptions/gmh5225__PPLKiller.md
updated: 2026-08-11
confidence: medium
---

# PPLKiller

Windows BYOVD tool that disables **Protected Process Light (PPL)** on target processes by abusing a signed vulnerable driver or other kernel read/write primitive—commonly MSI Afterburner **`RTCore64.sys`**—to patch the **`EPROCESS` protection level** field. Downgrading PPL-protected antimalware and security-service processes enables debugging or user-mode termination that standard APIs block. Aimed at kernel researchers studying PPL enforcement and bypass techniques. (source: wiki/sources/descriptions/gmh5225__PPLKiller.md)

## Links

- Repo: https://github.com/gmh5225/PPLKiller

## Related

[[byovd]] · [[createprocessasppl]] · [[rtcore64-vulnerability]] · [[phantomkiller]] · [[process-killer-byovd]] · [[kslkatz]] · [[kvc]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
