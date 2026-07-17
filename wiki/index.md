# Wiki Index

Compiled knowledge catalog for awesome-game-security.

> Maintained via `scripts/update-wiki-cli.py`. See [[AGENTS]] for schema.

## Overviews

- [Overview](overviews/overview.md) — project map; 40 README sections → skill topics (Cheat ~2543 / Anti Cheat ~592)
- [Anti-Cheat](overviews/anti-cheat.md) — layered AC; Detection:* + engine protection (~592)
- [DMA Attack](overviews/dma-attack.md) — PCIe DMA threat model and defenses
- [Game Engine](overviews/game-engine.md) — Unreal / Unity / Source / Godot / Lumix (~136); assets, hot-patch, MCP/AI gamedev
- [Game Hacking](overviews/game-hacking.md) — Cheat taxonomy (~2543) + Some Tricks (~112)
- [Graphics API](overviews/graphics-api.md) — DirectX/GL/Vulkan hooks, overlays, capture
- [Mobile Security](overviews/mobile-security.md) — Android / iOS; WSA, emulators, Cellular/SIM
- [Reverse Engineering](overviews/reverse-engineering.md) — RE tools, DBI, deobfuscation
- [Windows Kernel](overviews/windows-kernel.md) — callbacks, HVCI/CET/TPM attestation, BYOVD, pool

## Concepts

- [BattlEye](concepts/battleye.md)
- [BYOVD](concepts/byovd.md)
- [DMA](concepts/dma.md)
- [Easy Anti-Cheat](concepts/easy-anti-cheat.md)
- [Frida](concepts/frida.md)
- [HVCI](concepts/hvci.md)
- [IL2CPP](concepts/il2cpp.md)
- [IOMMU](concepts/iommu.md)
- [Kernel Callbacks](concepts/kernel-callbacks.md)
- [PatchGuard](concepts/patchguard.md)
- [Present Hook](concepts/present-hook.md)
- [Vanguard](concepts/vanguard.md)

## Entities

- [android-proxy-mcp](entities/android-proxy-mcp.md) — Android HTTP/HTTPS capture MCP (mitmdump + SQLite + NL query)
- [apktool-mcp-server](entities/apktool-mcp-server.md) — MCP server wrapping apktool (Android RE suite)
- [BlindEye](entities/blindeye.md) — BattlEye report-path pool-alloc drop (“Packet Fucker”)
- [BOOM](entities/boom.md) — hijack Beep.sys; stealth driver communication
- [BusterCall](entities/bustercall.md) — enumerate/patch kernel callbacks; HVCI PFN-swap research
- [checkhv_um](entities/checkhv-um.md) — user-mode HV detection (CPUID / RDTSC / VMCS / signatures)
- [cheese](entities/cheese.md) — Quest 3/3S root via Adreno CVE-2025-21479 (Magisk, no boot rewrite)
- [DayZzz](entities/dayzzz.md) — DayZ cheat/modding: SDK generation + overlays (C/C++)
- [Demystifying-PatchGuard](entities/demystifying-patchguard.md) — educational C/C++ walkthrough of PatchGuard
- [deobf](entities/deobf.md) — libtprt.so OLLVM deobf / plugin hooks (Python)

- [EtwExplorer](entities/etw-explorer.md) — GUI browse of ETW providers / event manifests
- [Fortnite-Fltokens-and-offsets](entities/fortnite-fltokens-and-offsets.md) — Fortnite FLToken/offset grabber (stale / offline)
- [hv](entities/hv.md) — minimal Intel VT-x Type-2 hypervisor (VMX/VMCS learning)
- [ida-jm-xorstr-decrypt-plugin](entities/ida-jm-xorstr-decrypt-plugin.md) — IDA Pro JM Xorstr decrypt (x64; Python)
- [IDADeflat](entities/idadeflat.md) — IDA Pro CFF deflatten (angr; OLLVM-style)
- [Il2cppSpy](entities/il2cpp-spy.md) — Unity IL2CPP APK disassembler / two-APK diff
- [Injectors](entities/injectors.md) — injection-testing harness (C/C++; AC stress)
- [lightsaber](entities/lightsaber.md) — iOS 18.4–18.6.2 userland exploit; JS inject SpringBoard (DarkSword-derived)
- [lsass-extend-mapper](entities/lsass-extend-mapper.md) — unsigned driver map via lsass address-space extend
- [mutaben](entities/mutaben.md) — Python MBA (mixed-boolean-arithmetic) expression generator
- [NTMemory](entities/ntmemory.md) — kernel cross-process R/W (MDL / CR3 walk / physical translate)
- [OpenArk](entities/openark.md) — Qt anti-rootkit / kernel analysis (callbacks, SSDT, drivers)
- [Ophion](entities/ophion.md) — stealth Intel VT-x Type-2 HV (EPT; CPUID/CR4/TSC anti-detect)
- [PG1903](entities/pg1903.md) — Win10 1903 PatchGuard disable via context-page NX (Demo NX)
- [proxmox-ve-anti-detection](entities/proxmox-ve-anti-detection.md) — Hidden PVE / QEMU-KVM anti-detection (kernel)
- [qemu-anti-detection](entities/qemu-anti-detection.md) — Hidden QEMU (device-string / fingerprint spoof)
- [QuickAsm](entities/quickasm.md) — x86/x64 assemble-and-run GUI (Keystone)
- [revert-mapper](entities/revert-mapper.md) — post-execution cleanup for manually mapped kernel drivers
- [shredder-rs](entities/shredder-rs.md) — x86_64 polymorphic instruction shredding (Rust)
- [Static-Variables-Obfuscator-UE4](entities/static-variables-obfuscator-ue4.md) — UE4 static-variable obfuscation vs memory scanners
- [TotalPE2](entities/totalpe2.md) — WPF PE viewer (headers, imports/exports, .NET metadata)
- [UniCli](entities/unicli.md) — Unity Editor terminal CLI (compile/test/build/inspect; AI-agent ready)
- [unflutter](entities/unflutter.md) — Flutter/Dart AOT snapshot static analyzer (symbol recovery)
- [vac3_inhibitor](entities/vac3-inhibitor.md) — VAC3 exploration via hooking / memory analysis (C++)
- [vt-debuuger](entities/vt-debuuger.md) — hacked hypervisor testing (C/C++ drivers / plugins)
- [x670e-tomahawk-anticheat-update](entities/x670e-tomahawk-anticheat-update.md) — MSI X670E Tomahawk BIOS v1KB DXE anti-cheat (option-ROM strip / NX)
- [XrefsExt](entities/xrefsext.md) — IDA Pro extended-xrefs plugin (cheat / IDA Plugins)
- [ZeroThreadKernel](entities/zero-thread-kernel.md) — threadless kernel exec via existing contexts / timers (vs AC thread enum)





## Sources

- Projected category map: `sources/README-categories.md` (generated on scan; 40 top-level sections)
- Skill projections: `sources/skills/`
- Description projections: `sources/descriptions/` (incremental only)
