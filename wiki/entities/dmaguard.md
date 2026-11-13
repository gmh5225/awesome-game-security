---
title: dmaguard
kind: entity
topics: [dma-attack, anti-cheat, windows-kernel, reverse-engineering]
sources:
  - wiki/sources/descriptions/grimh3xx__dmaguard.md
  - wiki/sources/README-categories.md
updated: 2026-11-13
confidence: medium
---

# dmaguard

**dmaguard** (grimh3xx) is a **read-only command-line auditor** that assesses whether plugged-in devices could **DMA-read system memory** by inspecting firmware and OS DMA protections. Targets blue-team operators, hardware security reviewers, and workstation hardening against **external PCIe and Thunderbolt** DMA surfaces—not runtime enforcement. (source: wiki/sources/descriptions/grimh3xx__dmaguard.md)

## Platform and scope

Rust CLI for **Windows and Linux x64**. Parses **ACPI DMAR and IVRS** in-tree and correlates findings with live **IOMMU state**, kernel boot parameters, **Thunderbolt security levels**, and **Windows Kernel DMA Protection**. (source: wiki/sources/descriptions/grimh3xx__dmaguard.md)

## Outputs and modes

Emits structured findings with **severity codes** (for example missing IOMMU, passthrough mode, or disabled pre-boot DMA opt-in). Supports **JSON** and **SARIF** export, offline Linux snapshots, and standalone ACPI table dumps. (source: wiki/sources/descriptions/grimh3xx__dmaguard.md)

## Detection relevance

Maps to the [[iommu-state-verification]] four-property model: separates ACPI advertisement, OS policy (KDP), live unit state, and requester coverage instead of collapsing posture into a single boolean. Complements bus/memory collectors such as [[drvscan]] and screenshare probes such as [[dexcheck]] in the Anti Cheat `Detection:DMA` lane. (source: wiki/sources/README-categories.md)

## Links

- Repo: https://github.com/grimh3xx/dmaguard

## Related

[[iommu]] · [[iommu-state-verification]] · [[assurance-boundaries]] · [[drvscan]] · [[dexcheck]] · [[dmaprotect]] · [[diedmaprotection]] · [[vtd-bypass]] · [[dma]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
