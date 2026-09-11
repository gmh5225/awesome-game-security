---
title: AntiCheatToggle
kind: entity
topics: [anti-cheat, windows-kernel, game-hacking]
sources:
  - wiki/sources/descriptions/lsxll666__AntiCheatToggle.md
updated: 2026-09-11
confidence: medium
---

# AntiCheatToggle

**AntiCheatToggle** (lsxll666) — small Windows **WinForms** utility (C# / .NET Framework) with GUI and CLI that **stops and disables** game anti-cheat **kernel drivers and services** so **VirtualBox** can launch VMs without `supR3HardenedWinReSpawn` **VERR_INVALID_NAME (-104)** errors. Targets **Perfect World Arena**, **Tencent ACE**, and **Reason CyberSecurity** drivers/services: stop service, optionally kill matching user-mode processes, set registry **Start** type to disabled. Backs up original service start types on first use; one-click or `--on` restore; `--off` and `--status` for scripting. Does not modify VirtualBox. For Windows users and security researchers who need to **temporarily** bypass kernel AC interference with virtualization; affected games may refuse to run while protection is disabled. (source: wiki/sources/descriptions/lsxll666__AntiCheatToggle.md)

README tag: Cheat / QEMU/KVM/PVE/VBOX research-host lane.

## Links

- Repo: https://github.com/lsxll666/AntiCheatToggle

## Related

[[virtualbox]] · [[virtualbox-kvm]] · [[ff-ace-anticheat-analysis]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/reverse-engineering]]
