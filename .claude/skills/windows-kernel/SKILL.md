---
name: windows-kernel-security
description: Analyze Windows driver trust boundaries and kernel evidence for game-security research. Use for IOCTL authorization, callbacks and IRQL, driver provenance, DSE/PatchGuard, VBS/HVCI, build-specific internals, and crash or memory forensics; select repository resources for symbol comparison, ETW metadata, driver-unit coverage and offline dumps. Distinguish documented contracts, observed host state and inferred internals; report privilege prerequisites, mitigation scope, missing coverage and benign alternatives.
---

# Windows Kernel Security

## Overview

This skill covers Windows kernel internals that matter for game security research: object callbacks, process and image notifications, APC behavior, driver loading, trust enforcement, memory manager structures, and the bookkeeping anti-cheats inspect to detect hostile drivers or hidden executable code.

Treat undocumented structures, offsets, globals, and allocator internals as
build-specific. Verify them against symbols and runtime observations for the
exact Windows build; use [`research-rigor`](../research-rigor/SKILL.md) before
generalizing a PoC or forensic heuristic.

## Driver Attack Surface and Evidence

For event provenance, provider/callback scope and absent telemetry, use
[observation coverage](../anti-cheat/references/input-provenance-and-measurement.md).

| Threat class | Necessary capability or boundary | Evidence and defensive focus |
|---|---|---|
| Dangerous privileged interface | A caller can reach sensitive driver operations | Device ACLs, per-operation authorization, constrained functionality |
| Vulnerable signed-driver abuse | An affected driver is loaded or loadable and its interface reachable | Exact hash/version, provenance, loaded inventory, applicable policy |
| Driver-mediated acquisition | A host kernel acquisition component and usable interface | Driver/service identity, acquisition process, interface access, timeline |
| Kernel code/data tampering | Ability to modify the affected protected state | Trusted comparison evidence, ownership, protection and integrity events |

