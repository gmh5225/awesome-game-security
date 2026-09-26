# IOMMU State Verification

Use this reference whenever a check or report claims that VT-d/AMD-Vi is
"enabled," that Kernel DMA Protection (KDP) covers a device, or that an ACPI
table proves runtime DMA isolation. The defensive model is read-only and
provenance-focused; Windows implementation details vary by build and platform.

The local [`kEv1nZ0/VTD-Bypass` archive](../../../../archive/kEv1nZ0/VTD-Bypass.txt)
is a historical sample for threat modeling, not proof that its README claims
work on a given machine. Do not reproduce its ACPI or physical-memory write
behavior. Public architecture contracts and target-machine observations must
support any conclusion.

## Keep Four Properties Separate

| Property | Question | Possible evidence | What that evidence does not establish |
|---|---|---|---|
| **Advertised** | Does firmware expose a remapping description? | ACPI DMAR (Intel) or IVRS (AMD) returned through a documented OS interface | That the described hardware exists, is enabled, or is used by Windows |
| **OS policy** | Does Windows report a platform protection policy/capability? | A documented, build-appropriate Windows status surface, including KDP reporting | That every internal endpoint is remapped or that a particular request was denied |
| **Live unit state** | Is a particular remapping unit configured and translating now? | Platform-owner diagnostics or a supported OS interface with unit-level semantics | That all requesters use that unit or have restrictive mappings |
| **Requester coverage** | Is this device's traffic actually subject to the intended translation policy at this time? | Supported per-device policy/domain evidence, correct topology and requester identity, and where available fault/diagnostic evidence | That no access occurred, or that every mapping is safe, unless those properties were separately verified |

A fifth observation—an actual denied request or controlled test outcome—can
support a narrow claim about that request. It is not interchangeable with the
four properties above. Record unavailable evidence as **unknown**, not as a
pass or a failure. Do not collapse these fields into a single `iommu_enabled`
boolean.

## 1. Advertised: Parse ACPI as Untrusted Input

On Windows, `GetSystemFirmwareTable` with the ACPI provider retrieves the
contents of an ACPI table exposed through the OS interface; it is not, by itself,
an independent read of the physical table page or a cryptographic authenticity
check. Microsoft documents that duplicate ACPI signatures can be enumerated with
`EnumSystemFirmwareTables`, while `GetSystemFirmwareTable` returns only the first
matching table. Preserve the enumeration, returned bytes, API result, requested
signature, OS build, and collection time. Microsoft documents `FirmwareTableID`
as little-endian (for example, FACP is requested as PCAF). Thus DMAR uses the
reversed ID RAMD (DWORD value `0x52414D44`) and IVRS uses SRVI (`0x53525649`);
prefer explicit values over C/C++ multi-character literals, whose values are
implementation-defined. Validate the returned signature before parsing.

For a parser, validate before interpreting fields:

- Returned size is sufficient for the fixed header; the declared `Length` is
  within the returned buffer and meets the table-specific minimum.
- Checksum is computed only over the validated declared length.
- Every variable-length structure has a valid minimum size, stays within the
  table length, and advances without integer overflow or zero-length loops.
- Preserve unknown structure types and raw bytes; do not silently treat a
  truncated or unrecognized table as valid.

For Intel DMAR, the fixed table portion is 48 bytes before remapping structures
begin (the 36-byte ACPI header, host-address-width and flags bytes, and reserved
bytes). Validate each structure according to the applicable Intel VT-d
specification. Type 0 is a DRHD; type 1 is an RMRR. AMD IVRS has its own layout
and selector semantics—do not parse it as DMAR. See the applicable ACPI, Intel
VT-d, and AMD I/O Virtualization specifications for version-specific rules.

