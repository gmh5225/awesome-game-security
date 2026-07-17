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
  - wiki/sources/descriptions/zorftw__revert-mapper.md
  - wiki/sources/descriptions/zorftw__lsass-extend-mapper.md
  - wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md
  - wiki/sources/descriptions/zodiacon__EtwExplorer.md
updated: 2026-07-17
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

**Detection:** memory hashing / manual-map detection; process handle stripping; [[kernel-callbacks]]; Segment Heap–aware pool scanning; behavioral/ML aimbot signals; screenshot + heartbeat; ETW provider/event discovery for telemetry design (e.g. [[etw-explorer]]). Trusted-process mapping (e.g. [[lsass-extend-mapper]] hosting unsigned drivers via lsass address-space extend) and post-execution map cleanup (e.g. [[revert-mapper]] freeing mapped driver memory and pool-tag traces) are common research counterparts to those scanners. (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md) (source: wiki/sources/descriptions/zorftw__revert-mapper.md) (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md)

**Architecture:** user-mode scanners → kernel callbacks/VAD → optional hypervisor EPT protection → server-side replay/stats.

**Threats defended against:** injected code, [[byovd]], hypervisor abuse (stress/test refs such as [[vt-debuuger]] under hacked-hypervisor detection), [[dma]] (PCIe fingerprinting + IOMMU + TPM attestation), AI visual cheats with hardware input. (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md)

**Platform trust:** DSE, [[patchguard]], [[hvci]]/VBS, Secure Boot.

**Obfuscation tooling:** [[shredder-rs]] — x86_64 polymorphic instruction shredding (context-preserving) for AC/obfuscation-engine research. (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md) Engine-side data hiding: [[static-variables-obfuscator-ue4]] obfuscates UE4 static variables against Cheat Engine–style scans (`Game Engine Protection:Unreal`). (source: wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md)


## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[dma]] · [[iommu]] · [[present-hook]] · [[vac3-inhibitor]] · [[vt-debuuger]] · [[shredder-rs]] · [[static-variables-obfuscator-ue4]] · [[blindeye]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[etw-explorer]]

## README map

`Anti Cheat` (~589 links): guides, stress/unit-test harnesses, packers, engine protection (Unreal/Unity/Source), and a wide `Detection:*` tree (hook, memory integrity, shellcode, attach, aimbot, hide, vulnerable driver, hacked hypervisor, virtual environments, HWID, speedhack, injection, stack spoof, ESP, DMA, wallhack, obfuscation, Android root). Cross-links `Windows Security Features` and Cheat PatchGuard/DSE lanes. (source: wiki/sources/README-categories.md)
