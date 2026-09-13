---
title: Assurance Boundaries
kind: concept
topics: [dma-attack, anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/dma-attack.md
updated: 2026-09-13
confidence: high
---

# Assurance Boundaries

Use when a report promises universal detection, runtime integrity, or protection from a device label or platform feature alone. Separate **mechanism**, **deployed policy**, **evidence coverage**, and **attribution** before drawing enforcement conclusions. (source: wiki/sources/skills/dma-attack.md)

## Device labels vs detection evidence

A firmware nickname, price, public/private status, or claimed sophistication tier does not establish measured detector coverage. Replace tier rankings with observed identity, configuration, functionality, topology, and access-policy evidence. Record collection method, exact hardware/firmware/driver, workload, matched benign controls, and false-positive uncertainty. An unexpected identifier or absent driver can justify investigation without establishing unauthorized memory access. Apply [[research-rigor]] for evaluation design. PCI identity inspection, remapping enforcement, and boot attestation observe different properties—their documented mechanisms do not establish a universal tier ladder. (source: wiki/sources/skills/dma-attack.md)

## CPU access vs device access

EPT concerns processor memory virtualization; VT-d/AMD-Vi supplies independent device DMA remapping. An EPT violation is not, by itself, a record of a PCIe DMA transaction. A hypervisor may manage both mechanisms, but its presence does not establish that either policy covers the relevant access path. For protected-page or decoy claims, identify the requester and collector: CPU access under active EPT policy, device request under an active [[iommu]] domain, or an application event. Report denied permission separately from malicious intent—no EPT event does not prove no DMA access. Classify the initiator first with [[memory-acquisition-path]]. (source: wiki/sources/skills/dma-attack.md)

## Separate platform features and deployment state

Memory integrity ([[hvci]]) isolates kernel code-integrity decisions using VBS. Treat code integrity, vulnerable-driver blocking, and DMA policy as distinct controls—a blocklist cannot cover every vulnerable driver. Kernel DMA Protection does not require VBS; device DMA remapping can be enabled independently. Runtime protection and firmware pre-boot responsibilities are separate. Review actual device/driver remapping and platform policy, not one UI flag. A missing feature is a policy/compatibility question, not a misconduct finding.

## Attestation has a defined subject

A TPM quote signs selected PCR information and caller-supplied qualifying data. PCR banks, reset/extend permissions, and platform profiles matter; neither all PCRs nor all boot measurements share one universal allocation. Preserve the selected bank, PCRs, nonce, and event-log relationship when interpreting a result. Verifier trust includes key enrollment and the applicable trust chain. A valid quote or accepted boot policy does not enumerate current PCIe devices, current IOMMU mappings, or every runtime action—obtain separate evidence for those unmeasured properties. Secure Launch/DRTM establishes a measured execution path at startup; do not describe it as an arbitrary post-boot application launch or a complete runtime scan.

## Containment belongs to the platform owner

Windows reserves PCI configuration headers and capability registers to the OS; supported configuration interfaces do not grant arbitrary write authority over them. A generic game-security collector should not rewrite another driver's bus-master, interrupt, BAR, or remapping state without documented OS/driver lifecycle and policy controls. Containment success depends on the actual platform path and verified state, not a firmware tier. Preserve evidence before applying an authorized response and keep access restriction separate from a sanction decision. Prefer explicit unsupported/unknown state over claims that a direct register change or a TPM quote closes every remaining gap.

## Related

[[memory-acquisition-path]] · [[iommu]] · [[hvci]] · [[dma]] · [[research-rigor]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]] · [[overviews/windows-kernel]]