A checksum-valid table, a nonzero-looking register base, an OEM/creator string,
or an OEM-ID match with another ACPI table is only a consistency signal. These
fields are not signatures. OEM equality is not authentication, and a plausible
advertisement does not prove that the described register block is live. Conversely,
platform quirks and collection limits can make an unexpected table inconclusive;
retain the raw result and test against matched hardware/firmware baselines.

Microsoft also documents a `FIRM` provider that returns a specified physical
address range. If a lab has authorized access to that distinct raw-range path,
record the address, provider, permissions, time and proof that the bytes are the
same table/version before comparing them with the ACPI-provider result. Two reads
through one function are not automatically independent evidence. Do not directly
map or modify physical ACPI pages as generic anti-cheat collection guidance.

## 2. OS Policy: Treat KDP as a Separate Signal

Record Windows' documented KDP status for the target build and the source used
to obtain it. Microsoft documents Windows Security's **Memory access protection**
status and the **Kernel DMA Protection** field in System Information (`msinfo32`).
These are system-level policy/status views, not a per-requester audit. KDP depends
on platform support and applies protections according to Windows' device/port and
driver policy; **KDP On is not proof that every internal PCIe endpoint is
covered**. KDP Off, unavailable, or unsupported is a platform-policy and
compatibility result—not, by itself, proof of cheating. Microsoft also states
that per-device DMA remapping can be enabled independently of overall KDP when
VT-d and the driver policy support it; KDP Off therefore does not mean every
requester is unremapped.

Microsoft also documents a per-device **DMA Remapping Policy** property in
Device Manager's Details view: values 0 or 1 mean the driver does not support
DMA remapping, while 2 means it does; an absent property is documented as no
support, and the value may vary with device location. Distinguish an absent
reported property from a collector/API error.

Treat this as driver-policy/compatibility evidence, not proof that current IOMMU
mappings cover every request. VBS, Memory Integrity/HVCI, Secure Boot, and KDP
are related but distinct properties. Do not infer KDP from HVCI/VBS, or infer
live mappings from an undocumented UI, registry, or WMI value. See [DMA and
hypervisor assurance boundaries](assurance-boundaries.md) and [Microsoft's KDP
documentation](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt).

For an anti-cheat policy that requires DMA protection, state the supported
hardware/Windows baseline, the authoritative status source, the behavior when
status is unavailable, and the recovery path. Do not silently turn unknown into
"protected" or "tampered."

## 3. Live Unit State: Do Not Probe Hardware by Guesswork

Intel VT-d specifications define unit registers such as capability registers,
Global Status (including Translation Enable), and Root Table Address; AMD has a
different register and table model. A unit-level status bit can help establish
that a unit is configured, but it does not alone prove correct mappings,
interrupt-remapping state, or coverage of every endpoint. A nonzero root-table
pointer is not proof that the pointed-to tables are valid, current, or used by
the device under investigation.

There is no generic anti-cheat recipe to map an arbitrary DRHD/IVHD physical
base with `MmMapIoSpace` and read or write registers. PCI/IOMMU hardware and its
register lifecycle are platform/OS-owned; probing can conflict with Windows,
firmware, virtualization, or a device driver. Use only a documented interface
or diagnostics explicitly owned by the platform component responsible for that
state. Otherwise record live unit state as **unknown**. Never write RTADDR,
translation-enable, invalidation, or page-table state as a detection action.

A lab may compare OS-reported state with unit diagnostics on a controlled,
matched platform. Document the unit, segment/topology, tool and build, time,
read-only method, and the exact meaning of each field. Do not generalize one
Intel unit's register interpretation to AMD or to every Windows release.

## 4. Requester Coverage: Static Scopes Are Not Runtime Mappings

DMAR DRHD device scopes describe remapping-unit relationships in firmware,
including segment, bus/device/function paths and include-all cases. IVRS uses
AMD-specific structures. Correctly parsing a scope can answer a topology
question about the table; it does **not** by itself prove that Windows assigned
the requester a restrictive domain, that all DMA paths traverse that unit, or
that the current I/O page tables exclude game memory. Device scopes and runtime
DMA mappings are different evidence.

