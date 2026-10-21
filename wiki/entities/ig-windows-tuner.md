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

**Auditable, reversible Windows 11 optimization tool** for competitive gaming that keeps **Defender**, **VBS**, **Secure Boot**, and **TPM** requirements intact while tuning power, graphics, input, network, privacy, and security settings from JSON-schemas. (source: wiki/sources/descriptions/arioofarmani__iG-Windows-Tuner.md)

Implemented in PowerShell with a read-only WPF GUI; each tweak is evidence-tiered against vendor documentation, captured in JSON snapshots with System Restore points, and revertible individually or in bulk. Adds health and **per-anti-cheat readiness** reports, Defender attack-surface reduction management, security scoring, and kernel/power inspectors for operators who want performance gains without disabling kernel AC prerequisites.

Listed in the README under **Anti Cheat** (Guide / PC readiness lane) alongside read-only diagnostics such as [[securebootcheck]].

## Links

- Repo: https://github.com/arioofarmani/iG-Windows-Tuner

## Related

[[overviews/anti-cheat]] · [[securebootcheck]] · [[hvci]] · [[windows-runtime-attestation-report]] · [[custos]]
