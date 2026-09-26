# Iommu And Defense

## IOMMU Architecture

### Translation Flow
```
1. Device issues a Memory TLP carrying an address; the transaction carries a
   16-bit Requester ID (Bus:Device:Function).
2. TLP travels upstream through switches/bridges toward the root complex.
3. When the applicable IOMMU path and translation mode require remapping, the
   unit uses requester/topology context to select a translation context.
4. In a translated context, the supplied address is interpreted as an IOVA and
   the unit walks the device's I/O page tables: IOVA → physical address.
5. Permissions are checked against the access type.
6. A permitted request is forwarded according to the platform's translation
   and routing mode; a denied request may produce a fault/event.

Do not assume every device Memory TLP is always translated, that an IOMMU
intercepts every path, or that an untranslated address is literally an IOVA
whose value happens to equal a physical address. Pass-through, untranslated,
identity-mapped, and remapped paths have different semantics; establish which
path applies to the device and platform under review.
```

### Intel VT-d Internals
```
Two-level table lookup:

BDF → Root Table (256 entries, 16B each, indexed by Bus)
    → Context Table (256 entries, 16B each, indexed by Dev:Func)
      → Second-Level Page Tables (3–5 levels)
        → Final 4 KB physical page

Context Entry fields:
- SLPTPTR: Second-Level Page Table Pointer
- Domain ID: 16-bit (multiple devices can share a domain)
- AW: Address Width (3/4/5-level = 39/48/57-bit IOVA)
- T: Translation Type (untranslated-only, translated-only, or both)
- P: Present
- FPD: Fault Processing Disable

Page table entries (PTE, EPT-like format):
[0]      R - Read permission
[1]      W - Write permission
[7]      PS - Page Size (1=leaf super-page, 0=next-level table)
[N-1:12] Physical address of next-level table or 4 KB page

Super-pages: level-2 leaf = 2 MB, level-3 leaf = 1 GB.

Scalable Mode (VT-d 3.0+):
Context Entry → PASID Directory → PASID Table → per-PASID
first-level page-table roots. Enables Shared Virtual Memory (SVM).
Check RTADDR_REG.TTM to determine which mode is in effect.
```

### AMD-Vi Internals
```
Single-level Device Table indexed directly by BDF:

BDF → Device Table Entry (32 bytes)
    → I/O Page Tables (1–6 levels)
      → Final page

DTE encodes:
- Page Table Root Pointer
- Mode (0–6, selects paging levels)
- Domain ID (16 bits)
- IR, IW — Default Read/Write permission
- GV — Guest Valid (nested translation)
- PASID-related fields

Page sizes: 4 KB, 2 MB, 1 GB.
```

### IOTLB and Invalidation
```
Translations cached in IOTLB (I/O Translation Lookaside Buffer).
When mappings change, IOTLB must be invalidated.

Two distinct caches when ATS is in use:
- IOMMU's own IOTLB
- Device-side TLB (DevTLB) caching prior translations

Full invalidation with ATS requires:
1. IOMMU invalidates own IOTLB
2. IOMMU sends ATS Invalidate Request Message to device
3. Device drops affected DevTLB entries, replies with Invalidate Completion

If step 2 or 3 is skipped, device retains stale translations
and can DMA to unmapped addresses.

VT-d invalidation granularities:
- Global: flush entire IOTLB
- Domain-Selective: flush all entries for a Domain ID
- Page-Selective: flush specific IOVA range in a domain

Strict vs lazy invalidation:
Lazy mode defers IOTLB invalidation, batching them for performance.
Opens a window where stale translations remain valid — a device
whose driver has unmapped a buffer can still DMA to the old IOVA.
```

### Fault Recording
```
VT-d: Fault Recording Registers — circular array capturing
  Requester ID, faulting IOVA, fault reason, TLP type.

AMD-Vi: Event Log Buffer — producer-consumer ring buffer of
  IO_PAGE_FAULT, INVALID_DEVICE_REQUEST, ATS-related events.

Both surface faults via interrupts and event-log entries.
On Windows, some IOMMU violations observable through WHEA/bug-check
paths and Driver Verifier DMA-violation telemetry.

Per-device fault rate is one of the most operationally useful
IOMMU-layer signals, but its baseline is platform-, device-, driver-, firmware-,
and workload-specific. Sustained faults show failed or invalid DMA requests;
driver bugs, resets, stale mappings, or hardware faults must be excluded before
attributing malicious out-of-domain access.

RMRR/IVMD:
DMAR RMRR and IVRS IVMD structures describe platform-reserved memory regions
and associated device scopes according to their respective specifications.
Validate them against the correct platform/OEM baseline. Do not automatically
reject a device because it appears in a reserved-region scope or infer malicious
access from an apparent range overlap; reserved-memory semantics and ownership
must be established for the target platform.
```

