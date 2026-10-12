---
title: KAC Inspector
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/saadahmedscse__kac-inspector.md
  - wiki/sources/README-categories.md
updated: 2026-10-12
confidence: medium
---

# KAC Inspector

**KAC Inspector** (saadahmedscse/kac-inspector) is a read-only **Windows CLI** that inventories kernel-mode anti-cheat drivers and labels each match as actively running, loaded-but-stopped, orphaned on disk, or stale. Rust correlates `EnumDeviceDrivers` module lists, Service Control Manager state, and the driver store against a built-in signature database (with heuristics for unlisted drivers that self-identify as anti-cheat), optionally surfacing related user-mode services—no installs, kernel patches, or network I/O. Targets players troubleshooting launch conflicts, privacy reviewers, and researchers who need a quick kernel AC presence snapshot before deeper forensics. (source: wiki/sources/descriptions/saadahmedscse__kac-inspector.md)

## Evidence model

- **Multi-source correlation** — kernel module list vs SCM vs driver-store paths reduce false positives from stale `.sys` files alone.
- **Status labels** — running, loaded, stopped, orphaned, stale; concise overall verdict for triage.
- **Read-only scope** — observation-only; pair conclusions with [[kernel-evidence-baseline]] build/symbol context when attributing behavior to a specific AC product.

## Positioning

Complements host survey tooling in [[apex-anticheat-lab]] (PowerShell driver/PCIe inventory) and screenshare forensics such as [[dexcheck]] with a lightweight **kernel AC driver census**—useful before BattlEye/EAC/Vanguard troubleshooting or when documenting what kernel components were present on a machine under review.

## Peers

[[apex-anticheat-lab]] · [[dexcheck]] · [[securebootcheck]] · [[hawkeye]] · [[mobsentry]]

## Links

- Repo: https://github.com/saadahmedscse/kac-inspector
