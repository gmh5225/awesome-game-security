---
title: Anti-Cheat
kind: overview
topics: [anti-cheat]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/README-categories.md
  - wiki/sources/descriptions/zyhp__vac3_inhibitor.md
  - wiki/sources/descriptions/x1tan__vac3-dumper.md
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
  - wiki/sources/descriptions/zer0condition__checkhv_um.md
  - wiki/sources/descriptions/ytk2128__pe32-password.md
  - wiki/sources/descriptions/ykus4__kagura.md
  - wiki/sources/descriptions/yardenshafir__cet-research.md
  - wiki/sources/descriptions/xxFURYWOLFxx__veh-dumper.md
  - wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md
  - wiki/sources/descriptions/xsj3n__x64-EXE-Packer.md
  - wiki/sources/descriptions/xM0kht4r__2Pack.md
  - wiki/sources/descriptions/xiaoweime__WProtect.md
  - wiki/sources/descriptions/xan105__Mini-Launcher.md
  - wiki/sources/descriptions/xakepru__x14.08-coverstory-blizzard.md
  - wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md
  - wiki/sources/descriptions/x86byte__sbox.md
  - wiki/sources/descriptions/x86byte__Obfusk8.md
  - wiki/sources/descriptions/wpdk__wdutf.md
  - wiki/sources/descriptions/wietze__windows-dll-hijacking.md
  - wiki/sources/descriptions/wietze__HijackLibs.md
  - wiki/sources/descriptions/whokilleddb__function-collections.md
  - wiki/sources/descriptions/whereisr0da__Lumina-Cheat.md
  - wiki/sources/descriptions/wesmar__FileRecoveryTool.md
  - wiki/sources/descriptions/weak1337__ricochet_deobfuscator.md
  - wiki/sources/descriptions/weak1337__NvidiaApi.md
  - wiki/sources/descriptions/weak1337__NO_ACCESS_Protection.md
  - wiki/sources/descriptions/weak1337__ModExMap.md
  - wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md
  - wiki/sources/descriptions/weak1337__CEDetector.md
  - wiki/sources/descriptions/weak1337__BE-Shellcode.md
  - wiki/sources/descriptions/weak1337__Alcatraz.md
  - wiki/sources/descriptions/wbenny__scfw.md
  - wiki/sources/descriptions/wbenny__injdrv.md
  - wiki/sources/descriptions/wbenny__DetoursNT.md
  - wiki/sources/descriptions/wazuh__wazuh.md
  - wiki/sources/descriptions/waryas__xign_poc_april_2026.md
  - wiki/sources/descriptions/waryas__WaryasSWHE.md
updated: 2026-07-18
confidence: high
---




# Anti-Cheat

Layered game protection across kernel drivers, privileged services, in-game modules, and backend telemetry. Modern systems monitor handles, image loads, memory integrity, driver trust, virtualization abuse, DMA, and suspicious input. (source: wiki/sources/skills/anti-cheat.md)

## Major systems

- [[easy-anti-cheat]] — service + driver + game-facing integrity (Fortnite, Apex, Rust)
- [[battleye]] — handle protection, process/memory scanning (PUBG, R6, DayZ); research ref [[blindeye]] drops BE report-path pool allocs via hooked `ExAllocatePool*` (source: wiki/sources/descriptions/zouxianyu__BlindEye.md); user-mode shellcode RE via [[be-shellcode]] (dump/disasm thread scan, VEH enum, module integrity) (source: wiki/sources/descriptions/weak1337__BE-Shellcode.md)
- [[vanguard]] — boot-start driver, early driver allowlisting (Valorant, LoL)
- FACEIT AC, VAC (user-mode signatures), GameGuard, XIGNCODE3 (vuln PoC [[xign-poc-april-2026]] on `xhunter64.sys` `IRP_MJ_WRITE` → phys R/W / kernel leak / process kill) (source: wiki/sources/descriptions/waryas__xign_poc_april_2026.md), ACE, Warden (Blizzard / WoW)
- [[vac3-inhibitor]] — C++ VAC3 exploration (hooking / memory analysis) under cheat → explore anticheat:vac (source: wiki/sources/descriptions/zyhp__vac3_inhibitor.md)
- [[vac3-dumper]] — dumps VAC3 modules loaded at different times for offline RE (Dump lane) (source: wiki/sources/descriptions/x1tan__vac3-dumper.md)
- [[ricochet-deobfuscator]] — C/C++ Ricochet deobfuscator (driver / memory analysis; explore anticheat:ricochet) (source: wiki/sources/descriptions/weak1337__ricochet_deobfuscator.md)
- [[x14-08-coverstory-blizzard]] — WoW cheat framework with Warden loader hooks / RunScript injection (research ref for Warden internals) (source: wiki/sources/descriptions/xakepru__x14.08-coverstory-blizzard.md)