## IOMMU Topology and Isolation

### IOMMU Groups
```
Devices in the same IOMMU group may not be safely isolated from
one another. Group membership determined by:
- PCIe topology — devices behind a switch share a group
  unless the switch supports and enables ACS
- ACS state of upstream bridges
- Quirks for known-broken hardware

Linux: /sys/kernel/iommu_groups/N/devices/
Windows: equivalent constraints but no simple public group filesystem
```

### ACS (Access Control Services, Extended Cap ID 0x000D)
```
ACS is a PCIe capability that switches/root ports advertise
to declare they can enforce isolation between downstream ports.

ACS Capability register enable bits:
Bit  Feature                      Effect
0    Source Validation (SV)        Drop TLPs with wrong Requester ID
1    Translation Blocking (TB)    Block AT=10 (Translated) TLPs
2    P2P Request Redirect (RR)    Force P2P requests upstream for IOMMU
3    P2P Completion Redirect (CR) Force P2P completions upstream
4    Upstream Forwarding (UF)     Forward upstream regardless
5    P2P Egress Control (EC)      Allow/deny P2P routing per-port
6    Direct Translated P2P (DT)   Allow P2P with translated addresses

ACS capability and enabled-control state describe specific peer-routing and
requester-validation behaviors. Their security relevance depends on the complete
PCIe hierarchy, root-complex routing, platform policy and active IOMMU path; a
missing bit alone does not prove an exploitable bypass. Establish which controls
are required by the target deployment rather than applying a universal bitset.
```

### Peer-to-Peer DMA

PCIe peer-to-peer routing can keep some transactions below the root complex,
where the host IOMMU may not observe or translate them. Whether that path exists
and is isolated depends on the endpoint, every bridge, root-complex routing and
platform policy. Assess actual topology and owner-provided state; do not infer a
bypass from a card class or an ACS bit in isolation. Any containment policy must
be designed for the platform owner, not applied by a generic anti-cheat driver.

### Interrupt Remapping

Interrupt-remapping controls validate device interrupt messages under
platform-defined policy. Its absence can weaken interrupt isolation, but do not
infer that any bus-master device can cause an arbitrary interrupt: address
routing, platform support and message validation also matter. Record advertised,
configured and observed state separately; make requirements deployment-specific
and verify through the platform owner.

## ATS, PASID, and Address Translation Trust

### ATS (Address Translation Services, Extended Cap ID 0x000F)

ATS allows a capable endpoint to cache translations granted through the
platform's translation-request/invalidation protocol. Translated requests can
use a device-side translation cache, so mapping lifetime, invalidation and the
platform's ATS trust policy matter. Do not claim that the ATS capability or an
AT=10 request alone proves a bypass; establish whether ATS is enabled and
accepted for this requester, how invalidations are handled, and what the
applicable IOMMU/platform specification guarantees.

### PASID (Extended Cap ID 0x001B)

PASID can select process/address-space context when the device, OS, and IOMMU
are configured for the relevant shared-virtual-memory features. Presence alone
is not anomalous; assess the exact function, driver, platform support, and
runtime policy.

### ATS Trust and Policy

ATS security depends on platform policy, requester context, permitted
translation requests and correct invalidation behavior. Do not assume every
platform enables ATS, nor that KDP status establishes ATS policy for every
internal endpoint. Collect per-device ATS policy only through a supported
owner-provided interface; otherwise mark it unknown. See [IOMMU state
verification](iommu-state-verification.md) for the distinction between a
capability advertisement and live requester coverage.

## Driver–IOMMU Contract and Coverage Assessment

### OS-Managed DMA Contract (Conceptual)

