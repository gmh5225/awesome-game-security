# Pcie Devices

## PCIe Protocol Stack

### Three Protocol Layers
```
Layer              Unit                Function
────────────────────────────────────────────────────────────────
Transaction        TLP                 Memory/IO/Config reads & writes,
                                       completions, messages
Data Link          DLLP                Acknowledgements, flow control
                                       credits, power management
Physical           Ordered Sets        Link training, equalization,
                                       clock recovery

A real device's behavior is shaped by all three layers.
Many FPGA designs primarily customize Transaction-Layer behavior; Physical and
Data Link behavior may retain implementation fingerprints unless the selected
IP, configuration, and surrounding behavior closely match the claimed device.
Whether a fingerprint is usable must be validated on the actual link.
```

### TLP (Transaction Layer Packet) Format
```
Every TLP contains a 3 DW (12-byte) or 4 DW (16-byte) base header; optional
TLP Prefixes may precede it. 4 DW headers are used for 64-bit addresses and
certain message types.

First DWord (DW0) encoding:
Bits       Field         Notes
[31:29]    Fmt[2:0]      Header format + data presence
[28:24]    Type[4:0]     TLP type (combined with Fmt)
[22:20]    TC[2:0]       Traffic Class (default 0)
[18]       Attr[2]       ID-Based Ordering (IDO)
[15]       TD            TLP Digest (ECRC trailer)
[14]       EP            Poisoned data
[13:12]    Attr[1:0]     Relaxed Ordering, No Snoop
[11:10]    AT[1:0]       Address Type (critical for ATS bypass)
[9:0]      Length[9:0]   Payload length in DWords (0x000 = 1024 DW = 4 KB)

Fmt[2:0] encoding:
000 = 3 DW header, no data
001 = 4 DW header, no data
010 = 3 DW header, with data
011 = 4 DW header, with data
100 = TLP Prefix

Key TLP types (Fmt + Type combinations):
Fmt  Type     TLP
000  0_0000   MRd (Memory Read, 3DW / 32-bit addr)
001  0_0000   MRd (Memory Read, 4DW / 64-bit addr)
010  0_0000   MWr (Memory Write, 3DW)
011  0_0000   MWr (Memory Write, 4DW)
000  0_0100   CfgRd0 (Config read — terminate at this device)
010  0_0100   CfgWr0
000  0_0101   CfgRd1 (Config read — forwarded by bridges)
010  0_0101   CfgWr1
000  0_1010   Cpl (Completion without data)
010  0_1010   CplD (Completion with data)
001  1_0rrr   Msg (Message, no data)
011  1_0rrr   MsgD (Message with data)
```

### Detection-Relevant DW0 Fields
```
TC[2:0] — Traffic Class. Default traffic commonly uses TC0, but non-zero TC is
valid when platform and device policy configure it. Compare usage with the
claimed device, driver, and workload rather than flagging it in isolation.

Attr[2:0] — Relaxed Ordering, No Snoop and ID-Based Ordering policy bits.
Interpret them against the PCIe version, device/driver contract and workload;
one traffic pattern is not a universal device-identity test.

AT[1:0] — Address Type:
  00 = Untranslated (translation depends on the applicable IOMMU path/policy)
  01 = Translation Request (ATS only)
  10 = Translated (used under applicable ATS/platform policy)
AT state must be interpreted with the requester context and IOMMU policy; it is
not by itself evidence of a bypass. See the ATS trust/policy discussion in
`iommu-and-defense.md`.

TD — TLP Digest. If set, an ECRC trailer is present.
EP — Poisoned. Indicates data is known-bad.
```

### TLP Routing and Requester ID
```
Three routing modes:
- Address routing — Memory and IO TLPs, matched against bridge apertures
- ID routing — Config TLPs and Completions, by BDF
- Implicit routing — Some Messages (broadcast, terminate at root)

DW1 carries the Requester ID (16 bits = Bus:Device:Function, "BDF")
and an 8-bit Tag for matching completions to requests.

Requester ID is a key input to IOMMU lookup, ACS source validation, AER source
identification, and interrupt-remapping policy. If spoofed IDs are accepted
without topology or source validation, per-function isolation can be
undermined; the exact effect depends on the platform and remapping path.

Transaction categories:
- Posted (P) — fire-and-forget (Memory Writes, Messages)
- Non-Posted (NP) — requires completion (Memory Reads, IO/Config R/W)
- Completion (Cpl/CplD) — response to Non-Posted requests

Completion Status codes:
000 = Successful Completion (SC)
001 = Unsupported Request (UR)
010 = Configuration Request Retry Status (CRS)
100 = Completer Abort (CA)

UR and CA are distinct completion statuses, but observed behavior depends on
request type, topology and device contract. Do not issue malformed requests or
probe unimplemented offsets as a generic anti-cheat test; compare only supported,
passively observed responses with a matched, versioned reference.
```

