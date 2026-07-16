# Wiki Index

Compiled knowledge catalog for awesome-game-security.

> Maintained via `scripts/update-wiki-cli.py`. See [[AGENTS]] for schema.

## Overviews

- [Overview](overviews/overview.md) — project map, skill routing, README categories
- [Anti-Cheat](overviews/anti-cheat.md) — layered AC architecture and detection
- [DMA Attack](overviews/dma-attack.md) — PCIe DMA threat model and defenses
- [Game Engine](overviews/game-engine.md) — Unreal / Unity / Source / Godot surfaces
- [Game Hacking](overviews/game-hacking.md) — offensive escalation taxonomy
- [Graphics API](overviews/graphics-api.md) — Present hooks, overlays, capture
- [Mobile Security](overviews/mobile-security.md) — Android / iOS game security
- [Reverse Engineering](overviews/reverse-engineering.md) — RE tools, DBI, deobfuscation
- [Windows Kernel](overviews/windows-kernel.md) — callbacks, HVCI, BYOVD, pool

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

- [BlindEye](entities/blindeye.md) — BattlEye report-path pool-alloc drop (“Packet Fucker”)
- [PG1903](entities/pg1903.md) — Win10 1903 PatchGuard disable via context-page NX (Demo NX)
- [shredder-rs](entities/shredder-rs.md) — x86_64 polymorphic instruction shredding (Rust)
- [vac3_inhibitor](entities/vac3-inhibitor.md) — VAC3 exploration via hooking / memory analysis (C++)
- [vt-debuuger](entities/vt-debuuger.md) — hacked hypervisor testing (C/C++ drivers / plugins)

## Sources

- Projected category map: `sources/README-categories.md` (generated on scan)
- Skill projections: `sources/skills/`
- Description projections: `sources/descriptions/` (incremental only)
