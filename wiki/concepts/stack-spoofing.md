---
title: Stack Spoofing
kind: concept
topics: [game-hacking, anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/game-hacking.md
  - wiki/sources/descriptions/mgeeky__ThreadStackSpoofer.md
  - wiki/sources/descriptions/klezVirus__SilentMoonwalk.md
  - wiki/sources/descriptions/klezVirus__BYOUD.md
updated: 2026-08-01
confidence: medium
---

# Stack Spoofing

Techniques that **fabricate or rewrite call-stack frames** so thread stack walks see return addresses inside expected modules (`ntdll`, `kernel32`, game binaries) instead of cheat or manually mapped code. Used to evade anti-cheat stack inspection, ETW stack traces, and unwind-based hook detection. (source: wiki/sources/skills/game-hacking.md)

## Return-address spoofing

Before calling a sensitive API, replace the stack slot that holds the return address with a gadget or module address; restore after return. Evades naive `RtlWalkFrameChain` scans that flag returns outside loaded images.

## Synthetic call stacks

Build multi-frame stacks whose return PCs land in legitimate modules with plausible offsets. Must satisfy **`RtlVirtualUnwind`** and **`.pdata` / UNWIND_INFO`** consistency—spoofed frames that violate unwind metadata fail deeper validation.

## Unwind-metadata manipulation

Instead of fabricating return addresses on the stack, some frameworks **tamper with or leverage unwind metadata** (`.pdata`, `UNWIND_INFO`, runtime function tables) so stack walks and debugger unwinds skip or misinterpret portions of the real call chain. [[byoud]] (klezVirus; x64 Windows framework) illustrates this inverted approach—hiding arbitrary call-chain segments from debuggers and EDRs rather than patching individual return slots. (source: wiki/sources/descriptions/klezVirus__BYOUD.md)

## Detection surface

Anti-cheat walks thread stacks for non-module returns, validates unwind records, and correlates with shadow-stack / CET where enabled. Illustrative corpus samples: [[return-address-spoofer]], [[loudsunrun]], [[thread-stack-spoofer]] (PoC thread call-stack spoof for in-process shellcode hiding; bypass thread-based memory examination) (source: wiki/sources/descriptions/mgeeky__ThreadStackSpoofer.md), [[silent-moonwalk]] (klezVirus; TRUE call-stack spoofer from joint stack-spoofing research) (source: wiki/sources/descriptions/klezVirus__SilentMoonwalk.md), [[byoud]] (klezVirus; unwind-metadata manipulation to hide call-chain segments) (source: wiki/sources/descriptions/klezVirus__BYOUD.md), [[nocturneldr]], [[callout-poc]]. Defensive context: [[overviews/anti-cheat]] Detection:Spoof Stack lane.

## Related

[[kernel-callbacks]] · [[present-hook]] · [[windows-process-injection]] · [[overviews/game-hacking]] · [[overviews/anti-cheat]]
