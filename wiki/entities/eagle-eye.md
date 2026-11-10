---
title: Eagle Eye
kind: entity
topics: [anti-cheat, dma-attack, windows-kernel]
sources:
  - wiki/sources/descriptions/zzjjmkk__eagle-eye.md
updated: 2026-11-10
confidence: medium
---

# Eagle Eye

**Eagle Eye** (zzjjmkk/eagle-eye) is a **read-only Windows x64 CLI** that scans a suspect machine for **local cheat-tool traces** and emits **scored, evidence-backed JSON/HTML reports** without hooking, touching game memory, or using the network. (source: wiki/sources/descriptions/zzjjmkk__eagle-eye.md)

Primary implementation is **C# on .NET 8** as a self-contained executable, with **PowerShell** helpers for packaging and rule maintenance. An optional **WDK C driver** performs **read-only PCIe configuration-space** reads during DMA-related checks.

## Scan surface

| Area | Role |
|------|------|
| Processes & handles | Live process inventory, cross-process handle relationships |
| Kernel & injection | Loaded drivers, injection artifacts |
| Overlays & ML | Transparent overlay windows, vision/inference-related modules |
| DMA & files | DMA-capable hardware signals, file hashes and signatures |
| Telemetry (optional) | Offline game telemetry when configured |

All checks are driven by **external JSON rules** with schema validation and **tunable risk aggregation**—human reviewers interpret aggregate scores rather than receiving automatic bans.

## Trust model

Conservative **on-machine triage** for game-security operators, tournament admins, and investigators when the PC is physically available. The tool **explicitly marks unobservable local gaps** instead of declaring a machine clean—aligned with [[detector-operations]] evidence discipline.

## Related tooling

Comparable read-only screenshare / integrity scanners include [[dexcheck]], [[irontrace]], [[aeterna-rongroi]], [[custos]], and [[cheatguard]]; consent-gated Minecraft workflows such as [[hapiscanner]] add server-session cryptography on top of similar artifact hunting.

## Links

- Repo: https://github.com/zzjjmkk/eagle-eye

## Related

[[overviews/anti-cheat]] · [[overviews/dma-attack]] · [[detector-operations]] · [[dexcheck]] · [[irontrace]] · [[cheatguard]]
