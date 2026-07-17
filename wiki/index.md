# Wiki Index

Compiled knowledge catalog for awesome-game-security.

> Maintained via `scripts/update-wiki-cli.py`. See [[AGENTS]] for schema.

## Overviews

- [Overview](overviews/overview.md) — project map; 40 README sections → skill topics (Cheat ~2543 / Anti Cheat ~592; Game Network ~25)
- [Anti-Cheat](overviews/anti-cheat.md) — layered AC; Detection:* + engine protection (~592)
- [DMA Attack](overviews/dma-attack.md) — PCIe DMA via Cheat/Detection:DMA + WSF attestation
- [Game Engine](overviews/game-engine.md) — Unreal / Unity / Source / Godot / Lumix (~136); assets, hot-patch, MCP/AI gamedev (~176)
- [Game Hacking](overviews/game-hacking.md) — Cheat taxonomy (~2543) + Some Tricks (~112)
- [Graphics API](overviews/graphics-api.md) — DirectX (~32) / GL / Vulkan hooks, overlays, capture
- [Mobile Security](overviews/mobile-security.md) — Android / iOS; WSA (~9), emulators (~9/~3), Cellular/SIM
- [Reverse Engineering](overviews/reverse-engineering.md) — RE tools, MBA/DBI, deobfuscation, packers
- [Windows Kernel](overviews/windows-kernel.md) — callbacks, HVCI/CET/TPM attestation (~9), BYOVD, pool

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

- [BattleField-1-Internal](entities/battlefield-1-internal.md) — BF1 internal: DirectX / SDK generation / hooking (C++)
- [android-proxy-mcp](entities/android-proxy-mcp.md) — Android HTTP/HTTPS capture MCP (mitmdump + SQLite + NL query)
- [apktool-mcp-server](entities/apktool-mcp-server.md) — MCP server wrapping apktool (Android RE suite)
- [awesome-educational-games](entities/awesome-educational-games.md) — curated educational games (editors / languages / programming; Game Develop Guide)
- [BlindEye](entities/blindeye.md) — BattlEye report-path pool-alloc drop (“Packet Fucker”)
- [BOOM](entities/boom.md) — hijack Beep.sys; stealth driver communication
- [BusterCall](entities/bustercall.md) — enumerate/patch kernel callbacks; HVCI PFN-swap research
- [checkhv_um](entities/checkhv-um.md) — user-mode HV detection (CPUID / RDTSC / VMCS / signatures)
- [cheese](entities/cheese.md) — Quest 3/3S root via Adreno CVE-2025-21479 (Magisk, no boot rewrite)
- [CounterStrike2-Linux-Cheat](entities/counterstrike2-linux-cheat.md) — Linux external CS2 cheat (C++; memory analysis)
- [CounterStrikeSource-Linux-Trainer](entities/counterstrikesource-linux-trainer.md) — Linux external CS:S trainer (movement / info display)
- [DayZzz](entities/dayzzz.md) — DayZ cheat/modding: SDK generation + overlays (C/C++)
- [Demystifying-PatchGuard](entities/demystifying-patchguard.md) — educational C/C++ walkthrough of PatchGuard
- [deobf](entities/deobf.md) — libtprt.so OLLVM deobf / plugin hooks (Python)

- [EtwExplorer](entities/etw-explorer.md) — GUI browse of ETW providers / event manifests
- [Fortnite-Fltokens-and-offsets](entities/fortnite-fltokens-and-offsets.md) — Fortnite FLToken/offset grabber (stale / offline)
- [hv](entities/hv.md) — minimal Intel VT-x Type-2 hypervisor (VMX/VMCS learning)
- [ida-ios-helper](entities/ida-ios-helper.md) — IDA plugin for iOS reversing (vtable symbols required)
- [ida-jm-xorstr-decrypt-plugin](entities/ida-jm-xorstr-decrypt-plugin.md) — IDA Pro JM Xorstr decrypt (x64; Python)

- [IDADeflat](entities/idadeflat.md) — IDA Pro CFF deflatten (angr; OLLVM-style)
- [Il2cppSpy](entities/il2cpp-spy.md) — Unity IL2CPP APK disassembler / two-APK diff
- [Injectors](entities/injectors.md) — injection-testing harness (C/C++; AC stress)
- [Kagura](entities/kagura.md) — LLVM pass plugin: CFG/string obfuscation, anti-tamper, anti-debug (mobile/desktop/Wasm)
- [lightsaber](entities/lightsaber.md) — iOS 18.4–18.6.2 userland exploit; JS inject SpringBoard (DarkSword-derived)
- [lsass-extend-mapper](entities/lsass-extend-mapper.md) — unsigned driver map via lsass address-space extend
- [mutaben](entities/mutaben.md) — Python MBA (mixed-boolean-arithmetic) expression generator
- [MoveCertificate](entities/move-certificate.md) — Magisk/KernelSU/APatch user→system CA module (Android 7–15)
- [NTMemory](entities/ntmemory.md) — kernel cross-process R/W (MDL / CR3 walk / physical translate)
- [OFRP-device_xiaomi_mondrian](entities/ofrp-device-xiaomi-mondrian.md) — OFRP/TWRP device tree for Redmi K60 Pro (mondrian)
- [OpenArk](entities/openark.md) — Qt anti-rootkit / kernel analysis (callbacks, SSDT, drivers)
- [Ophion](entities/ophion.md) — stealth Intel VT-x Type-2 HV (EPT; CPUID/CR4/TSC anti-detect)
- [pe32-password](entities/pe32-password.md) — PE32 password binary packer (Anti Cheat → Binary Packer)
- [PG1903](entities/pg1903.md) — Win10 1903 PatchGuard disable via context-page NX (Demo NX)
- [proxmox-ve-anti-detection](entities/proxmox-ve-anti-detection.md) — Hidden PVE / QEMU-KVM anti-detection (kernel)
- [qemu-anti-detection](entities/qemu-anti-detection.md) — Hidden QEMU (device-string / fingerprint spoof)
- [QuickAsm](entities/quickasm.md) — x86/x64 assemble-and-run GUI (Keystone)
- [revert-mapper](entities/revert-mapper.md) — post-execution cleanup for manually mapped kernel drivers
- [shredder-rs](entities/shredder-rs.md) — x86_64 polymorphic instruction shredding (Rust)
- [Static-Variables-Obfuscator-UE4](entities/static-variables-obfuscator-ue4.md) — UE4 static-variable obfuscation vs memory scanners
- [TotalPE2](entities/totalpe2.md) — WPF PE viewer (headers, imports/exports, .NET metadata)
- [tiny-csgo-client](entities/tiny-csgo-client.md) — minimal CS:GO client for dedicated servers (modding / SDK)
- [ts-ue4dumper](entities/ts-ue4dumper.md) — TypeScript + Frida UE4 dumper (modular; C++ offsets)
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
