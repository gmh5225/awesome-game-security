---
title: XenoDLLRE
kind: entity
topics: [anti-cheat, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/aauuzy__XenoDLLRE.md
updated: 2026-11-10
confidence: medium
---

# XenoDLLRE

**Defensive research** repository that statically reverse engineers the **Xeno** Windows Roblox script executor (**v1.3.65**) and documents how its native DLL attaches, runs user Luau, and leaves detectable artifacts—without shipping or improving executor functionality. (source: wiki/sources/descriptions/aauuzy__XenoDLLRE.md)

## Analysis surface

| Area | Documented behavior |
|------|---------------------|
| Attach | Native DLL injection path; **en-us locale `ModuleScript` bytecode replacement** for script delivery |
| Control plane | Localhost **HTTP** API for executor orchestration |
| Payload protection | **XOR** + **zstd** on embedded resources |
| Compilation | Luau compile / workflow notes with evidence-graded findings |

## Tooling

Python utilities **profile DLL samples**, **decrypt embedded resources**, **compare builds**, and run a **score-based file scanner** alongside **YARA** rules derived from the static analysis. Architecture write-ups and IOC-style notes target game security, anti-cheat, and RE teams on Windows.

Pair with [[rustblox]] client watchdog patterns, [[byfron-bypass]] offensive client research, Luau analysis via [[wontree-rblx-dumper]], and Roblox server-side AC samples such as [[advanced-anticheat]] / [[shprotect-ac]].

## Links

- Repo: https://github.com/aauuzy/XenoDLLRE

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[byfron-bypass]] · [[rustblox]] · [[wontree-rblx-dumper]] · [[roblox-external-base]]
