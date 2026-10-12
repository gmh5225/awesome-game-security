---
title: KAC Inspector
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/saadahmedscse__kac-inspector.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: high
---

# KAC Inspector

**KAC Inspector** (saadahmedscse/kac-inspector) is a read-only **Windows CLI** that scans for kernel-mode anti-cheat drivers and reports whether each match is actively loaded, idle, running, or leftover on disk. Rust correlates the kernel module list (`EnumDeviceDrivers`), Service Control Manager service state, and the system driver store against a built-in database of dozens of known anti-cheat signatures, plus heuristics for unlisted drivers that identify themselves as anti-cheat. Output includes a concise overall verdict and per-driver labels (running, loaded, stopped, orphaned, stale) and can surface related user-mode services—without installing software, modifying the system, or using the network. Aimed at players troubleshooting launch conflicts, privacy assessment, and researchers who need a read-only kernel AC presence snapshot before deeper game-security or host forensics. (source: wiki/sources/descriptions/saadahmedscse__kac-inspector.md)

## Evidence model

- **Multi-source correlation** — kernel module list vs SCM vs driver-store paths reduce false positives from stale `.sys` files alone.
- **Status labels** — running, loaded, stopped, idle, orphaned, stale; concise overall verdict for triage.
- **Read-only scope** — observation-only; pair conclusions with [[kernel-evidence-baseline]] build/symbol context when attributing behavior to a specific AC product.

## Positioning

Complements host survey tooling in [[apex-anticheat-lab]] (PowerShell driver/PCIe inventory) and screenshare forensics such as [[dexcheck]] with a lightweight **kernel AC driver census**—useful before BattlEye/EAC/Vanguard troubleshooting or when documenting what kernel components were present on a machine under review.

## Peers

[[apex-anticheat-lab]] · [[dexcheck]] · [[securebootcheck]] · [[hawkeye]] · [[mobsentry]]

## Links

- Repo: https://github.com/saadahmedscse/kac-inspector
