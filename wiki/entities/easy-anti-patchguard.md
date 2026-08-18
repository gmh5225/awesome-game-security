---
title: EasyAntiPatchGuard
kind: entity
topics: [windows-kernel, reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/armasm__EasyAntiPatchGuard.md
updated: 2026-08-18
confidence: medium
---

# EasyAntiPatchGuard

Windows kernel **proof of concept** that interferes with [[patchguard]] execution behavior via a driver and low-level assembly hook logic — observing or short-circuiting specific dispatch paths in protected routines. Targets **Win8 through Win10-era** builds and documents call-chain analysis from kernel debugging sessions for kernel security and anti-cheat researchers studying KPP internals and bypass concepts. (source: wiki/sources/descriptions/armasm__EasyAntiPatchGuard.md)

Sits alongside partial/runtime PG disable PoCs such as [[tableflipper]] and [[vulnerablepatchguardexploit]], educational PG walkthroughs such as [[demystifying-patchguard]], and PG monitoring tooling such as [[sushi]].

## Links

- Repo: https://github.com/armasm/EasyAntiPatchGuard

## Related

[[patchguard]] · [[tableflipper]] · [[vulnerablepatchguardexploit]] · [[demystifying-patchguard]] · [[sushi]] · [[overviews/windows-kernel]] · [[overviews/game-hacking]]
