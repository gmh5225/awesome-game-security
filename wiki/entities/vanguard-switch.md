---
title: VanguardSwitch
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/shinishiz__VanguardSwitch.md
  - wiki/sources/README-categories.md
updated: 2026-11-01
confidence: high
---

# VanguardSwitch

**VanguardSwitch** (shinishiz; C# .NET Framework 4.8 WinForms; Explore AntiCheat System:Vanguard) is a Windows **desktop utility** for **Windows 10/11** players and researchers who cannot use Riot's official **Vanguard On-Demand** mode. It turns Vanguard off while idle and restores it before play **without a full reboot**. (source: wiki/sources/descriptions/shinishiz__VanguardSwitch.md)

## Components toggled

The tool stops and blocks the **`vgc`** user-mode service, optionally keeps the **`vgk`** kernel driver loaded, closes **Riot Client** and related games, and reverses those steps on re-enable with **explicit per-step verification**. Flows use Windows **service control**, **startup entry** changes, and **WinVerifyTrust** signature verification before terminating Riot processes. Optional **GitHub release** self-update verifies **SHA-256** of downloaded artifacts. (source: wiki/sources/descriptions/shinishiz__VanguardSwitch.md)

## Edge cases

The implementation documents handling for **VAN 57** errors and **driver boot-state** inconsistencies when toggling Vanguard outside official On-Demand. (source: wiki/sources/descriptions/shinishiz__VanguardSwitch.md)

## Positioning

Operational **Vanguard exposure management** between play sessions—not an in-match AC bypass. Compare [[faceoff]] (FACEIT driver/service toggle) and [[vanguard-service-manager-vgk-control]] (`vgk` auto-start SCM control).

## Links

- Repo: https://github.com/shinishiz/VanguardSwitch

## Related

[[vanguard]] · [[vanguard-service-manager-vgk-control]] · [[vanguard-update-notifier]] · [[faceoff]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
