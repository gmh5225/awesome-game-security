---
title: IronTrace
kind: entity
topics: [anti-cheat, dma-attack, windows-kernel]
sources:
  - wiki/sources/descriptions/codedevdev__irontrace.md
updated: 2026-09-01
confidence: medium
---

# IronTrace

Windows **hardware and forensic integrity scanner** for game-server administrators reviewing player machines for cheating-related signals. Built primarily in **C#** with a WPF desktop app, headless CLI, and optional ASP.NET Core server, it collects evidence about platform security, PCI/PCIe and USB devices, drivers, **DMA masquerade indicators**, and optional forensic layers such as execution artifacts, [[byovd]] abuse, HWID mismatches, and memory integrity via external hollows_hunter. Offline reference databases cover PCI IDs, USB IDs, and [[loldrivers]]; a conservative risk engine produces **explainable JSON verdicts without auto-banning**. Optional upload to a self-hosted server supports human admin triage. An optional **KMDF** kernel driver (C++) provides bounded PCI evidence collection for lab use. Intended for anti-cheat investigation and hardware integrity auditing—not cryptographic proof of cheating or a DMA attack toolkit. (source: wiki/sources/descriptions/codedevdev__irontrace.md)

Complements PCIe inventory tooling such as [[pcie-detector]] and [[drvscan]], driver-risk scanners such as [[driver-risk-scout]] and [[loldriverscan]], and dispatch-integrity auditors such as [[device-control-hooks-scanner]].

## Links

- Repo: https://github.com/codedevdev/irontrace (README tag: Windows hardware and forensic integrity scanner for game-server anti-cheat with DMA/PCIe/USB watchlists and explainable integrity reports)

## Related

[[overviews/anti-cheat]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]] · [[pcie-detector]] · [[drvscan]] · [[driver-risk-scout]] · [[loldriverscan]] · [[loldrivers]] · [[byovd]] · [[device-control-hooks-scanner]]