To assess a specific endpoint, keep the following identities and sources
explicit:

1. The present PnP device and its parent/bridge topology as Windows enumerates it.
2. The requester identity (including segment and BDF where available) derived
   through a supported interface, not guessed from a display name.
3. The applicable DRHD/IVHD scope, including include-all and bridge-path rules.
4. Any supported OS/driver evidence that the requester is actually remapped,
   plus the scope and time limits of that evidence.

VMD is a PCIe topology/ownership case, not permission to assume fixed
configuration-window offsets in a controller BAR. Use Windows' enumerated PnP
tree and supported bus/driver interfaces for devices it exposes. If a child
cannot be mapped reliably to a requester or remapping unit, mark coverage
**unknown**; do not replace missing evidence with undocumented `pci.sys`
structure offsets or direct BAR mapping.

There may be no public, generic Windows API that exposes every device's live
IOMMU domain and mappings to an anti-cheat. Be explicit about this limit. A
static DMAR/IVRS scope that appears to omit a device is a lead for platform
investigation, not proof of a bypass until include-all rules, topology, aliases,
OS policy, and actual routing are resolved.

## Evidence and Decision Checklist

For each machine/session, retain separate fields rather than one pass/fail bit:

```text
ACPI advertisement:       present / absent / malformed / unknown
Windows policy:            on / off / unsupported / unknown
Live unit state:           enabled / disabled / conflicting / unknown
Requester coverage:        evidenced / not evidenced / conflicting / unknown
Observed DMA faults:       count + source + interval, or unavailable
Device identity/topology:  source + timestamp + collection limitations
```

Use **not evidenced** when the collector cannot establish coverage; reserve
**not covered** for evidence that actually demonstrates that state. A zero fault
count only means no faults were observed by that source during that interval. It
does not prove that no DMA was attempted or that allowed requests were harmless.

A staged defensive assessment should:

1. Inventory present devices and topology using supported Windows PnP surfaces.
2. Collect read-only configuration and OS resource data within the collector's
   documented ownership; see [PCIe configuration access](pcie-devices.md).
3. Parse the OS-exposed ACPI advertisement with strict length/checksum checks.
4. Record KDP and other platform policy separately from live-unit evidence.
5. Correlate per-device scope and runtime coverage only where supported evidence
   exists; otherwise retain the gap as unknown.
6. Observe hot-plug, policy changes, and fault telemetry with timestamped
   baselines. A fault, identifier mismatch, or missing driver is evidence to
   investigate, not a standalone attribution of malicious intent.
7. Apply a launch policy only against a documented compatibility baseline,
   tested false-positive rate, user recovery path, and appeal process.

Related guidance: [defensive PCIe inventory and signal correlation](detection-and-forensics.md#defensive-anti-cheat-inventory-and-correlation),
[PCIe devices](pcie-devices.md), and [assurance boundaries](assurance-boundaries.md).

## Primary Contracts to Pin

- The applicable [ACPI Specification 6.5 software programming model](https://uefi.org/specs/ACPI/6.5/05_ACPI_Software_Programming_Model.html)
  for ACPI table identification and common conventions.
- The matching Intel VT-d Architecture Specification or AMD I/O Virtualization
  Technology Specification for vendor-specific DMAR/IVRS structures, registers,
  translation modes, scopes/selectors and faults. Pin the applicable revision;
  do not mix structure versions.
- Microsoft's [`GetSystemFirmwareTable` API documentation](https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemfirmwaretable),
  [`EnumSystemFirmwareTables`](https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-enumsystemfirmwaretables),
  [PCI configuration ownership guidance](https://learn.microsoft.com/en-us/windows-hardware/drivers/pci/accessing-pci-device-configuration-space),
  and [Kernel DMA Protection documentation](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)
  for the target Windows release.
