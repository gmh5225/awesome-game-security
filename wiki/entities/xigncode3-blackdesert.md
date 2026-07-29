---
title: xigncode3-blackdesert
kind: entity
topics: [anti-cheat, reverse-engineering, windows-kernel]
sources:
  - wiki/sources/descriptions/miyakejima__xigncode3-blackdesert.md
updated: 2026-07-29
confidence: medium
---

# xigncode3-blackdesert

Layered static analysis and reconstruction archive for the XIGNCODE3 anti-cheat client on Black Desert. Documents how `xmag` and `xnina` container binaries unpack into user-mode modules, kernel drivers, Lua 5.3 scripts, and configuration data. (source: wiki/sources/descriptions/miyakejima__xigncode3-blackdesert.md)

## Pipeline

Eight-stage workflow: Python carving/unpacking tools → Ghidra decompilation of seventeen native modules → Lua recovery via unluac-rs → static triage with capa, FLOSS, and Detect It Easy. Includes dedicated work on the VMProtect-protected `xhunter1` kernel driver.

## Artifacts

Semantic inventories, behavior/architecture notes, IPC and detection subsystem specifications, and PowerShell live-host capture harnesses for reconciling static findings with runtime behavior.

## Links

- Repo: https://github.com/miyakejima/xigncode3-blackdesert

## Related

[[xign-poc-april-2026]] · [[ricochet-deobfuscator]] · [[kiroshi]] · [[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/windows-kernel]]
