---
title: SEWindows
kind: entity
topics: [windows-kernel, anti-cheat, dma-attack]
sources:
  - wiki/sources/descriptions/fsquirt__SEWindows.md
updated: 2026-08-15
confidence: medium
---

# SEWindows

Windows **TPM measured-boot analysis and remote attestation** tool (fsquirt) that parses TCG event logs, verifies PCR values, analyzes **WBCL** boot policy, and performs **EK/AK-based remote attestation** with security-feature reporting. It acts as a TPM-based verifier for CPU virtualization, [[iommu]], Secure Boot, VBS/[[hvci]], DSE, and the vulnerable-driver blocklist — supporting both local PCR replay and remote attestation workflows. (source: wiki/sources/descriptions/fsquirt__SEWindows.md)

Useful for anti-cheat and [[dma]] defense research where external trust anchors (measured boot, TPM Quote, boot-chain integrity) complement bus-layer PCIe/IOMMU checks that firmware can evade in isolation.

Complements stack-integrity probes such as [[detect-tpm-spoofing]] (IOCTL vs `TPM.sys` cache mismatch) and ground-truth MMIO reads via [[tpm-mmio]]; contrasts with offensive HWID lanes such as [[tpm-spoofer]].

## Links

- Repo: https://github.com/fsquirt/SEWindows

## Related

[[overviews/windows-kernel]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[hvci]] · [[dma]] · [[detect-tpm-spoofing]] · [[tpm-mmio]] · [[tpm-spoofer]]
