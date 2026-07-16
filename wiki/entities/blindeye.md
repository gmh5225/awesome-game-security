---
title: BlindEye
kind: entity
topics: [anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/zouxianyu__BlindEye.md
updated: 2026-07-16
confidence: medium
---

# BlindEye

Kernel-oriented research sample labeled “Packet Fucker”: by hooking `ExAllocatePool` / `ExAllocatePoolWithTag` imports used by the [[battleye]] kernel module, it drops memory allocations tied to the BattlEye “report” path so kernel detections that depend on those allocations fail open. (source: wiki/sources/descriptions/zouxianyu__BlindEye.md)

Useful for researchers studying how BE report buffering/allocation can be disrupted from Ring0—not a production bypass.

## Links

- Repo: https://github.com/zouxianyu/BlindEye

## Related

[[battleye]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[kernel-callbacks]]
