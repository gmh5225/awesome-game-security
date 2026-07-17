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
  - wiki/sources/descriptions/zoand__Injectors.md
  - wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md
  - wiki/sources/descriptions/zhaodice__qemu-anti-detection.md
  - wiki/sources/descriptions/zer0condition__hv.md
  - wiki/sources/descriptions/zer0condition__Ophion.md
  - wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md
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

**Detection:** memory hashing / manual-map detection; process handle stripping; [[kernel-callbacks]]; Segment Heap–aware pool scanning; behavioral/ML aimbot signals; screenshot + heartbeat; ETW provider/event discovery for telemetry design (e.g. [[etw-explorer]]). Trusted-process mapping (e.g. [[lsass-extend-mapper]] hosting unsigned drivers via lsass address-space extend) and post-execution map cleanup (e.g. [[revert-mapper]] freeing mapped driver memory and pool-tag traces) are common research counterparts to those scanners. Thread-enumeration detectors (looking for manual-map worker threads) are studied against threadless Ring0 PoCs such as [[zero-thread-kernel]]. (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md) (source: wiki/sources/descriptions/zorftw__revert-mapper.md) (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md) (source: wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md)


**Architecture:** user-mode scanners → kernel callbacks/VAD → optional hypervisor EPT protection → server-side replay/stats.

**Threats defended against:** injected code (stress/test harnesses such as [[injectors]] under Injection Testing), [[byovd]], hypervisor abuse (stress/test refs such as [[vt-debuuger]]; minimal VT-x Type-2 learning stacks such as [[hv]]; stealth Type-2 stacks such as [[ophion]] with CPUID cache / CR4.VMXE hide / TSC compensation under hacked-hypervisor detection), hidden/anti-detect PVE/QEMU guests (e.g. [[proxmox-ve-anti-detection]], [[qemu-anti-detection]] under virtual-environment detection), [[dma]] (PCIe fingerprinting + IOMMU + TPM attestation), AI visual cheats with hardware input. (source: wiki/sources/descriptions/zoand__Injectors.md) (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md) (source: wiki/sources/descriptions/zer0condition__hv.md) (source: wiki/sources/descriptions/zer0condition__Ophion.md) (source: wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md) (source: wiki/sources/descriptions/zhaodice__qemu-anti-detection.md)

**Platform trust:** DSE, [[patchguard]], [[hvci]]/VBS, Secure Boot.

**Obfuscation tooling:** [[shredder-rs]] — x86_64 polymorphic instruction shredding (context-preserving) for AC/obfuscation-engine research. (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md) Engine-side data hiding: [[static-variables-obfuscator-ue4]] obfuscates UE4 static variables against Cheat Engine–style scans (`Game Engine Protection:Unreal`). (source: wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md)


## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[dma]] · [[iommu]] · [[present-hook]] · [[vac3-inhibitor]] · [[hv]] · [[ophion]] · [[vt-debuuger]] · [[proxmox-ve-anti-detection]] · [[qemu-anti-detection]] · [[shredder-rs]] · [[static-variables-obfuscator-ue4]] · [[blindeye]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[etw-explorer]] · [[injectors]] · [[zero-thread-kernel]]


## README map

`Anti Cheat` (~589 links): guides, stress/unit-test harnesses, packers, engine protection (Unreal/Unity/Source), and a wide `Detection:*` tree (hook, memory integrity, shellcode, attach, aimbot, hide, vulnerable driver, hacked hypervisor, virtual environments, HWID, speedhack, injection, stack spoof, ESP, DMA, wallhack, obfuscation, Android root). Cross-links `Windows Security Features` and Cheat PatchGuard/DSE lanes. (source: wiki/sources/README-categories.md)