### Memory Read Completion Splitting
```
A Memory Read request is bounded by its requested size; the completer returns
one or more Completion-with-Data packets subject to the PCIe rules, Read
Completion Boundary (RCB) and payload limits. Completion headers carry Lower
Address[6:0], Byte Count[11:0] and Tag fields used to associate responses with
the request. Exact behavior depends on the applicable PCIe revision and link
configuration.

A captured split/latency pattern reflects the completer, root complex, memory,
link, power state and capture point as well as workload. It is not by itself a
fingerprint of the requesting endpoint or its FPGA implementation. Use it only
in a controlled, matched protocol-analysis study with the observation path
explicitly identified.
```

### Tags and Outstanding Requests
```
PCIe uses requester tags to match non-posted requests with completions. The
original 5-bit tag space supports up to 32 outstanding requests; Extended Tag
and 10-Bit Tag capabilities can increase that limit when supported and enabled.
Exact limits depend on specification revision, endpoint capability and active
controls. A tag sequence describes one implementation under one workload; it
is not a portable fingerprint. Do not infer identity or misuse from tag order
alone; preserve the capture point and matched baseline.
```

### MPS and MRRS Evidence
```
Record advertised and configured values separately, with the platform software
and topology. In the PCIe Express capability, Max_Payload_Size_Supported is in
Device Capabilities[2:0], configured MPS is in Device Control[7:5], and MRRS is
in Device Control[14:12]. The common size encodings are 0=128, 1=256, 2=512,
3=1024, 4=2048 and 5=4096 bytes; reserved values and supported maxima are
revision-dependent. MPS must not exceed the function's supported maximum, and
the chosen value is subject to platform policy and path constraints. MRRS is a
separate request-size setting. Do not infer a spoof from one value or infer
active behavior solely from capability bits; compare the exact device revision
with a matched root-port/workload baseline.
```

### Data Link Layer
```
DLLPs provide reliable delivery between Physical and Transaction layers.

DLLP          Purpose
─────────────────────────────────────────
Ack           TLP received correctly
Nak           TLP received with error; sender must replay
InitFC1/2     Flow control credit initialization at link bring-up
UpdateFC      Ongoing flow control credit updates
PM_*          Power management (L0s, L1 entry/exit)
Vendor        Vendor-defined

Flow control credits are per TLP category:
- PH / PD — Posted Header / Data
- NPH / NPD — Non-Posted Header / Data
- CplH / CplD — Completion Header / Data

Negotiated credit values are not generally exposed through standard
Link Capabilities register. They are visible in protocol-level traces,
some root-port/vendor performance counters, or FPGA-side debug.
Useful for lab fingerprinting and forensic captures, not normal
runtime config-space detection.
```

### Physical Layer
```
Two details matter even without PHY-level instrumentation:

LTSSM (Link Training and Status State Machine):
- States: Detect → Polling → Configuration → L0 (operational)
  → L0s, L1, L2 (low-power) → Recovery → Hot Reset → Disabled → Loopback
- Observable via Link Status Register and root-port performance counters

Detection-relevant:
- Negotiated Link Width (Link Status[9:4]):
  Compare with slot wiring, platform policy, signal quality, and matched donor
  deployments; devices can legitimately train below maximum width
- Current Link Speed (Link Status[3:0]):
  A lower negotiated generation is contextual, not a contradiction by itself
- Recovery cycle frequency:
  Comparative signal; materially different from donor reference is anomalous

ASPM (Active State Power Management):
- L0s and L1 are link-level low-power states
- Capability does not imply the platform enabled ASPM; evaluate transitions only
  under verified policy and workload conditions that should exercise them
```

### Configuration Access Mechanisms

Host-issued PCI configuration transactions are distinct from endpoint-issued
Memory TLPs and are not evidence that device DMA is enabled or covered by an
IOMMU. The host can enumerate and inspect a function even when DMA remapping is
disabled; a configuration snapshot also does not show whether the endpoint
actually issued memory requests. Windows retains ownership of configuration
state; use supported observations only.