In an intended OS-managed path, a device driver requests DMA mappings through
the platform's DMA subsystem; the OS/IOMMU establishes and tears down mappings
according to the device and platform policy. Isolation depends on remapping
being active for that requester, correct buffer bounds and lifetime, appropriate
invalidation, and trusted driver/OS behavior. Do not infer from this intended
contract that game memory can never be mapped, copied into an allowed buffer, or
exposed through a faulty driver. Use the target Windows/driver documentation and
runtime evidence for exact guarantees.

### Coverage Failure Classes

For a defensive threat model, consider whether remapping is absent or not
applied to a requester; whether pre-boot and runtime protections differ;
whether a domain or mapping is broader than the product policy permits; whether
buffer sizing, mapping lifetime or invalidation is faulty; whether sensitive
data is intentionally present in an allowed buffer; and whether firmware, the
kernel or hypervisor is outside the trust boundary. These are review categories,
not a prevalence ranking or an attribution checklist. Establish each path with
platform-specific evidence and benign alternatives.

### Failure-Mode Evidence

Do not present a generic bypass catalog or prevalence ranking as a current
threat assessment. Relate each suspected failure to the four separate properties
in [IOMMU state verification](iommu-state-verification.md): advertised firmware
table, Windows policy, live remapping-unit state, and requester coverage. Add
boot measurements, runtime fault evidence, ACS/ATS state or driver-mapping
analysis only when the source and scope are documented. A failed or unavailable
observation remains unknown; a finding is not an attribution of intent.

## Hypervisor-Level Defense

### EPT-Based Memory Protection

EPT supplies a processor-side guest-physical to host-physical translation and
permission boundary. A violation concerns an access governed by the active EPT
policy. IOMMU remapping supplies the separate device-to-memory boundary; an EPT
trap is not direct evidence of a PCIe DMA request.

A trusted hypervisor can own both policies, but verify each path independently.
Protection depends on correct region coverage, page lifetime, backing-memory
isolation, and trusted policy/configuration interfaces. A guest CPU permission
change alone establishes no device-DMA coverage. Hypervisor presence and effects
may be observable; operating outside the guest kernel does not imply invisibility.
[CPU, DMA, and hypervisor assurance](assurance-boundaries.md)

### VBS, HVCI, and VTL Split

VBS and memory integrity strengthen isolation of kernel code-integrity decisions.
They do not grant arbitrary third-party drivers a VTL 1 extension interface or
make every signed driver safe. Review documented integration and the effective
vulnerable-driver policy separately; blocklist coverage has limits.

Record platform support, configured policy, services actually running, and
compatibility evidence. Kernel DMA Protection does not require VBS, and per-device
DMA remapping can be enabled independently of the overall feature. Select an
explicit deployment baseline for the product instead of treating every security
feature as a universal requirement or its absence as misconduct.
[Feature and deployment boundaries](assurance-boundaries.md)

### SMM Considerations
```
System Management Mode (Ring -2) runs in SMRAM, isolated from
the OS. SMM CPU memory accesses are not mediated by the device IOMMU, but
accessible data still depends on platform protections, memory encryption,
firmware design, and virtualization context.

A vulnerable SMI handler = path to arbitrary memory access
without IOMMU mediation.

Mitigations:
- Intel Boot Guard / AMD Platform Secure Boot (firmware signatures)
- SMI Transfer Monitor (STM): hypervisor-resident, treats SMM as
  constrained guest; availability and deployment are platform-specific
- Runtime verification of SMM lockdown registers
```

### PCIe IDE (Integrity and Data Encryption)
```
IDE adds link-level TLP protection: integrity (MAC-based, required)
and confidentiality (encryption, optional).
Incorporated into PCIe 6.0 base specification.

Valuable against: physical link interposers, malicious retimers/switches,
traffic tampering.

NOT a DMA-cheat silver bullet: cheat installed as the endpoint
still originates legitimate IDE-protected TLPs after key establishment.
IDE raises the bar for passive bus sniffing but endpoint identity,
IOMMU policy, ACS topology, ATS policy, and attestation remain required.
```

## External Trust Anchors

### TPM Measurements and PCR Profiles

A TPM supports protected keys and measurement reporting. Record the actual TPM
implementation, PCR bank, platform profile, and selected measurements. PCR reset
and extend rules are profile-dependent; a universal extend-only table is
inaccurate. Resolve measurement meaning from the applicable profile and event
log, rather than assigning one fixed PCR layout to every system.

