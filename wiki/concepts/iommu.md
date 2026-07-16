---
title: IOMMU
kind: concept
topics: [dma-attack, anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/dma-attack.md
updated: 2026-07-16
confidence: high
---

# IOMMU

I/O Memory Management Unit (Intel VT-d / AMD-Vi) that translates device IOVAs using the Requester ID (BDF) and enforces per-device permissions—the primary software-controlled barrier against out-of-domain [[dma]]. (source: wiki/sources/skills/dma-attack.md)

## Defense uses

- Strict domains instead of identity/passthrough mappings
- ACS on bridges (source validation, translation blocking, P2P redirect)
- Interrupt Remapping for MSI/MSI-X
- Fault-rate monitoring; containment via sandbox remapping, BME clear, or DPC
- ATS-untrusted policy for untrusted endpoints

## Limits

Misconfigured BIOS, pre-boot DMA, ACS holes, ATS abuse, over-mapped pages, or kernel compromise reprogramming tables can defeat IOMMU alone—hence layered attestation with [[hvci]]/TPM.

## Related

[[dma]] · [[overviews/dma-attack]] · [[hvci]]
