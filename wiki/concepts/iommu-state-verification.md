---
title: IOMMU State Verification
kind: concept
topics: [dma-attack, anti-cheat, windows-kernel]
sources:
  - wiki/sources/skills/dma-attack.md
updated: 2026-09-26
confidence: high
---

# IOMMU State Verification

Use when a check or report claims VT-d/AMD-Vi is "enabled," Kernel DMA Protection (KDP) covers a device, or an ACPI table proves runtime DMA isolation. The defensive model is read-only and provenance-focused; Windows implementation details vary by build and platform. Do not collapse these observations into a single `iommu_enabled` boolean. (source: wiki/sources/skills/dma-attack.md)

## Four properties to keep separate

| Property | Question | Possible evidence | What that evidence does not establish |
|----------|----------|-------------------|--------------------------------------|
| **Advertised** | Does firmware expose a remapping description? | ACPI DMAR (Intel) or IVRS (AMD) via documented OS interface | That the described hardware exists, is enabled, or is used by Windows |
| **OS policy** | Does Windows report a platform protection policy? | Documented KDP / Memory access protection status for the target build | That every internal endpoint is remapped or that a particular request was denied |
| **Live unit state** | Is a remapping unit configured and translating now? | Platform-owner diagnostics or supported OS interface with unit-level semantics | That all requesters use that unit or have restrictive mappings |
| **Requester coverage** | Is this device's traffic subject to the intended translation policy now? | Per-device policy/domain evidence, topology + requester identity, fault/diagnostic evidence where available | That no access occurred, or that every mapping is safe, unless separately verified |

A fifth observation—an actual denied request or controlled test outcome—supports a narrow claim about **that request** only. Record unavailable evidence as **unknown**, not pass or fail. Route certainty claims about HVCI, containment, or TPM proof through [[assurance-boundaries]]; classify the initiator first with [[memory-acquisition-path]].

## Advertised: parse ACPI as untrusted input

On Windows, `GetSystemFirmwareTable` returns ACPI table bytes exposed through the OS interface—not an independent physical read or cryptographic authenticity check. Preserve enumeration results, returned bytes, API result, requested signature, OS build, and collection time. Validate declared length and checksum before interpreting fields; preserve unknown structure types and raw bytes.

For Intel DMAR, the fixed table portion is 48 bytes before remapping structures begin. Type 0 is DRHD; type 1 is RMRR. AMD IVRS has its own layout—do not parse it as DMAR. A checksum-valid table or plausible OEM string is a consistency signal, not authentication. Conversely, an unexpected table can be inconclusive under platform quirks; retain raw results and compare against matched hardware/firmware baselines.

## OS policy: KDP is a separate signal

Record Windows' documented KDP status and the source used (`msinfo32` Memory access protection / Kernel DMA Protection field). These are system-level policy views, not a per-requester audit. **KDP On is not proof that every internal PCIe endpoint is covered.** KDP Off or unsupported is a platform-policy result—not, by itself, proof of cheating. Per-device **DMA Remapping Policy** in Device Manager (values 0/1 = no driver support; 2 = supported; absent = no support) is driver-policy evidence, not proof of current mappings.

VBS, Memory Integrity ([[hvci]]), Secure Boot, and KDP are related but distinct. Do not infer KDP from HVCI/VBS, or live mappings from undocumented UI, registry, or WMI values. See [[assurance-boundaries]] for the separation.

## Live unit state: no guesswork probing

Intel VT-d and AMD-Vi define unit registers (capability, Global Status / Translation Enable, root-table pointer). A status bit can show a unit is configured; it does not alone prove correct mappings, interrupt-remapping state, or endpoint coverage. There is no generic anti-cheat recipe to map arbitrary DRHD/IVHD bases and read/write registers—PCI/IOMMU hardware is platform/OS-owned. Use only documented interfaces owned by the responsible platform component; otherwise record live unit state as **unknown**. Never write RTADDR, translation-enable, invalidation, or page-table state as a detection action.

## Requester coverage: scopes ≠ runtime mappings

DMAR DRHD device scopes describe remapping-unit relationships in firmware (segment, BDF paths, include-all cases). Correct parsing answers a topology question; it does **not** prove Windows assigned a restrictive domain, that all DMA paths traverse that unit, or that I/O page tables exclude game memory. Keep explicit: PnP topology, requester identity (segment + BDF via supported interface), applicable DRHD/IVHD scope, and any supported OS/driver remapping evidence with time limits.

VMD is a topology/ownership case—use Windows' enumerated PnP tree and supported bus/driver interfaces. If a child cannot be mapped to a requester or unit, mark coverage **unknown**; do not substitute undocumented structure offsets or direct BAR mapping. A static scope that appears to omit a device is a lead for platform investigation, not proof of bypass until include-all rules, topology, aliases, OS policy, and routing are resolved.

## Evidence checklist

Retain separate fields per machine/session:

```text
ACPI advertisement:       present / absent / malformed / unknown
Windows policy:            on / off / unsupported / unknown
Live unit state:           enabled / disabled / conflicting / unknown
Requester coverage:        evidenced / not evidenced / conflicting / unknown
Observed DMA faults:       count + source + interval, or unavailable
Device identity/topology:  source + timestamp + collection limitations
```

Use **not evidenced** when the collector cannot establish coverage; reserve **not covered** for evidence that demonstrates that state. A zero fault count only means no faults were observed by that source during that interval.

Staged defensive assessment: (1) inventory devices via supported PnP surfaces; (2) collect read-only config within collector ownership; (3) parse ACPI advertisement with strict validation; (4) record KDP separately from live-unit evidence; (5) correlate scope and runtime coverage only where supported evidence exists; (6) observe hot-plug, policy changes, and fault telemetry with baselines; (7) apply launch policy only against documented compatibility baseline, tested false-positive rate, and recovery path. Apply [[research-rigor]] before attributing malicious intent from a fault or identifier mismatch alone.

Runtime DMAR/ACPI spoofing via physical memory (e.g. [[vtd-bypass]]) illustrates why **advertised** state must not be equated with **live unit state** or **requester coverage**.

## Related

[[iommu]] · [[assurance-boundaries]] · [[memory-acquisition-path]] · [[hvci]] · [[vtd-bypass]] · [[pcie-detector]] · [[research-rigor]] · [[overviews/dma-attack]] · [[overviews/windows-kernel]]