### Remote Attestation Evidence

Review key enrollment, verifier trust anchors, signature validity, expected
qualifying data, PCR selection/digest consistency, event-log consistency, and
the appraisal policy. An attestation key's trust chain depends on the enrollment
scheme; it does not automatically terminate at a TPM manufacturer certificate.

A valid quote supports the selected measurements under that trust model. It does
not establish the absence of a DMA-capable device or authenticate every current
IOMMU mapping. Separate accepted boot evidence, unsupported measurement coverage,
and verified runtime state in the report.

### DRTM and Secure Launch

Secure Launch uses DRTM during startup to establish a measured execution path.
Do not describe this as an arbitrary post-boot application launch or assume that
one PCR comparison verifies every security component. Record platform support,
launch state, applicable measurement profile, and appraisal policy.

### Pre-Boot DMA Evidence

Firmware's pre-boot isolation responsibilities and Windows runtime DMA policy
are distinct. Microsoft's OEM contract specifies a PCR 7 event when relevant
DMA protections are disabled or reduced. Interpret its presence or absence only
against the applicable contract and a trustworthy measurement/event-log path.
ACPI indicators describe platform capabilities and policy inputs, not a complete
snapshot of live IOMMU mappings.

Sources and verification limits: [attestation and platform contracts](assurance-boundaries.md).

## Layered Detection Pipeline

### Pre-Game Environmental Verification

Record supported, configured, and observed-running state separately for device
remapping, interrupt remapping, Secure Boot, VBS/memory integrity, and attestation.
Bind requirements to a documented product/platform policy. Assess firmware update
applicability and relevant topology; absence from a known-issue list is not proof
that firmware has no vulnerabilities. Unsupported or unavailable evidence should
remain explicit, with compatibility and recovery paths defined.

### PCIe Inventory Pass
```
- Enumerate all PCIe devices via PnP tree
- Supported configuration snapshot, recording readable span and missing fields
- Check device problem codes (DEVPKEY_Device_ProblemCode)
- Cross-reference SMBIOS slot inventory with populated devices
```

### Configuration Integrity Per Device
```
- VID/DID/SVID/SDID against known-good list
- Capability-chain walk and validation
- Signature-residue scan
- OS-reported BAR/resource consistency
- Configuration consistency from permitted observations
- Compare against per-donor reference database
```

### Behavioral Sampling During Play
```
- Periodic Link Status reads (LTSSM, ASPM transitions)
- AER counter snapshots
- Per-device interrupt rate and distribution
- Per-device IOMMU fault rate
- BAR-region content sampling for class consistency
```

### Statistical Analysis Over Session
```
- Latency distribution comparison (KS test, Hill estimator)
- Interrupt arrival distribution
- ASPM transition rate
```

### Cheat-Phase Detection
```
- Honeypot region access
- Memory access frequency / locality classifiers
```

### Containment Before Verdict
```
Each detection produces evidence, not a verdict.
Verdict informed by:
- Multi-signal correlation with measured joint error rates; correlated
  signals can share the same false-positive cause
- Server-side aggregation across sessions
- Behavioral verification (input timing, gameplay statistics)

Any authorized containment must use the established OS/platform owner and
verify its actual scope and completion. EPT CPU permissions and device DMA
isolation are different controls; neither implies a guaranteed real-time outcome.
```

Apply [`research-rigor`](../../research-rigor/SKILL.md) when converting these
signals into a claim or response. Validate baselines per device, firmware,
platform, topology, driver, and power state; preserve raw captures and test
benign alternatives before attribution.

### Realistic Limits

A passing identity or behavioral check establishes consistency only in the
observed dimensions. A denied DMA request establishes the enforced boundary
for that request; it does not classify every device or actor. A valid attestation
result covers its selected measurements and appraisal policy, not all current
memory access.

Choose complementary controls for independently identified trust gaps. External
attestation can support boot-state confidence but is not a universal solution to
unobserved runtime activity. Report coverage, missing evidence, shared failure
modes, and measured error rates instead of an evasion checklist or a claim that
one device class requires a particular detector.

Layered protection may increase attack cost; the magnitude and economic effect
remain deployment-specific claims requiring evidence.