## Key sub-areas

**Detection:** memory hashing / manual-map detection; process handle stripping; [[kernel-callbacks]]; Segment Heap–aware pool scanning; behavioral/ML aimbot signals; screenshot + heartbeat; ETW provider/event discovery for telemetry design (e.g. [[etw-explorer]]); ThreatIntel injection consumers such as [[tietwagent]] (Microsoft-Windows-Threat-Intelligence + krabsetw/Yara; ELAM/PPL service path). Ring3 Instrumentation Callback research such as [[instrumentation-callback-syscall-logger]] inspects each syscall on kernel return before user-mode resumes. Unconventional Ring3 PoC collections such as [[function-collections]] (C; asset pipelines / memory analysis) support the same anti-cheat / Windows Ring3 callback research lane. (source: wiki/sources/descriptions/whokilleddb__function-collections.md) Trusted-process mapping (e.g. [[lsass-extend-mapper]] hosting unsigned drivers via lsass address-space extend) and post-execution map cleanup (e.g. [[revert-mapper]] freeing mapped driver memory and pool-tag traces) are common research counterparts to those scanners. Thread-enumeration detectors (looking for manual-map worker threads) are studied against threadless Ring0 PoCs such as [[zero-thread-kernel]]. HWID / GPU serial fingerprinting (undocumented NvAPI) is illustrated by [[nvidiaapi]]; TPM EK spoofing via hooked `DeviceIoControl` / TPM device-stack filters is detected by [[detect-tpm-spoofing]] (IOCTL `TPM2_ReadPublic` vs `TPM.sys` cached buffers). Cheat Engine presence (window classes / process names / driver / debug artifacts, incl. renamed or anti-detect CE) is illustrated by [[cedetector]]. Enterprise host XDR / HIDS platforms such as [[wazuh]] (agent–manager IDS, FIM, log correlation; Elasticsearch viz) sit adjacent to AC/EDR telemetry design under the README `[XDR]` lane. (source: wiki/sources/descriptions/zorftw__lsass-extend-mapper.md) (source: wiki/sources/descriptions/zorftw__revert-mapper.md) (source: wiki/sources/descriptions/zodiacon__EtwExplorer.md) (source: wiki/sources/descriptions/xuanxuan0__TiEtwAgent.md) (source: wiki/sources/descriptions/zer0condition__ZeroThreadKernel.md) (source: wiki/sources/descriptions/x86matthew__InstrumentationCallbackSyscallLogger.md) (source: wiki/sources/descriptions/weak1337__NvidiaApi.md) (source: wiki/sources/descriptions/weak1337__DetectTpmSpoofing.md) (source: wiki/sources/descriptions/weak1337__CEDetector.md) (source: wiki/sources/descriptions/wazuh__wazuh.md)


**Architecture:** user-mode scanners → kernel callbacks/VAD → optional hypervisor EPT protection → server-side replay/stats. Driver-side AC engineering can use user-space unit-test harnesses such as [[wdutf]] (Microsoft C++ unit tests against kernel-driver code). (source: wiki/sources/descriptions/wpdk__wdutf.md)

