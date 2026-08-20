---
title: Alibi
kind: entity
topics: [anti-cheat, game-hacking, dma-attack, windows-kernel]
sources:
  - wiki/sources/descriptions/Sutaigne__alibi.md
updated: 2026-08-20
confidence: medium
---

# Alibi

Read-only Windows forensic scan kit that helps accused players **prove they are not cheating** by producing shareable text and HTML reports for tournament admins, Discord mods, or lobby reviewers. Built mainly in PowerShell with batch launchers and offline HTML companions, it inspects the machine the way an investigator would—without installing software, creating accounts, or sending telemetry off the PC. (source: wiki/sources/descriptions/Sutaigne__alibi.md)

## Scan modes

| Mode | Targets |
|------|---------|
| **PC scan** | Cheat software, DMA artifacts, HWID spoofers, [[byovd]]-adjacent driver residue |
| **Console-rig scan** | Capture-card stacks, vision aimbots, input adapters (XIM, Cronus, ReaSnow) |

Scans emit clear verdict tiers and self-contained visual reports. Supported title coverage includes Call of Duty, CS2, Apex Legends, Escape from Tarkov, Rust, Rainbow Six Siege, and Marvel Rivals.

## Workflow

1. Run the local read-only scan (no host modification).
2. Review verdict tier and artifact summary in the generated report.
3. Share the self-contained text/HTML output with reviewers.

Primary use case: **defensive game-security attestation** for accused players who need auditable, local evidence—not a traditional always-on anti-cheat product.

## Links

- Repo: https://github.com/Sutaigne/alibi

## Related

[[jaranalyzer]] · [[driver-risk-scout]] · [[drvscan]] · [[vulnerable-driver-scanner]] · [[hardware-input-injection]] · [[ai-aimbot-detection]] · [[dma]] · [[byovd]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]] · [[overviews/dma-attack]]