Review buffer lengths, output initialization, object lifetime, cancellation,
and IRQL alongside caller authorization. Signed code can still expose unsafe
operations. The table is a threat-model synthesis; actual reachability requires
evidence for the specific build and configuration.
[Microsoft driver security checklist](https://learn.microsoft.com/en-us/windows-hardware/drivers/driversecurity/driver-security-checklist)

Distinguish VBS/HVCI capability, configuration, and running state. Memory
integrity imposes executable-memory constraints; compatibility does not prove
every driver interface or data operation safe.
[Memory integrity compatibility](https://learn.microsoft.com/en-us/windows-hardware/drivers/driversecurity/implement-hvci-compatible-code)

Driver blocklists have incomplete coverage. Distinguish controls that prevent
writing a vulnerable driver to disk from policies that block loading it, and
record the active policy/version rather than assuming protection from the OS name.
[Microsoft driver block rules](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules)

Use Driver Verifier on a recovery-capable test system when evaluating owned
drivers; preserve tested configuration and crash artifacts. It can deliberately
bugcheck a system and does not establish a low false-positive anti-abuse detector.
[Driver Verifier](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/driver-verifier)

For acquisition relayed over USB or a network, use the
[source/transport distinction](../dma-attack/references/acquisition-and-transport.md).
Legitimate incident response can produce the same acquisition artifacts.
Sources in this section were reviewed on 2026-09-09.

## README Coverage

- `Cheat > PatchGuard-related`
- `Cheat > Driver Signature enforcement`
- `Cheat > Windows Kernel Explorer`
- `Cheat > EFI Driver` (cross-reference with game-hacking skill)
- `Cheat > Vulnerable Driver`
- `Anti Cheat > Detection:Attach`
- `Anti Cheat > Detection:Hide`
- `Anti Cheat > Detection:Vulnerable Driver`
- `Anti Cheat > Detection:Spoof Stack`
- `Anti Cheat > Windows Ring3 Callback`
- `Anti Cheat > Windows Ring0 Callback`
- `Anti Cheat > Information System & Forensics`
- `Some Tricks > Windows Ring0`
- `Windows Security Features`

## Core Kernel Concepts

### Important Structures
- EPROCESS / ETHREAD
- KTHREAD / KAPC / KAPC_STATE
- MMVAD / VAD tree nodes
- PEB / TEB
- DRIVER_OBJECT
- DEVICE_OBJECT
- IRP (I/O Request Packet)

### Key Tables
- SSDT (System Service Descriptor Table)
- IDT (Interrupt Descriptor Table)
- GDT (Global Descriptor Table)
- PspCidTable (Process/Thread handle table)
- PiDDBCacheTable / MmUnloadedDrivers / PoolBigPageTable

## User-Mode Kernel Symbol Walking

### Methodology
```
- Load local ntoskrnl image (typically C:\Windows\System32\ntoskrnl.exe)
- Use dbghelp + symbol server path (srv*cache*https://msdl.microsoft.com/download/symbols)
  to resolve exported symbol RVAs and type information
- Build structure-aware field lookup:
  - Query field offset directly (e.g., _EPROCESS.Token)
  - Enumerate all members of a target struct (_TOKEN, _EPROCESS, etc.)
  - Search a field name across all known structs (useful when parent type is unknown)
- Keep symbol path configurable for offline/private symbol repositories
```

### Why It Matters in Game Security
```
- Reduces hardcoded-offset fragility across Windows builds
- Helps map kernel object layouts used by anti-cheat and drivers
- Supports rapid adaptation when anti-cheat-relevant fields shift
  (EPROCESS, ETHREAD, token/handle/security-related members)
```

### Gadget Scanning Workflow
```
- Map executable sections of ntoskrnl image in user mode
- Scan for short control-flow gadgets (e.g., pop rcx ; ret, jmp rax)
- Use as a research primitive for:
  - ROP chain feasibility analysis
  - Kernel exploit mitigation evaluation
  - Anti-cheat hardening review against gadget-dependent attack paths
```

## Security Features

### PatchGuard (Kernel Patch Protection)
```
- Protects critical kernel structures
- Periodic verification checks
- BSOD on tampering detection
- Multiple trigger mechanisms
```

### Driver Signature Enforcement (DSE)
```
- Requires signed drivers
- CI.dll verification
- Test signing mode
- WHQL certification
```

### Virtualization-Based Security (VBS)
```
Architecture:
- Uses the Windows hypervisor to create an isolated execution environment
- Splits the system into Virtual Trust Levels (VTLs)
  - VTL0: Normal world — standard Windows kernel and user-mode processes
  - VTL1: Secure world — Secure Kernel, security policy enforcement
- VTL1 is designed to remain isolated from a compromised VTL0, assuming the
  hypervisor, secure kernel, hardware, and configuration path remain trustworthy
- Three main buckets:
  - Memory-protection features (HVCI)
  - Virtual Trust Levels (VTL0/VTL1 separation)
  - VBS enclaves (isolated execution for selected workloads)
```

### Hypervisor-Enforced Code Integrity (HVCI)
```
- Also known as Memory Integrity
- Ensures only trusted, validated code executes in kernel mode
- Combines Windows hypervisor + Secure Kernel (VTL1) for enforcement
- Key mechanism: W→X transition restriction
  - Enforced code pages are not intended to be writable from VTL0
  - Executability is granted only after the configured code-integrity checks
- Enforcement pipeline:
  - Code integrity policy defines what is trusted
  - Hypervisor memory enforcement via second-stage address translation (EPT/SLAT)
  - Once a kernel page is validated, strict execution rules are enforced
- Driver compatibility requirements: drivers must be HVCI-compatible
```

### Secure Boot
```
- UEFI-based boot verification
- Boot loader chain validation
- Kernel signature checks
- DBX (forbidden signatures)
- Foundation for attestation and DMA-hardening assumptions
```

## Kernel Callbacks

### Process Callbacks
```cpp
PsSetCreateProcessNotifyRoutine
PsSetCreateProcessNotifyRoutineEx
PsSetCreateProcessNotifyRoutineEx2
```

### Thread Callbacks
```cpp
PsSetCreateThreadNotifyRoutine
PsSetCreateThreadNotifyRoutineEx
```

### Image Load Callbacks
```cpp
PsSetLoadImageNotifyRoutine
PsSetLoadImageNotifyRoutineEx
```

### Object Callbacks
```cpp
ObRegisterCallbacks
// OB_OPERATION_HANDLE_CREATE
// OB_OPERATION_HANDLE_DUPLICATE
```

### APC / Execution Context
```cpp
KeInitializeApc
KeInsertQueueApc
KeStackAttachProcess
RtlWalkFrameChain
```

### Registry Callbacks
```cpp
CmRegisterCallback
CmRegisterCallbackEx
```

### Minifilter Callbacks
```cpp
FltRegisterFilter
// IRP_MJ_CREATE, IRP_MJ_READ, etc.
```

## Driver Development

### Basic Structure
```cpp
NTSTATUS DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
) {
    DriverObject->DriverUnload = DriverUnload;
    DriverObject->MajorFunction[IRP_MJ_CREATE] = DispatchCreate;
    DriverObject->MajorFunction[IRP_MJ_DEVICE_CONTROL] = DispatchIoctl;
    // Create device, symbolic link...
    return STATUS_SUCCESS;
}
```

### Communication Methods
- IOCTL (DeviceIoControl)
- Direct I/O
- Buffered I/O
- Shared memory

## Vulnerable Driver Exploitation

### Common Vulnerability Types
- Arbitrary read/write primitives
- IOCTL handler vulnerabilities
- Pool overflow
- Use-after-free

### Notable Vulnerable Drivers
```
- gdrv.sys (Gigabyte)
- iqvw64e.sys (Intel)
- MsIo64.sys
- Mhyprot2.sys (Genshin Impact)
- dbutil_2_3.sys (Dell)
- RTCore64.sys (MSI)
- Capcom.sys
```

### Exploitation Steps
1. Load vulnerable signed driver
2. Trigger vulnerability
3. Achieve kernel read/write
4. Disable DSE or load unsigned driver
5. Execute arbitrary kernel code

## PatchGuard Bypass Techniques

### Timing-Based
- Predict PG timer
- Modify between checks

### Context Manipulation
- Exception handling
- DPC manipulation
- Thread context tampering

### Hypervisor-Based
- EPT manipulation
- Memory virtualization
- Intercept PG checks

## Kernel Hooking

### ETW (Event Tracing for Windows)
```
- InfinityHook technique
- HalPrivateDispatchTable
- System call tracing
```

## ETW Internals

### Provider / Consumer Model
```
Architecture:
- Providers: kernel or user-mode components that emit events
  - Manifest-based providers (registered via wevtutil)
  - TraceLogging providers (self-describing, no manifest)
  - MOF providers (legacy WMI-based)
- Consumers: tools that subscribe to and process events
  - Real-time consumers (ETW sessions)
  - Log file consumers (.etl files)
- Controllers: manage sessions (xperf, tracelog, logman)

Key kernel providers:
  Microsoft-Windows-Kernel-Process (process/thread lifecycle)
  Microsoft-Windows-Kernel-File (file I/O)
  Microsoft-Windows-Kernel-Audit-API-Calls (security-sensitive APIs)
```

### ThreatIntel ETW Provider
```
- Microsoft-Windows-Threat-Intelligence
- Available to PPL (Protected Process Light) and above
- Events: NtReadVirtualMemory, NtWriteVirtualMemory, NtMapViewOfSection on protected processes
- Used by EDR and anti-cheat for detecting memory access to protected processes
- Attackers target: patch EtwThreatIntProvRegHandle or EtwpEventWriteFull
```

### Common ETW Bypass Patterns
```
- Patch EtwEventWrite in ntdll.dll (user-mode ETW silencing)
- Patch nt!EtwpEventWriteFull in kernel (kernel-mode ETW silencing)
- A debugger-related thread setting does not establish ETW invisibility;
  undocumented cross-subsystem effects need build/provider-specific evidence
- Remove provider registration by walking EtwRegistration list
- EPT-based protection can defend ETW structures from tampering
```

## Kernel Pool Architecture and Allocation Contracts

Treat allocator internals as hypotheses tied to an exact kernel binary,
architecture, configuration and matching symbols. Internal structure offsets,
size thresholds, encoded headers, cache depths and allocation-routing diagrams
are not a stable Windows driver interface. A symbol name without sufficient type
information does not establish a layout; public and private symbol content differ.
[Microsoft symbol scope](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/public-and-private-symbols)

### Architecture Questions for a Review

Separate the public allocation request from its observed allocator path. Record
pool flags, requested size, lifetime, calling/access IRQL and any special-pool or
verifier configuration. If a dump or source study identifies size-class,
variable-size, segment-backed or large-allocation paths, report only the path
supported for that artifact. Do not infer the introduction date or every later
layout from the availability of a public API.

For corruption analysis, preserve the useful threat classes: out-of-bounds
access, use after free, double free, uninitialized disclosure and metadata damage.
Each requires evidence of the faulty access or lifetime boundary. A crash, unusual
allocation pattern or integrity-check failure alone does not establish deliberate
exploitation, a specific corruption mechanism or successful privilege escalation.
Do not turn historical metadata-decoding formulas into a current parser contract.

### Public Pool API Boundaries

- `ExAllocatePool2` and `ExAllocatePool3` document Windows 10 version 2004 as
  their minimum supported client. The latter adds extended parameters; match the
  particular parameter contract to the target WDK and OS.
- Pool2 zero-initializes by default unless `POOL_FLAG_UNINITIALIZED` is used.
  Allocation initialization does not cover later buffer reuse or incomplete
  construction of a larger object. Review information disclosure and output
  initialization before removing explicit clearing.
- Review failure handling, quota semantics and pool/access IRQL together.
  At `DISPATCH_LEVEL`, Pool2 requires nonpaged allocation; memory accessed there
  must remain nonpaged even if it was allocated at a lower IRQL.
- Earlier Windows targets require the documented down-level allocation APIs and
  their initialization requirements. Do not assume Pool2 automatically falls
  back to allocation plus clearing on an older kernel.

[ExAllocatePool2](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2),
[ExAllocatePool3](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool3).

### KDP and Protected Data

Microsoft's 2020 KDP architecture article describes static data protection and
dynamic secure-pool allocations using VBS/SLAT. It is historical implementation
context, not evidence that a present machine protects every pool allocation or
that an arbitrary Pool3 allocation is secure. Establish the applicable API,
successful protection state, exact region and lifecycle, and the trustworthiness
of the hypervisor and policy path. Content protection does not by itself prove
that every reference to that content, caller or update operation is authorized.
[Microsoft KDP architecture](https://www.microsoft.com/en-us/security/blog/2020/07/08/introducing-kernel-data-protection-a-new-platform-security-technology-for-preventing-data-corruption/)

## Pool Allocation & Forensics

### Attribution and Coverage

Pool tags are caller-supplied labels used by debugging and tracking tools;
PoolMon groups memory use by tag. They are leads for attribution, not
cryptographic driver identities. A rare tag, a shared tag or a lookup in
`pooltag.txt` cannot by itself establish which signed binary allocated a buffer,
that a hidden driver is present, or that the allocation is malicious.
[PoolMon scope](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/using-poolmon-to-find-a-kernel-mode-memory-leak)

If a report invokes `PiDDBCacheTable`, `MmUnloadedDrivers`, `PoolBigPageTable` or
similar internal names, require an exact-build definition, collection method,
retention/coverage limits and supporting artifacts. Do not assume a universal
field layout, complete driver history or a one-to-one relationship between a
pool allocation and a driver object. Missing or malformed data can reflect
image incompleteness, stale symbols, reuse, collection effects or corruption.

### Review Evidence

For an existing authorized image, record its provenance/hash, acquisition time,
OS/architecture, symbol identity, parser version and unavailable regions. Keep
allocation facts, ownership hypotheses and security conclusions separate.
Correlate available allocation stacks, loaded-module provenance, driver/service
records and independent telemetry. Explain benign alternatives before assigning
intent to executable memory, unrecognized tags or unusual allocation counts.

A negative scan describes the selected parser, metadata path and retained
snapshot; it is not proof that all allocations or prior driver activity were
observed. A bugcheck code is a starting point for its parameters, stack and
surrounding state, not a unique allocator-path or attack signature.

Sources for these pool-contract and evidence corrections reviewed: 2026-09-09.

### SSDT Hooking (Legacy)
```
- Modify service table entries
- Requires PG bypass
- High detection risk
```

### IRP Hooking
```
- Hook driver dispatch routines
- Less monitored than SSDT
- Per-driver targeting
```

## Memory Manipulation

### Physical Memory Access
```cpp
MmMapIoSpace
MmCopyMemory
\\Device\\PhysicalMemory
```

### Virtual Memory
```cpp
ZwReadVirtualMemory
ZwWriteVirtualMemory
KeStackAttachProcess
MmCopyVirtualMemory
```

### MDL Operations
```cpp
IoAllocateMdl
MmProbeAndLockPages
MmMapLockedPagesSpecifyCache
```

## Research Tools

### Analysis
- WinDbg / WinDbg Preview
- Process Hacker / System Informer
- OpenArk
- WinArk

### Utilities
- KDU (Kernel Driver Utility)
- OSR Driver Loader
- DriverView

### Monitoring
- Process Monitor
- API Monitor
- ETW consumers

## EFI/Boot-Time Threats

### EFI Driver Cross-Reference
```
The README's > EFI Driver subcategory (under Cheat) contains 30+ projects:
- EFI bootkit frameworks: UEFI DXE drivers that persist across boots
- Boot-time memory mappers: inject code before Windows kernel initializes
- ExitBootServices hooks: intercept Windows boot handoff
- EFI runtime service abuse: GetVariable/SetVariable for kernel ↔ EFI comm

See also: game-hacking skill for EFI cheat workflows
```

### Boot-Time Access
```
- EFI runtime services persist after ExitBootServices
- DXE (Driver Execution Environment) phase: full hardware access
- Pre-kernel execution: no DSE, no PatchGuard, no HVCI enforcement
- Secure Boot is the primary mitigation (firmware signature verification)
```

### Memory Access
```
- GetVariable/SetVariable: pass data between EFI and OS runtime
- Runtime memory mapping via EFI memory map
- Physical memory access before Windows memory manager initializes
- ACPI table injection for persistent low-level modifications
```

## Hypervisor Development

### Hypervisor Types
```
Type 1 (bare-metal):
- Runs directly on hardware
- Examples: VMware ESXi, Microsoft Hyper-V, Xen
- Used for VBS, production security enforcement

Type 2 (hosted):
- Runs on top of a host operating system
- Examples: Oracle VirtualBox, VMware Workstation
- Common for research, development, and testing
```

### Hardware Virtualization Platforms
```
Intel VT-x:
- Introduced 2005, widely supported on modern Intel CPUs
- Foundation for VMCS, EPT, VM exits

AMD-V (SVM):
- AMD's counterpart to VT-x, also introduced 2005
- VMCB structure, NPT (Nested Page Tables)

ARM Virtualization Extensions:
- EL2 (hypervisor mode) and stage-2 memory translation
- Used on ARM platforms for mobile and embedded security
```

### Intel VT-x Core Concepts

#### VMCS (Virtual Machine Control Structure)
```
Central data structure for Intel VT-x:
- Describes guest state, host state, and virtualization controls
- Tells the processor:
  - What state to restore on VM entry
  - What state to save on VM exit
  - Which events transfer control back to the hypervisor

Guest/Host State Areas:
- Control registers (CR0, CR3, CR4)
- Segment registers (CS, SS, DS, ES, FS, GS)
- Debug registers (DR7 — hardware breakpoints)
- Descriptor-table registers (GDTR, IDTR)
- Key fields:
  - CR3: root of guest page tables, central to virtual memory
  - GDTR/IDTR: Global/Interrupt Descriptor Tables
  - CS/SS: code and stack segments
  - DR7: hardware breakpoint control

Control Fields:
- Pin-based controls
- Primary processor-based controls
- Secondary processor-based controls
- Events that cause VM exits:
  - CPUID interception
  - INVLPG interception
  - Control-register access
  - EPT violations
  - MSR access
```

#### EPT (Extended Page Tables)

EPT is Intel's second-stage translation for guest-physical to host-physical
addresses; guest page tables separately translate guest virtual addresses.
Review the processor capabilities and active virtualization controls before
assuming a paging depth, page size or particular handling of a denied access.
A four-level diagram describes one configuration, not every implementation.
[Intel system-programming manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)

Second-stage permissions constrain CPU access to the configured guest mappings.
They do not themselves identify the responsible module or decide whether an
operation is legitimate. Device-originated access needs its own IOMMU and device
policy analysis; use [DMA analysis](../dma-attack/SKILL.md). A guest virtual
address or module name must be correlated with the observed mapping and execution
context before making an attribution claim.

#### VM Exits & VMCALL
```
VM Exits:
- Occur when configured events happen in the guest
- Triggers: CPUID, CR access, I/O instructions, EPT violations, MSR access
- On exit: processor saves guest state (per VMCS), restores host state,
  records exit reason for hypervisor handler

VMCALL:
- Guest intentionally transfers control to hypervisor
- Similar in concept to a system call (guest → hypervisor)
- Used for guest-hypervisor communication interfaces
```

#### Nested Virtualization
```
- Running a hypervisor inside a VM managed by another hypervisor
- Useful for research, testing, and development
- Adds complexity: multiple layers participate in the same virtualization flow
- Relevant for testing hypervisor-based defense under VMware/Hyper-V
```

### AMD-V (SVM)
- VMCB (Virtual Machine Control Block) structure
- NPT (Nested Page Tables) — AMD's SLAT equivalent
- SVM operations (VMRUN, VMSAVE, VMLOAD)

### Review Use Cases

Use virtualization evidence to examine guest isolation, authorized introspection
and integrity policy. Treat unauthorized concealment or tampering as threat
categories with explicit access prerequisites and observation limits; the
presence of virtualization is also normal for development and platform security.

### Windows Hypervisor Platform (WHP) API

WHP exposes user-mode APIs to manage guest partitions, virtual processors and
guest-physical mappings using the Windows hypervisor. It does not grant a tool
arbitrary control over the running host kernel. Record the host/guest boundary,
Windows build, architecture, SDK, feature state and actual capabilities.
[WHP API contract](https://learn.microsoft.com/en-us/virtualization/api/hypervisor-platform/hypervisor-platform)

The current `WHvRunVirtualProcessor` contract lists Windows 10 version 1803 for
x64 and Windows 11 version 24H2 build 26100.3915 for Arm64. Its successful return
and exit context describe a stop in guest execution, not complete tracing of
every instruction or a deterministic replay. Capabilities and available exit
contexts are architecture- and configuration-dependent; there is no generic
`syscall` exit reason in the documented enumeration. Correlate the actual reason
and context with the analysis question.
[Run contract](https://learn.microsoft.com/en-us/virtualization/api/hypervisor-platform/funcs/whvrunvirtualprocessor),
[exit contexts](https://learn.microsoft.com/en-us/virtualization/api/hypervisor-platform/funcs/whvexitcontextdatatypes),
[capabilities](https://learn.microsoft.com/en-us/virtualization/api/hypervisor-platform/funcs/whvgetcapability).

Preserve unmodeled device, scheduler, timing and concurrency effects in a result.
A CPU feature name or enabled optional feature alone does not prove that a given
analysis tool, nested environment or third-party hypervisor combination is
supported. Use product/build-specific evidence for compatibility; do not impose
a universal coexistence or conflict rule.

## Hypervisor-Based Defense

### Enforcement Boundary

A trusted hypervisor can enforce a separate guest-memory protection boundary.
Windows VBS/KDP is one concrete architecture; other platforms' isolated execution
environments require their own contracts and must not be equated with EPT hooks.
Protecting selected data also differs from validating kernel code, authenticating
an administrative request or preserving a detector's end-to-end coverage.
[Microsoft KDP architecture](https://www.microsoft.com/en-us/security/blog/2020/07/08/introducing-kernel-data-protection-a-new-platform-security-technology-for-preventing-data-corruption/)

### Conditions for a Supported Protection Claim

| Review question | Evidence required |
|---|---|
| What is covered? | Exact protected memory, active mappings, access class and lifecycle; names such as callback list or ETW structure are not enough |
| Who owns the policy? | Hypervisor/security-component provenance and the authority allowed to change mappings or configuration |
| Was an access observed? | Available fault/exit context, collection coverage and correlation with the relevant mapping and execution context |
| Was the operation prevented? | Enforced decision and resulting state; a reported exit alone does not establish denial or continuing integrity |
| What remains outside scope? | Unprotected aliases or state, permitted update paths, device DMA, firmware and independent event or service failures |

For a vulnerable-driver threat, first establish the affected driver's presence,
reachable interface and required privilege. A claim that attempted kernel data
tampering was blocked additionally requires the protection evidence above.
Do not infer that every driver-mediated write would fault or that every callback
remains intact merely because a hypervisor is installed.

A CPU fault gives machine context; identifying a trustworthy principal and
handling an allowed update are separate policy problems. Report detection,
prevention, post-event integrity and recovery as different outcomes. Guest-kernel
compromise does not automatically defeat an independently enforced boundary,
but that claim assumes the hypervisor, hardware and configuration path remain
trustworthy. Preserve those assumptions and any missing coverage explicitly.

Sources for these virtualization-boundary corrections reviewed: 2026-09-09.

## Resource Organization

The README contains categorized links for:
- PatchGuard research and bypasses
- DSE bypass techniques
- Vulnerable driver exploits
- Kernel callback enumeration
- ETW/PMI/NMI handlers
- Intel PT integration

---

## Repository Navigation

For project selection, load [repository resource selection](references/repository-resources.md) on demand. Use the shared [repository navigation](../overview/references/repository-navigation.md) for local discovery layers, filename case, missing snapshots and currentness. Generated descriptions and wiki pages are discovery aids, not independent evidence.

For topic discovery, see the [compiled windows-kernel overview](../../../wiki/overviews/windows-kernel.md). Verify its technical claims against primary sources and the actual target context.

## Data Source

Use the following repository sources directly when applying this skill. Prefer
available local files for discovery and scoped historical inspection; use the
raw URLs when the collection is not installed locally. These entrypoint details
are retained here so source lookup does not depend on loading another skill.

### 0. Compiled Wiki

Start with [wiki/index.md](../../../wiki/index.md) for topical synthesis and
cross-project connections. [Wiki schema](../../../wiki/AGENTS.md) describes its
structure. Generated wiki pages are discovery aids; follow their original
citations before adopting technical claims.

Raw catalog: [wiki/index.md](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/wiki/index.md).
For this domain, read [wiki/overviews/windows-kernel.md](../../../wiki/overviews/windows-kernel.md).
Raw URL: [windows-kernel overview](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/wiki/overviews/windows-kernel.md).

A direct project question can start with its README entry or description below;
reading the entire wiki is unnecessary.

### 1. Project Overview and Resource Index

[README.md](../../../README.md) contains the collection's actual categories,
subcategories, project URLs and short descriptions. Find the relevant category
and retain the original URL, including any specific file or revision suffix.

Raw index: [README.md](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md).

### 2. Repository Descriptions

For a concise project summary, look for the actual local path:

```text
description/{owner}/{repo}/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt
```

Example: [bgfx description](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/bkaradzic/bgfx/description_en.txt).
Extract owner/repository from the original GitHub project URL, omitting a .git
suffix. Resolve existing path casing before constructing a local/raw path.
Descriptions are generated summaries, not independent verification. If absent
or inaccessible, use the README entry, relevant archive or original project.

### 3. Repository Source Archives

For deeper inspection of an available captured source tree, locate:

```text
archive/{owner}/{repo}.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt
```

Example: [bgfx archive](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/bkaradzic/bgfx.txt).
Prefer inspecting the relevant portion of an existing archive over re-cloning
merely to inspect the same captured material. Archives may exclude files, use
fallback extraction or contain truncation; they are not guaranteed complete
checkouts. Record any upstream revision evidence and included-file limits.
If missing or insufficient, follow the README's original upstream URL.

### Choose and Verify the Source

For a specific project, locate its README identity, use a description or wiki
page for orientation when helpful, then inspect the relevant archive/source
artifact for the question. For current compatibility or exact implementation,
verify the matching upstream documentation, release or immutable source revision.
Keep the collection revision and capture/generation dates separate from the
upstream version. Multiple generated layers from one source are not independent
corroboration, and missing archive content does not establish upstream absence.

The per-domain resource guide above helps choose useful artifacts. Shared
[repository navigation](../overview/references/repository-navigation.md) adds the optional read-only indexer,
case-ambiguity handling and maintenance details; it supplements this Data Source
section rather than replacing it.