**Threats defended against:** usermode AC bypass via shatter-attack PoCs such as [[waryasswhe]] (0day shatter → any-AC claim; cheat / RPM research lane) (source: wiki/sources/descriptions/waryas__WaryasSWHE.md); injected code (stress/test harnesses such as [[injectors]] under Injection Testing; user-mode PE manual-map samples such as [[modexmap]] — VirtualAllocEx/WPM + import/reloc/TLS + CreateRemoteThread entry stub) (source: wiki/sources/descriptions/weak1337__ModExMap.md); kernel APC DLL injectors such as [[injdrv]] (process-create notify → user APC → `LdrLoadDll`; bypasses many UM inject hooks) (source: wiki/sources/descriptions/wbenny__injdrv.md); NTDLL-only Detours ports such as [[detoursnt]] (unmodified Detours; no Win32 deps; hook/trampoline research) (source: wiki/sources/descriptions/wbenny__DetoursNT.md); Windows shellcode build frameworks such as [[scfw]] (cross-platform C++; shellcode engine & tricks lane) (source: wiki/sources/descriptions/wbenny__scfw.md); DLL search-order / sideload / phantom-DLL catalogs such as [[windows-dll-hijacking]] and disclosed-opportunity DBs such as [[hijacklibs]] for image-load attack-surface mapping (source: wiki/sources/descriptions/wietze__windows-dll-hijacking.md) (source: wiki/sources/descriptions/wietze__HijackLibs.md); platform-bypass launchers such as [[mini-launcher]] (Steam API stubs / SteamAppID + DLL/Lua inject without the full client) (source: wiki/sources/descriptions/xan105__Mini-Launcher.md); [[byovd]], hypervisor abuse (stress/test refs such as [[vt-debuuger]]; minimal VT-x Type-2 learning stacks such as [[hv]]; stealth Type-2 stacks such as [[ophion]] with CPUID cache / CR4.VMXE hide / TSC compensation under hacked-hypervisor detection; user-mode detection probes such as [[checkhv-um]] via CPUID / RDTSC / VMCS artifacts / signature match), hidden/anti-detect PVE/QEMU guests (e.g. [[proxmox-ve-anti-detection]], [[qemu-anti-detection]] under virtual-environment detection), [[dma]] (PCIe fingerprinting + IOMMU + TPM attestation), AI visual cheats with hardware input. (source: wiki/sources/descriptions/zoand__Injectors.md) (source: wiki/sources/descriptions/zxd1994__vt-debuuger.md) (source: wiki/sources/descriptions/zer0condition__hv.md) (source: wiki/sources/descriptions/zer0condition__Ophion.md) (source: wiki/sources/descriptions/zer0condition__checkhv_um.md) (source: wiki/sources/descriptions/zhaodice__proxmox-ve-anti-detection.md) (source: wiki/sources/descriptions/zhaodice__qemu-anti-detection.md)

**Platform trust:** DSE, [[patchguard]], [[hvci]]/VBS, Secure Boot; CET/shadow-stack research such as [[cet-research]] in the Windows Security Features lane. (source: wiki/sources/descriptions/yardenshafir__cet-research.md)

**Obfuscation tooling:** [[shredder-rs]] — x86_64 polymorphic instruction shredding (context-preserving) for AC/obfuscation-engine research. (source: wiki/sources/descriptions/zx0CF1__shredder-rs.md) Cheat-side signature mutation: [[lumina-cheat]] — internal CS:GO sample that mutates to keep a changing signature (VAC-facing research lane). (source: wiki/sources/descriptions/whereisr0da__Lumina-Cheat.md) Engine-side data hiding: [[static-variables-obfuscator-ue4]] obfuscates UE4 static variables against Cheat Engine–style scans (`Game Engine Protection:Unreal`). (source: wiki/sources/descriptions/zompi2__Static-Variables-Obfuscator-UE4.md) Binary Packer lane: [[pe32-password]] — C/C++ PE32 password packing for packed/modded client study. (source: wiki/sources/descriptions/ytk2128__pe32-password.md); [[x64-exe-packer]] — PE X64 packing. (source: wiki/sources/descriptions/xsj3n__x64-EXE-Packer.md); [[2pack]] — Rust PE & shellcode packing (EXE/DLL + raw shellcode). (source: wiki/sources/descriptions/xM0kht4r__2Pack.md) LLVM pass-plugin obfuscation/anti-tamper: [[kagura]] (CFG/string/data passes + anti-debug runtime; NDK/iOS/Unity/Unreal). (source: wiki/sources/descriptions/ykus4__kagura.md) Obfuscation Engine lane: [[wprotect]] — C/C++ WProtect research reference. (source: wiki/sources/descriptions/xiaoweime__WProtect.md) Post-compile x64 PE obfuscator: [[alcatraz]] — ImGui GUI; mutation / CFF / anti-disasm junk / IAT obfuscation (Zydis + AsmJit). (source: wiki/sources/descriptions/weak1337__Alcatraz.md) Compile-time / runtime C++17 library: [[obfusk8]] — logic/data obfuscation for AC compile-time research. (source: wiki/sources/descriptions/x86byte__Obfusk8.md) Compile-time string encryption: [[sbox]] — C++ constexpr AES-128 / S-box macros (Obfusk8 spin-off; binary-safe). (source: wiki/sources/descriptions/x86byte__sbox.md)