```
Two mechanisms on x86:

CAM (Legacy I/O-port path):
1. CPU writes to I/O port 0xCF8 (Bus:Device:Function:Register)
2. CPU reads/writes at I/O port 0xCFC
- Reaches only first 256 bytes
- Still used during early BIOS/UEFI boot

ECAM (Enhanced, MMIO path):
1. Read MCFG ACPI table for segment base addresses
2. Compute: addr = base + ((bus << 20) | (dev << 15) | (func << 12) | offset)
3. OS maps physical address into kernel virtual memory
- Required for Extended Configuration Space (0x100–0xFFF)
- Where AER, DSN, LTR, VSEC, ATS, PASID, SR-IOV live

On Windows, supported paths are:
- IRP_MN_READ_CONFIG / IRP_MN_WRITE_CONFIG
- BUS_INTERFACE_STANDARD.GetBusData / SetBusData
Use documented bus interfaces within the caller's permitted ownership scope.
CAM/ECAM describes hardware access mechanisms, not permission for a generic
Windows collector to use raw I/O ports or map configuration apertures. Direct
MCFG mapping is not a supported substitute for the Windows PCI stack; OS
ownership of headers and capabilities still applies.
```

For Windows access rules, see [Microsoft's PCI configuration-space guidance](https://learn.microsoft.com/en-us/windows-hardware/drivers/pci/accessing-pci-device-configuration-space).

## PCIe Configuration Space

### Legacy 256-Byte Header (Type 0 Endpoint)
```
Offset  Field                    Notes
0x00    Vendor ID (2B)           Chip manufacturer (e.g., 0x8086 Intel)
0x02    Device ID (2B)           Specific product
0x04    Command (2B)             BME (bit 2), MemSpace (bit 1), IOSpace (bit 0)
0x06    Status (2B)              Capabilities List (bit 4)
0x08    Revision ID + Class Code Class triplet: Base / Sub / ProgIF
0x0C    Cache Line / Latency /   Header Type 0x00 = endpoint,
        Header Type / BIST       0x01 = bridge, 0x80 = multi-function
0x10–27 BAR0–BAR5               Memory or I/O windows
0x2C    Subsystem Vendor ID      Often distinguishes board manufacturers
0x2E    Subsystem Device ID
0x30–33 Expansion ROM Base
0x34    Capabilities Pointer     Offset of first capability in linked list
0x3C    IRQ Line/Pin/Min/Max     Legacy INTx routing

BAR encoding (32-bit BAR):
bit 0:    0 = Memory BAR, 1 = I/O BAR
bits 2:1: 00 = 32-bit, 10 = 64-bit (BAR pair)
bit 3:    Prefetchable

BAR sizing belongs to platform enumeration and resource management.
For a collector, compare OS-reported resources with the exact device contract;
do not rewrite a live device's BARs. A size discrepancy requires context about
the device revision, active function, firmware, and collection method.
```

### Capabilities Chain
```
If Status[4] is set, 0x34 points to the first capability.
Each capability has a 2-byte header: [ID | Next].
Next is DWord-aligned in 0x40–0xFF, or 0x00 to terminate.

Common capability IDs:
ID    Capability
0x01  PCI Power Management
0x05  MSI
0x10  PCI Express
0x11  MSI-X
0x12  SATA Configuration
0x13  PCI Advanced Features
0x14  Enhanced Allocation

For a read-only parser, check that each next pointer is aligned, in bounds and
not cyclic, and validate the minimum layout for known capability IDs against the
applicable specification. Standard capability headers do not contain a generic
"declared size" field; do not guess unknown capability lengths. A malformed or
truncated read is a signal to review the collector and device, not proof of
spoofing by itself.
```

### PCIe Express Capability (ID 0x10)
```
A useful source of read-only capability and negotiated-link observations.

Offset  Field                    Notes
+0x02   PCIe Capabilities        Cap Version, Device/Port Type, Slot Impl
+0x04   Device Capabilities      MPS Supported, FLR, Phantom Functions
+0x08   Device Control           MPS current, MRRS, Error Enables
+0x0A   Device Status            CED, NFED, FED, URD, Transactions Pending
+0x0C   Link Capabilities        Max Link Speed/Width, ASPM, L0s/L1 latencies
+0x10   Link Control             ASPM Control, RCB, Link Disable, Retrain
+0x12   Link Status              Current Link Speed/Width, Link Training
+0x24   Device Capabilities 2    Completion Timeout Ranges, AtomicOp,
                                 OBFF, LTR mechanism
+0x28   Device Control 2         Completion Timeout Value, AtomicOp, LTR Enable
+0x2C   Link Capabilities 2      Supported Link Speeds Vector
+0x30   Link Control 2           Target Link Speed, Compliance
+0x32   Link Status 2            De-emphasis, EQ Phase status

Read-only comparison points:
- Device/port type and class should fit the claimed function and topology.
- Advertised capability ceilings and OS-configured values should be interpreted
  against the exact device revision and root-port constraints.
- Link Status reflects negotiated state; compare with slot wiring, platform
  policy, power state and a matched device baseline.
- Slot-clock, completion-timeout and AtomicOp fields are version- and
  platform-dependent; treat discrepancies as leads, not standalone proof.

Do not trigger FLR, alter completion controls or issue unsupported operations as
a generic anti-cheat probe. Device-specific conformance tests belong in an
authorized lab under the owning driver's lifecycle.
```

### MSI and MSI-X Capabilities
```
MSI (ID 0x05):
Message Control bits:
  [0]    MSI Enable
  [3:1]  Multiple Message Capable (0–5, representing 1–32 vectors)
  [6:4]  Multiple Message Enable (cannot exceed Capable)
  [7]    64-bit Address Capable
  [8]    Per-Vector Masking Capable

x86 MSI Address: bits [31:20] fixed at 0xFEE (LAPIC prefix)
  [19:12] Destination ID, [3] Redirection Hint, [2] Destination Mode
Message Data: [15] Trigger Mode, [10:8] Delivery Mode, [7:0] Vector

MSI-X (ID 0x11):
- Supports up to 2,048 vectors
- Table stored in BAR-mapped region (not Config Space)
- Each entry: 16 bytes (Addr Low, Addr High, Data, Vector Control)
- PBA (Pending Bit Array): bit-per-vector pending state

MSI-X masking, pending state and interrupt delivery are stateful and owned by
the device/driver lifecycle. Do not mask a live vector or induce an interrupt as
a generic anti-cheat probe. Prefer OS/driver interrupt telemetry and read-only
state available through an authorized owner. Any behavior test should be limited
to an isolated lab with the device owner's participation and a recovery path.
```

### AER Extended Capability (ID 0x0001)
```
Three error classes:
- Correctable: Receiver Error, Bad TLP, Bad DLLP, Replay Timer Timeout
- Uncorrectable Non-Fatal: Completion Timeout, Completer Abort, UR, ACS Violation
- Uncorrectable Fatal: Malformed TLP, DLL Protocol Error, Surprise Down

Each has Status (sticky, W1C), Mask, and Severity registers.
Header Log (16B) captures full TLP header of first logged uncorrectable error.

Interpret capability availability and counters against the exact device,
firmware, link and collection source. A zero error count means only that no error
was observed by that source during the interval; it is not identity evidence.
Status registers may be write-one-to-clear and belong to the device/platform
owner—do not write them or probe malformed offsets as a generic collector.
```

### Extended Capabilities
```
4-byte header at each offset:
[31:20] Next Capability Offset (0 to terminate)
[19:16] Capability Version
[15:0]  Extended Capability ID

Key Extended Capability IDs:
0x0001  AER
0x0002  Virtual Channel (VC)
0x0003  DSN (Device Serial Number, 8 bytes)
0x000B  Vendor-Specific Extended Capability (VSEC)
0x000D  ACS (Access Control Services)
0x000E  ARI
0x000F  ATS (Address Translation Services)
0x0010  SR-IOV
0x0015  Resizable BAR (RBAR)
0x0018  LTR (Latency Tolerance Reporting)
0x001B  PASID
0x001D  DPC (Downstream Port Containment)
0x001E  L1 PM Substates
0x001F  Precision Time Measurement (PTM)

Treat DSN, VSEC, ATS, PASID and SR-IOV fields as device claims to compare with
an exact specification and matched baseline. A DSN is not an authentication
credential; capability presence or absence alone does not establish spoofing,
malice, or DMA coverage. Consumer/server-class expectations need a current,
versioned device reference rather than a demographic assumption.
```

## FPGA and Device-Emulation Considerations

An FPGA endpoint can implement configurable PCIe functions, but its observed
behavior depends on the board, PCIe hard IP, firmware, platform and driver. A
field that differs from a claimed device's matched baseline can justify review;
it does not identify an FPGA or prove malicious use. Conversely, a self-consistent
configuration snapshot does not authenticate silicon or prove IOMMU coverage.

Treat the claimed identity, capability list, OS-assigned resources, link state,
interrupt telemetry and driver behavior as separate evidence. Compare only with
versioned, device-specific references under matched topology and workload. A
vendor ID, BAR pattern, FPGA model, timing statistic or absence of a PCIe child
in a software slot inventory is not a universal detector. Physical-slot and
SMBIOS inventories can be incomplete; retain collector scope and alternatives.

This reference intentionally omits FPGA build, resource-sizing, firmware
synthesis and register-emulation instructions. For source classification, see
[acquisition and transport](acquisition-and-transport.md); for read-only
observations and ownership boundaries, see [detection and forensics](detection-and-forensics.md).

## Acquisition and Analysis Tools

### Component Roles

PCILeech, LeechCore, MemProcFS and related projects occupy different roles in
hardware acquisition, host-mediated acquisition, transport and analysis. A
project name, loaded module, library filename or mounted analysis view does not
prove which memory source is active. Establish component provenance and the
active backend separately; see [acquisition and transport](acquisition-and-transport.md).

### Device-Side Observation Limits

An FPGA design may use a PCIe hard IP block and custom endpoint logic. Public
reference configurations can have version-specific identity, capability,
resource or behavior differences, but those are leads—not portable signatures.
Do not infer the active bitstream from a filename or assume a generic BAR probe
is safe. Compare read-only, OS-reported configuration/resources and documented
link/driver behavior with a versioned baseline; never modify another device to
classify it.

### Host-Side Analysis Layer

Memory-analysis interfaces are downstream of acquisition. A filesystem view,
process listing or analysis API does not identify whether its input came from a
PCIe endpoint, host driver, hypervisor, transport peer or offline image. Record
source provenance, privileges, transfer path, missing data and analysis version;
do not infer DMA from the tool name or its output format.

### Reference-Firmware Evidence

A public reference bitstream may leave implementation-specific identity or
behavior that is useful for a version-pinned lab comparison. Such observations
must be tied to an exact source/build and matched platform. Do not turn one
reference's identifiers, capability omissions, timing or BAR behavior into a
universal blacklist, and do not use active BAR/register probes on a live device.

## Emulated Configuration: Defensive Interpretation

A programmable endpoint may expose configuration values through its PCIe hard
IP or an emulated configuration view. Both paths can present self-consistent
identifiers and capabilities; configuration reads alone cannot authenticate the
physical device or prove that its DMA is remapped. Compare identity, class,
capability chain, OS-assigned resources, driver binding and observed behavior
against a versioned, matched device baseline. Keep any inconsistency as a
triage signal with benign explanations, not a proof of spoofing.

Do not use undocumented offsets, raw ECAM/MMIO access or private bus-driver
structures as an assumed independent source. Use documented, ownership-appropriate
configuration observations; compare a second source only when its provenance is
actually independent. See [defensive inventory boundaries](detection-and-forensics.md#defensive-anti-cheat-inventory-and-correlation).

PCI configuration and capability registers have different ownership and
side-effect semantics. Writes to Command/BME, BAR, MSI/MSI-X, reset, status or
write-one-to-clear fields can disrupt devices, lose evidence or conflict with
Windows. A generic anti-cheat must not toggle these fields to test whether an
endpoint is emulated. Use passive, OS-mediated observations; any active
conformance test must be an explicitly authorized device-owner lab test with
isolation and recovery. See [configuration and containment boundaries](assurance-boundaries.md).

### Claimed Device Identity and Baselines

Compare the claimed device with provenance-backed inventory and a matched
reference: exact SKU, function, firmware, driver, topology, and power/workload
state. Multiple legitimate devices can share product identifiers. A lower link
speed, inactive function, or unusual device class needs context; none is an
automatic finding of device impersonation.

### Device Evidence Dimensions

Replace informal firmware tiers with a record of properties actually observed:

| Dimension | Evidence needed | Permitted conclusion |
|---|---|---|
| Identity and provenance | Device inventory, exact identifiers, trusted source and version | Consistent, inconsistent, or unverified identity |
| Configuration and function | Applicable device contract and matched observations | A specific conformance discrepancy with known alternatives |
| Runtime behavior | Collector coverage, workload and power-state baseline | A calibrated anomaly within the measured conditions |
| Memory-access policy | Active platform/driver remapping and available fault evidence | Permitted or denied access on the established path |
| Platform trust | Attestation policy and supported runtime observations | Trust in the measured properties, with unmeasured state explicit |

No public/private label establishes detector difficulty, guaranteed detection,
or a requirement for one particular trust anchor. A device can satisfy observed
behavioral checks while other properties remain unknown. See
[assurance boundaries](assurance-boundaries.md).

### Reference-Set Limits

Describe which legitimate device populations a baseline covers. A reference-set
absence is an unknown identity, not proof that a device class is malicious or
technically implausible. Do not claim that a whole class is defeated, undetected,
or exhausted without a versioned evaluation and measured error rates.
