---
title: IOMMU
kind: concept
topics: [dma-attack, anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/dma-attack.md
  - wiki/sources/descriptions/tandasat__HelloIommuPkg.md
  - wiki/sources/descriptions/iqrw0__DieDMAProtection.md
  - wiki/sources/descriptions/cutecatsandvirtualmachines__DmaProtect.md
  - wiki/sources/descriptions/BigAnteater__KVM-GPU-Passthrough.md
updated: 2026-09-09
confidence: high
---

# IOMMU

I/O Memory Management Unit (Intel VT-d / AMD-Vi) translates device IOVAs using the Requester ID (BDF) and enforces per-device read/write permissions—the primary software-controlled barrier against out-of-domain [[dma]] when remapping is active on the device path. Classify the initiator first with [[memory-acquisition-path]]; host-mediated capture and hypervisor EPT events are separate boundaries. (source: wiki/sources/skills/dma-attack.md)

## Translation flow

1. Device issues a Memory TLP with IOVA; header carries 16-bit BDF.
2. TLP reaches root complex; IOMMU walks I/O page tables (VT-d: Root → Context → SLPT; AMD-Vi: Device Table → I/O PT).
3. Permission bits checked; success forwards translated physical address; failure logs fault and returns UR/CA.

Translations cache in IOTLB; ATS adds a device-side DevTLB—invalidation must reach both or stale mappings persist.

## Isolation primitives

- **IOMMU groups:** devices behind a switch share a group unless ACS enables port isolation.
- **ACS (Access Control Services):** Source Validation drops spoofed Requester IDs; Translation Blocking blocks AT=10 (translated) TLPs; P2P Request/Completion Redirect forces peer traffic through the IOMMU.
- **Interrupt Remapping:** without IR, any bus-master can write MSI addresses to `0xFEE00000` range.
- **ATS-untrusted:** disable or block ATS for FPGAs, Thunderbolt enclosures, and other untrusted endpoints—AT=10 (translated) TLPs must not bypass page walks. ATS lets devices cache IOMMU translations in a DevTLB; a malicious endpoint can present arbitrary translated addresses unless policy treats it as untrusted (Linux `pci=noats` quirks; Windows Kernel DMA Protection per-endpoint—not a blanket guarantee for internal slots).
- **RMRR/IVMD:** ACPI DMAR RMRR and AMD IVMD tables declare identity-mapped ranges; audit for suspect BDFs or overlap with game memory regions.

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

## Bypass catalog (16 techniques)

| # | Technique | Mitigation |
|---|-----------|------------|
| 1 | IOMMU disabled | Refuse misconfigured platforms |
| 2 | Pre-boot DMA | UEFI updates; verify ACPI indicators |
| 3 | Identity/passthrough domain | Strict-mode IOMMU policy |
| 4 | Driver over-allocation | OS bounce buffers; strict mappings |
| 5 | ATS abuse | ATS-untrusted for non-allowlisted endpoints |
| 6 | ACS missing on bridge | Verify SV, TB, RR, CR on all bridges |
| 7 | Lazy IOTLB invalidation | Strict invalidation mode |
| 8 | FLR race | Synchronized FLR handling |
| 9 | SMM bypass | Boot Guard / Platform Secure Boot |
| 10 | DMA-remapping driver bugs | OS patching |
| 11 | Hypervisor trust failure | Platform remediation; boot evidence ≠ runtime proof |
| 12 | Interrupt injection (no IR) | Mandatory interrupt remapping |
| 13 | RMRR/IVMD scope abuse | Measured boot; runtime RMRR audit |
| 14 | Snoop-bit manipulation | Strict snoop enforcement |
| 15 | PASID confusion | PASID-aware IOMMU programming |
| 16 | DMAR/IVRS spoofing | Measured boot covering firmware |

Techniques 1–6 are the active surface for most commercial DMA cheats; 7–13 appear in academic, APT, or firmware contexts; 14–16 are largely theoretical. (source: wiki/sources/skills/dma-attack.md)

## Defense uses

- Windows kernel driver [[dmaprotect]] programs VT-d/AMD-Vi remapping tables to block unauthorized PCIe DMA while permitting legitimate device domains—defensive runtime counterpart to [[diedmaprotection]]. (source: wiki/sources/descriptions/cutecatsandvirtualmachines__DmaProtect.md)
- Strict domains instead of identity/passthrough mappings
- Fault-rate monitoring (VT-d Fault Recording, AMD-Vi Event Log, WHEA)
- Live containment: sandbox domain remapping, Bus Master Enable clear, Downstream Port Containment (DPC)—use OS-managed lifecycle; remapping, BME, and DPC differ in prerequisites and scope
- Pre-game audit: passthrough domains, oversized IOMMU groups, RMRR overlap with game memory
- Per-device fault rate: sustained faults need driver-bug and reset exclusions before attributing malicious out-of-domain access
- Lab setup guides such as [[kvm-gpu-passthrough]] (BigAnteater; Arch Linux GRUB/libvirt/QEMU templates; IOMMU/VT-d and AMD/Intel BIOS prerequisites for GPU passthrough VMs) document the **host-side isolation topology** researchers must validate before assigning devices to VFIO guests. (source: wiki/sources/descriptions/BigAnteater__KVM-GPU-Passthrough.md)

## Limits

Misconfigured BIOS, pre-boot DMA, ACS holes, ATS abuse, over-mapped pages, legitimate-path exfil, or kernel compromise reprogramming tables can defeat IOMMU alone—hence layered PCIe fingerprinting, hypervisor EPT, and TPM/measured-boot attestation with [[hvci]].

## Related

[[dma]] · [[memory-acquisition-path]] · [[helloiommupkg]] · [[dmaprotect]] · [[diedmaprotection]] · [[kvm-gpu-passthrough]] · [[byovd]] · [[hvci]] · [[overviews/dma-attack]] · [[overviews/anti-cheat]]
