---
title: IOMMU
kind: concept
topics: [dma-attack, anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/tandasat__HelloIommuPkg.md
  - wiki/sources/descriptions/iqrw0__DieDMAProtection.md
updated: 2026-08-04
confidence: high
---

# IOMMU

I/O Memory Management Unit (Intel VT-d / AMD-Vi) translates device IOVAs using the Requester ID (BDF) and enforces per-device read/write permissions—the primary software-controlled barrier against out-of-domain [[dma]]. (source: wiki/sources/skills/dma-attack.md)

## Translation flow

1. Device issues a Memory TLP with IOVA; header carries 16-bit BDF.
2. TLP reaches root complex; IOMMU walks I/O page tables (VT-d: Root → Context → SLPT; AMD-Vi: Device Table → I/O PT).
3. Permission bits checked; success forwards translated physical address; failure logs fault and returns UR/CA.

Translations cache in IOTLB; ATS adds a device-side DevTLB—invalidation must reach both or stale mappings persist.

## Isolation primitives

- **IOMMU groups:** devices behind a switch share a group unless ACS enables port isolation.
- **ACS (Access Control Services):** Source Validation drops spoofed Requester IDs; Translation Blocking blocks AT=10 (translated) TLPs; P2P Request/Completion Redirect forces peer traffic through the IOMMU.
- **Interrupt Remapping:** without IR, any bus-master can write MSI addresses to `0xFEE00000` range.
- **ATS-untrusted:** disable or block ATS for FPGAs, Thunderbolt enclosures, and other untrusted endpoints—AT=10 TLPs must not bypass page walks.

Sample DXE remapping programming appears in [[helloiommupkg]] (learning-only, not production AC). (source: wiki/sources/descriptions/tandasat__HelloIommuPkg.md)

## Six paths to out-of-domain access

| # | Path | Notes |
|---|------|-------|
| 1 | IOMMU disabled / not applied | BIOS or OS policy gap |
| 2 | Pre-boot DMA | Before IOMMU init |
| 3 | Identity / passthrough domain | 1:1 IOVA→PA mapping |
| 4 | Driver over-allocation | Full 4 KB page maps adjacent kernel data |
| 5 | Legitimate-path exfil | Spoofed NIC reads own RX ring within mapped IOVAs—**invisible to IOMMU layer** |
| 6 | Kernel table reprogramming | [[byovd]] or compromised kernel |

Windows PoC [[diedmaprotection]] disables active DMA remapping (IOMMU/VT-d) from kernel mode to restore out-of-domain PCIe access—illustrating path 1/6 when OS policy can be subverted at runtime. (source: wiki/sources/descriptions/iqrw0__DieDMAProtection.md)

Paths 1–3 underpin most commercial DMA cheats today. (source: wiki/sources/skills/dma-attack.md)

## Bypass catalog (selected)

| Technique | Mitigation |
|-----------|------------|
| ACS missing on bridge | Walk topology; verify SV, TB, RR, CR |
| ATS abuse | ATS-untrusted policy per endpoint |
| Lazy IOTLB invalidation | Strict invalidation mode |
| RMRR/IVMD scope abuse | Audit ACPI tables; measured boot |
| Interrupt injection (no IR) | Mandatory interrupt remapping |
| Hypervisor / SMM escape | VBS, Boot Guard, attestation |

Full 16-entry catalog in skill source; techniques 7–16 are mostly academic, APT, or firmware-level.

## Defense uses

- Strict domains instead of identity/passthrough mappings
- Fault-rate monitoring (VT-d Fault Recording, AMD-Vi Event Log, WHEA)
- Live containment: sandbox domain remapping, Bus Master Enable clear, Downstream Port Containment (DPC)
- Pre-game audit: passthrough domains, oversized IOMMU groups, RMRR overlap with game memory

## Limits

Misconfigured BIOS, pre-boot DMA, ACS holes, ATS abuse, over-mapped pages, legitimate-path exfil, or kernel compromise reprogramming tables can defeat IOMMU alone—hence layered PCIe fingerprinting, hypervisor EPT, and TPM/measured-boot attestation with [[hvci]].

## Related

[[dma]] · [[helloiommupkg]] · [[diedmaprotection]] · [[byovd]] · [[hvci]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
