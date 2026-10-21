---
title: iG Windows Tuner
kind: entity
topics: [anti-cheat, windows-kernel]
sources:
  - wiki/sources/descriptions/arioofarmani__iG-Windows-Tuner.md
  - wiki/sources/README-categories.md
updated: 2026-10-21
confidence: medium
---

# iG Windows Tuner

**Auditable, reversible Windows 11 optimization tool** for competitive gaming that keeps **Defender**, **virtualization-based security (VBS)**, **Secure Boot**, and **TPM** requirements intact while applying measurable performance tweaks. (source: wiki/sources/descriptions/arioofarmani__iG-Windows-Tuner.md)

Implemented in **PowerShell** with a read-only **WPF** GUI and a **data-driven engine** that applies cataloged tweaks from **JSON schemas** covering power, graphics, input, network, privacy, and security settings. **Hardware-profile presets** complement manual selection. Each change is **evidence-tiered** against vendor documentation, captured in **JSON snapshots** with **System Restore** points, and revertible individually or in bulk.

Operator-facing features include system health and **per-anti-cheat readiness** reports, **Defender attack surface reduction** management, **security scoring**, **kernel** and **power** inspectors, and **safe system maintenance** utilities—aimed at gamers and PC tuners who want tuning without disabling kernel anti-cheat prerequisites.

Listed in the README under **Anti Cheat** (Guide / PC readiness lane) alongside read-only diagnostics such as [[securebootcheck]].

## Links

- Repo: https://github.com/arioofarmani/iG-Windows-Tuner

## Related

[[overviews/anti-cheat]] · [[overviews/windows-kernel]] · [[securebootcheck]] · [[hvci]] · [[windows-runtime-attestation-report]] · [[custos]]
