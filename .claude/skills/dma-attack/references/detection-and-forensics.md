# Detection And Forensics

## Defensive Anti-Cheat Inventory and Correlation

Treat this as a read-only evidence pipeline, not a single-device verdict. The
four layers describe different questions; a signal at one layer does not fill
gaps at another.

| Layer | Defensive question | Useful observations | Key limit |
|---|---|---|---|
| **L1 — identity/topology** | Which PCIe functions does the OS enumerate, and where are they in the PnP tree? | Device/compatible IDs, class, parent/child path, status, OS-assigned resources | IDs are device claims; OS enumeration may not expose every physical path |
| **L2 — capability** | Could the function initiate transactions, and what resources/capabilities does it advertise? | Read-only Command/BME snapshot, BAR resource description, validated capability chain | Bus Master Enable is permission, not proof of DMA capability in use or a crime |
| **L3 — consistency** | Do identity, function, driver binding, status, resources, and behavior fit a matched device baseline? | Correlated PnP/configuration observations, driver/service metadata, documented device behavior | A mismatch needs platform and driver context; heuristics can share false-positive causes |
| **L4 — IOMMU assurance** | Is protection advertised, enabled by policy, active, and applicable to this requester? | Separate ACPI, Windows policy, live-unit, requester-scope and runtime evidence | One layer does not prove the next; see [IOMMU state verification](iommu-state-verification.md) |

### Collection boundaries

