# Wiki Index

Compiled knowledge catalog for awesome-game-security.

> Maintained via `scripts/update-wiki-cli.py`. See [[AGENTS]] for schema.

## Overviews

- [Overview](overviews/overview.md) — project map; ~40 README sections → skill topics
- [Anti-Cheat](overviews/anti-cheat.md) — layered AC; Detection:* + engine protection map
- [DMA Attack](overviews/dma-attack.md) — PCIe DMA threat model and defenses
- [Game Engine](overviews/game-engine.md) — Unreal / Unity / Source / Godot; assets & hot-patch
- [Game Hacking](overviews/game-hacking.md) — Cheat taxonomy (~2540 links) + Some Tricks
- [Graphics API](overviews/graphics-api.md) — DirectX/GL/Vulkan hooks, overlays, capture
- [Mobile Security](overviews/mobile-security.md) — Android / iOS; WSA & emulators
- [Reverse Engineering](overviews/reverse-engineering.md) — RE tools, DBI, deobfuscation
- [Windows Kernel](overviews/windows-kernel.md) — callbacks, HVCI/CET, BYOVD, pool

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

- [apktool-mcp-server](entities/apktool-mcp-server.md) — MCP server wrapping apktool (Android RE suite)
- [BlindEye](entities/blindeye.md) — BattlEye report-path pool-alloc drop (“Packet Fucker”)
- [BOOM](entities/boom.md) — hijack Beep.sys; stealth driver communication
- [deobf](entities/deobf.md) — libtprt.so OLLVM deobf / plugin hooks (Python)
- [EtwExplorer](entities/etw-explorer.md) — GUI browse of ETW providers / event manifests
- [Fortnite-Fltokens-and-offsets](entities/fortnite-fltokens-and-offsets.md) — Fortnite FLToken/offset grabber (stale / offline)
- [Injectors](entities/injectors.md) — injection-testing harness (C/C++; AC stress)
- [lsass-extend-mapper](entities/lsass-extend-mapper.md) — unsigned driver map via lsass address-space extend
- [PG1903](entities/pg1903.md) — Win10 1903 PatchGuard disable via context-page NX (Demo NX)
- [QuickAsm](entities/quickasm.md) — x86/x64 assemble-and-run GUI (Keystone)
- [revert-mapper](entities/revert-mapper.md) — post-execution cleanup for manually mapped kernel drivers
- [shredder-rs](entities/shredder-rs.md) — x86_64 polymorphic instruction shredding (Rust)
- [Static-Variables-Obfuscator-UE4](entities/static-variables-obfuscator-ue4.md) — UE4 static-variable obfuscation vs memory scanners
- [TotalPE2](entities/totalpe2.md) — WPF PE viewer (headers, imports/exports, .NET metadata)
- [vac3_inhibitor](entities/vac3-inhibitor.md) — VAC3 exploration via hooking / memory analysis (C++)
- [vt-debuuger](entities/vt-debuuger.md) — hacked hypervisor testing (C/C++ drivers / plugins)



## Sources

- Projected category map: `sources/README-categories.md` (generated on scan; 40 top-level sections)
- Skill projections: `sources/skills/`
- Description projections: `sources/descriptions/` (incremental only)