**VEH-based protection RE:** [[veh-dumper]] surgically dumps VectoredException/Continue handlers as IDA-ready PE64 modules for studying VEH-backed AC / anti-tamper logic. (source: wiki/sources/descriptions/xxFURYWOLFxx__veh-dumper.md) PAGE_NOACCESS + VEH trampoline / single-step re-protect sample: [[no-access-protection]] (external scanners AV; legitimate exec resumes via VEH). (source: wiki/sources/descriptions/weak1337__NO_ACCESS_Protection.md)

**Disk / file forensics:** recover deleted on-disk artifacts (payloads, logs, dumps) via tools such as [[file-recovery-tool]] (NTFS/FAT32/ExFAT MFT/USN + carving; Information System & Forensics lane). (source: wiki/sources/descriptions/wesmar__FileRecoveryTool.md)



## Related concepts

[[kernel-callbacks]] · [[byovd]] · [[hvci]] · [[cet-research]] · [[dma]] · [[iommu]] · [[present-hook]] · [[vac3-inhibitor]] · [[vac3-dumper]] · [[ricochet-deobfuscator]] · [[x14-08-coverstory-blizzard]] · [[xign-poc-april-2026]] · [[waryasswhe]] · [[veh-dumper]] · [[no-access-protection]] · [[file-recovery-tool]] · [[hv]] · [[ophion]] · [[checkhv-um]] · [[vt-debuuger]] · [[proxmox-ve-anti-detection]] · [[qemu-anti-detection]] · [[shredder-rs]] · [[lumina-cheat]] · [[static-variables-obfuscator-ue4]] · [[pe32-password]] · [[x64-exe-packer]] · [[2pack]] · [[kagura]] · [[wprotect]] · [[alcatraz]] · [[obfusk8]] · [[sbox]] · [[blindeye]] · [[be-shellcode]] · [[scfw]] · [[injdrv]] · [[detoursnt]] · [[lsass-extend-mapper]] · [[revert-mapper]] · [[etw-explorer]] · [[tietwagent]] · [[wazuh]] · [[instrumentation-callback-syscall-logger]] · [[function-collections]] · [[injectors]] · [[modexmap]] · [[windows-dll-hijacking]] · [[hijacklibs]] · [[mini-launcher]] · [[zero-thread-kernel]] · [[wdutf]] · [[nvidiaapi]] · [[detect-tpm-spoofing]] · [[cedetector]]




## README map

`Anti Cheat` (~595 links): guides, stress/unit-test harnesses, packers, obfuscation engines, open-source / analysis-framework AC samples (incl. hybrid CS2-style proposals with judge ratings, honeypot entities, and shadow monitoring), engine protection (Unreal/Unity/Source), and a wide `Detection:*` tree (hook, memory integrity, shellcode, attach, aimbot, hide, vulnerable driver, hacked hypervisor, virtual environments, HWID, speedhack, injection, stack spoof, ESP, DMA, wallhack, obfuscation, Android root). Cross-links `Windows Security Features` (~9; CET/TPM/IOMMU/HVCI attestation), Cheat (~2552) PatchGuard/DSE + Launcher Abuser lanes, adjacent `Game Tools` (~8; RCE hardening for PC gamers), and `Windows Emulator` (~7; WHP trap-driven guests + hybrid kernel-driver stacks for AC analysis). (source: wiki/sources/README-categories.md)