- Use SetupAPI/Configuration Manager device properties for user-mode PnP inventory
  and supported, ownership-appropriate PCI/bus interfaces for kernel observation.
  Windows documents `BUS_INTERFACE_STANDARD` and `IRP_MN_READ_CONFIG` for
  configuration access ([Microsoft guidance](https://learn.microsoft.com/en-us/windows-hardware/drivers/pci/accessing-pci-device-configuration-space));
  this does not grant generic write authority. Configuration
  snapshots may be partial; record readable spans and errors, not zero-filled data.
- Treat an OS-enumerated PnP tree as the scope of that collector, not proof that
  no other physical endpoint exists. For VMD, follow the Windows-exposed parent/
  child topology and its owner driver. Do not assume fixed offsets in a VMD BAR,
  walk undocumented `pci.sys` structures, or map a BAR as a generic way to probe
  downstream configuration windows.
- Read OS-reported BAR/resource assignments; do not rewrite BARs or use the
  sizing-probe write of all ones against a live device. Device-specific BAR
  contents require documented ownership and register semantics; they are not a
  default anti-cheat collection method.
- BME set means the function is permitted to initiate bus-master transactions
  under the current configuration. NICs, NVMe, GPUs and other legitimate devices
  commonly need it. Interpret it with class, driver, topology, policy and other
  evidence—not as an accusation or proof of active memory reads.
- A missing service, unexpected service name, non-running service, or PnP problem
  code is context, not a universal `nosrv`/`wrongsrv` rule. Function/class,
  driver model, device start state, shared services and Windows build all matter.
  Do not reuse sample-specific magic status values or label a device `fakesrv`
  from one ID/name pair alone.
- Vendor/device/subsystem IDs, class and capability lists can be emulated or
  legitimately vary by revision, firmware, topology and driver. Maintain any
  risk/allowlist with exact device/driver/firmware baselines, provenance and
  review date; use it for triage until false-positive behavior is measured.
- Compare sources only when they are genuinely independent. Two APIs may both
  report the same bus-driver cache; a raw ECAM/MMIO read is not automatically an
  independent or supported observation. Do not infer hiding from a blank read,
  alternating DWORD pattern, one-device count, or mismatch without excluding
  power state, access limits, topology, virtualization and collector failure.

### Decision and telemetry

Store each observation with its API/collector, timestamp, OS build, device path,
readable span, error status and baseline version. Keep `present`, `absent`,
`conflicting` and `unknown` distinct. Unknown is not a pass, but neither is it
proof of tampering. Correlate layers, validate joint false-positive rates on
representative benign systems, start with telemetry, and enforce only a
published platform baseline with compatibility handling, recovery and appeal.
A finding can justify investigation; it does not by itself establish malicious
intent or identify the memory requester.

## Detection at the PCIe Layer

### Configuration Integrity

Use supported, permitted observations of device identity, capability structure,
OS-assigned resources, and advertised functions. Compare with the exact device
contract and a matched baseline; document unavailable or inaccessible fields.
Collection should not modify another driver's configuration registers.

### BAR and Register Evidence

Distinguish OS-reported BAR resources from device-specific register contents.
A zero or unexpected value may reflect reset, power state, a missing driver,
unsupported functionality, or collector scope. Establish register semantics and
which actor owns access before interpreting it as a conformance failure.

### Configuration Ownership and Consistency

Assess consistency from existing traces, device documentation, owned-source
review, and documented platform interfaces. Windows retains control of PCI
headers and capabilities. A generic collector is not entitled to toggle bus
mastering, payload size, MSI state, or reserved bits to classify live devices.
Any separately designed device validation must respect the owning driver and
platform lifecycle. See [configuration and containment boundaries](assurance-boundaries.md).

### Link and ASPM Evidence

Use only owner-appropriate, read-only link observations. Negotiated width/speed
and DLL-active state are snapshots; they do not provide a complete LTSSM trace.
Compare negotiated values with slot wiring, root-port limits, signal quality,
power state and matched device baselines. A device may legitimately train below
its advertised maximum.

ASPM capability does not mean the platform enabled ASPM. Evaluate L0/L1 or
L1-substate behavior only when firmware/OS policy, the link partner and workload
are known to exercise it, and the collector can actually observe transitions.
A missing transition or unexpected latency is a contextual anomaly, not proof of
emulation; Link Status polling alone can miss transitions.

### AER Baselining

Treat Advanced Error Reporting as component-local telemetry. A zero counter may
mean no error was logged, the capability/counter is unavailable, or the observer
cannot read it; do not flag a "too clean" device without a controlled, matched
baseline. Correlate error status, valid-header indicators, logging component,
link/topology and workload. Do not generate malformed configuration or TLP
probes as a generic anti-cheat fingerprinting method.

### Completion Latency (Lab Instrumentation Only)

Windows does not provide a generic per-device API for measuring PCIe DMA TLP
completion timing. A protocol trace or owner-supported counter measures only its
specific path; observed latency also includes memory, arbitration, buffering,
power state, link, driver and workload effects. It is not a portable endpoint
fingerprint.

For a controlled lab comparison, select distribution tests only after defining
the capture point, sample size and matched device/workload population. Validate
thresholds on held-out systems and report uncertainty; mean, tails, modes and
autocorrelation can all vary legitimately. Do not infer emulation from low
variance or use software-request latency as a proxy for an unseen DMA TLP.

### MSI/MSI-X Behavioral Validation

Use OS interrupt accounting, ETW/performance telemetry or owner-driver counters
within their documented scope. Interpret a low or zero count only after confirming
the device is started, the relevant vector is enabled/unmasked, the workload
should interrupt, and the collector observes that vector. Polling, power state,
shared-vector behavior and telemetry loss are benign alternatives. Arrival-time
patterns require a matched workload baseline and are not standalone device
identity evidence.

### Device-Access Pattern Evidence

Access periodicity or address-range breadth is usable only when the collector
actually observes device requests through a validated platform or protocol
instrumentation path. Such patterns also arise from legitimate workload and
buffering behavior; validate metrics against matched benign systems before use.
An EPT event records processor access under the active EPT policy, not device
DMA. Device DMA needs separate remapping/fault or protocol evidence, and server
events have their own application semantics. Do not attribute one collector's
event to another layer.

### Hot-Plug and Link Disruption Events

Device resets and link interruptions can produce telemetry, but also have benign
causes. Use supported PnP notifications and owner-appropriate link/error sources.
A Surprise Down, hot-plug status change, retraining cycle, or re-enumeration with
changed configuration is an anomaly to correlate, not a unique fingerprint of
firmware reload or cheating. Preserve event order, device path, error source and
plausible alternatives; do not write slot-status or link-control registers as a
generic collector.

## Detection at the IOMMU Layer

### Fault-Rate Monitoring

Use OS/platform-supported fault events where available; there is no generic
anti-cheat interface that exposes every VT-d or AMD-Vi hardware log. Record the
source, requester-identity mapping, interval, dropped-event semantics and
collection errors. A fault is evidence of a denied/failed request within that
logging path, not proof of malicious intent. A zero count is not proof that no
request occurred. Do not directly map, clear or reprogram IOMMU registers as a
monitoring method. See [IOMMU state verification](iommu-state-verification.md).

### Domain Assignment Audit

Audit assignments only through a trusted platform/OS interface that documents
what it exposes. Preserve requester, domain/mode, policy, timestamp and coverage
limits; unavailable state is **unknown**, not an empty or safe assignment.
Passthrough/identity domains, shared domain IDs or large isolation groups are
not universal misconduct signals. Compare them with the documented platform and
deployment policy, and assess ACS/topology separately.

### ACS Topology Verification

Where an owner-appropriate source exposes ACS capability/control state, record
it along the complete endpoint-to-root path. Missing or disabled ACS can limit
isolation where peer routing is possible, but a capability bit alone does not
establish actual routing or an exploitable path. Assess topology, root-complex
behavior, firmware policy and the effective IOMMU path before drawing a finding;
do not assume one universal ACS bitset is required on every platform.

### IOMMU as Containment Primitive

Containment is a platform/driver responsibility. Record the authorized policy
owner, affected device hierarchy, existing mappings, in-flight work, recovery
path, and evidence that the requested isolation completed. Remapping, bus-master
state, and downstream-port containment have different prerequisites and scope;
none has an effectiveness guarantee derived from a firmware tier.

Use supported OS-managed device lifecycle and isolation controls. Do not instruct
a generic game-security driver to rewrite another device's PCI configuration or
IOMMU ownership. Preserve evidence and evaluate availability impact before an
authorized response; restriction is separate from misconduct attribution.
[Platform ownership and containment](assurance-boundaries.md)

## Forensic Evidence Capture

### What to Capture
```
Artifact                     Source                          Purpose
──────────────────────────────────────────────────────────────────────────────
Supported config snapshot    OS PCI interface                Device identity and collection scope
Capability chain walk        Parsed from config              Capability presence
PCIe link state history      Link Status over session        LTSSM anomaly evidence
MSI/MSI-X arrival timeline   OS interrupt telemetry          Rate claim refutation
AER error events             Owner-approved AER telemetry   Matched baseline and source context
IOMMU fault events           OS/platform source, if exposed Denied/failed-request evidence within source scope
IOMMU assignment status     Platform/OS API, if available   Coverage within documented scope; else unknown
ACS bridge state             Bridge enumeration              Isolation assessment
Protected-page CPU event    Hypervisor EPT event evidence   CPU access-policy observation
Device DMA fault evidence    Platform/IOMMU collector        Device request-policy observation
TPM quote and measurement log Attestation provider           Selected-measurement appraisal
MCFG / DMAR / IVRS tables   ACPI subsystem                  Platform config baseline
Slot/topology context       PnP + firmware data, if exposed Topology context, not completeness proof
Firmware identity/version   OS/vendor inventory             Compare with applicable advisory; not proof of fix
Latency-distribution hists   Per-session sampling            Statistical fingerprint
```

### Multi-Signal Correlation
```
Strongest evidence packages combine:
1. Hardware-layer signal (config space, BAR, link state)
2. Behavioral-layer signal (interrupt distribution, IOMMU fault rate, honeypot)
3. Temporal correlation (hardware signal preceded behavioral by plausible interval)

No signal count guarantees a target false-positive rate. Establish independence
or model dependence, validate the joint decision rule on representative benign
systems, and report confidence bounds plus expected appeal volume.
```

### PCIe Protocol Captures
```
A PCIe protocol analyzer can provide detailed evidence at its observation
point, subject to its configuration, capture filters, buffers, and timestamp
accuracy. Do not assume a given analyzer captures every TLP, DLLP, or ordered set.
A trace can support reproduction only for the captured path and conditions;
record analyzer model, configuration, topology and dropped-capture indicators.

Cost and deployment complexity limit routine use. For high-impact cases,
protocol-level captures from an independent lab can materially strengthen the
record, but capture coverage, analyzer configuration, and interpretation still
need validation.
```

## External PCIe DMA: Thunderbolt and USB4

A connector or protocol label does not by itself prove that a port supports
PCIe tunneling; capability and authorization depend on the platform, port,
firmware and attached device. Runtime hot-plug policy and pre-boot DMA protection
are separate responsibilities. Assess the target's documented platform policy
and actual PnP/remapping evidence rather than assuming a universal security-level
mapping or that a device could DMA before Windows starts.

Thunderclap-class research demonstrated specific weaknesses in device/driver
DMA isolation and buffer handling; it should not be summarized as a universal
IOMMU bypass. Windows Kernel DMA Protection provides policy-controlled
protection on supported systems, but its status does not establish coverage of
every internal endpoint. Check the exact Windows, firmware, port and device/driver
conditions in [Microsoft's KDP documentation](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)
and [IOMMU state verification](iommu-state-verification.md).

## CPU Page-Table and Hypervisor Boundary

CR3, CPU page-table and EPT/TLB observations concern processor address
translation; they are not evidence that a PCIe endpoint initiated DMA. A CPU
translation event must not be attributed to a device without separate requester
and IOMMU/protocol evidence. Generic TLB flushing or re-walking is not a proof of
page-table integrity and does not establish device-DMA coverage. Route host
kernel/hypervisor manipulation to [windows-kernel-security](../../windows-kernel/SKILL.md)
and assess CPU and device isolation as separate controls.

## External Memory-Acquisition Boundary

A PCIe endpoint can initiate memory transactions without a host process issuing
an ordinary CPU read on its behalf. Whether those transactions reach system
memory depends on topology, platform routing and the active IOMMU policy for the
requester. A host process/module scan therefore cannot establish that no device
initiated DMA; a PCIe inventory or IOMMU status flag likewise does not prove
that game memory was read.

For defensive analysis, establish the claimed source, transport, analysis host,
requester identity and applicable remapping evidence separately. Prefer
OS/platform fault telemetry, authorized protocol captures, measured machine
state and matched device baselines. Preserve the collector's coverage and
limitations. Do not turn this section into a physical-memory acquisition,
page-table-walking or device-control recipe; use [acquisition and transport](acquisition-and-transport.md)
for architecture classification and [IOMMU state verification](iommu-state-verification.md)
for the boundary evidence.

## Defensive Test Safety

Run hardware-facing validation only on authorized, isolated test systems with a
recovery path. Prefer passive/read-only collection and preserve raw observations.
Do not alter another driver's PCI configuration, BARs, IOMMU state or page
tables as part of generic anti-cheat detection. Separate a protection-policy
failure from misconduct attribution, and document the system state that could
not be observed.
