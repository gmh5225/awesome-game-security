---
title: Anti-Cheat
kind: overview
topics: [anti-cheat]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zyhp__vac3_inhibitor.md
  - wiki/sources/descriptions/zxd1994__vt-debuuger.md
  - wiki/sources/descriptions/zx0CF1__shredder-rs.md
  - wiki/sources/descriptions/zouxianyu__BlindEye.md
updated: 2026-07-16
confidence: high
---


# Anti-Cheat

Layered game protection across kernel drivers, privileged services, in-game modules, and backend telemetry. Modern systems monitor handles, image loads, memory integrity, driver trust, virtualization abuse, DMA, and suspicious input. (source: wiki/sources/skills/anti-cheat.md)

## Major systems

- [[easy-anti-cheat]] — service + driver + game-facing integrity (Fortnite, Apex, Rust)
- [[battleye]] — handle protection, process/memory scanning (PUBG, R6, DayZ); research ref [[blindeye]] drops BE report-path pool allocs via hooked `ExAllocatePool*` (source: wiki/sources/descriptions/zouxianyu__BlindEye.md)
- [[vanguard]] — boot-start driver, early driver allowlisting (Valorant, LoL)
- FACEIT AC, VAC (user-mode signatures), GameGuard, XIGNCODE3, ACE
- [[vac3-inhibitor]] — C++ VAC3 exploration (hooking / memory analysis) under cheat → explore anticheat:vac (source: wiki/sources/descriptions/zyhp__vac3_inhibitor.md)


## Key sub-areas

**Detection:** memory hashing / manual-map detection; process handle stripping; [[kernel-callbacks]]; Segment Heap–aware pool scanning; behavioral/ML aimbot signals; screenshot + heartbeat.

**Architecture:** user-mode scanners → kernel callbacks/VAD → optional hypervisor EPT protection → server-side replay/stats.

**Threats defended against:** injected code, [[byovd]], hypervisor abuse (stress/test refs such as [[vt-debuuger]] under hacked-hypervisor detection), [[dma]] (PCIe fingerprinting + IOMMU + TPM attestation), AI visual cheats with hardware input. (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md)

**Platform trust:** DSE, [[patchguard]], [[hvci]]/VBS, Secure Boot.

**Obfuscation tooling:** [[shredder-rs]] — x86_64 polymorphic instruction shredding (context-preserving) for AC/obfuscation-engine research. (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md)

## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[dma]] · [[iommu]] · [[present-hook]] · [[vac3-inhibitor]] · [[vt-debuuger]] · [[shredder-rs]] · [[blindeye]]

## README map

`Anti Cheat` (~565 links): guides, packers, engine protection, `Detection:*` (hook, DMA, injection, ESP, root, …), Ring0/Ring3 callbacks, forensics. Cross-links `Windows Security Features`. (source: wiki/sources/README-categories.md)
