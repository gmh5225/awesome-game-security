---
name: windows-kernel-security
description: Guide for Windows kernel internals and security mechanisms used in game protection and low-level research. Use this skill when working with drivers, IRQL-sensitive callbacks, EPROCESS, ETHREAD, MMVAD internals, IOCTL paths, DSE, PatchGuard, HVCI, PiDDBCache, MmUnloadedDrivers, or kernel memory inspection.
---

# Windows Kernel Security

## Overview

This skill covers Windows kernel internals that matter for game security research: object callbacks, process and image notifications, APC behavior, driver loading, trust enforcement, memory manager structures, and the bookkeeping anti-cheats inspect to detect hostile drivers or hidden executable code.

## README Coverage

- `Cheat > PatchGuard-related`
- `Cheat > Driver Signature enforcement`
- `Cheat > Windows Kernel Explorer`
- `Anti Cheat > Detection:Attach`
- `Anti Cheat > Detection:Hide`
- `Anti Cheat > Detection:Vulnerable Driver`
- `Anti Cheat > Windows Ring0 Callback`
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
- Even if VTL0 kernel is fully compromised, VTL1 remains isolated
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
  - Executable kernel pages cannot become writable
  - Writable pages cannot become executable without re-validation
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

## EFI/UEFI Integration

### Boot-Time Access
```
- EFI runtime services
- Boot driver loading
- Pre-OS execution
```

### Memory Access
```
- GetVariable/SetVariable
- Runtime memory mapping
- Physical memory access
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
```
Intel's implementation of SLAT (Second-Level Address Translation):
- Gives the hypervisor independent control over guest memory
- Two-stage address translation pipeline:
  1. GVA → GPA: Guest Virtual → Guest Physical (via guest page tables, rooted at CR3)
  2. GPA → HPA: Guest Physical → Host Physical (via EPT, rooted at EPTP in VMCS)
- Guest believes it owns its own memory mappings
- Hypervisor has a second, independent layer controlling:
  - What physical memory is reachable
  - What permissions apply (read/write/execute)

EPT Hierarchy:
- PML4 → PDPT → PD → PT (4-level page table)
- Each entry carries read/write/execute permissions
- EPT violations trigger VM exits when access permissions are violated

Page Table Entries (PTE):
- Maps GVA to GPA
- Carries: read/write, supervisor-only, caching, software-defined bits
- Guest PTEs and EPT serve different roles:
  - Guest PTE: controls guest's view of memory
  - EPT: controls hypervisor's view of the guest
```

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

### Use Cases
- Memory hiding
- Syscall interception
- Security monitoring
- Anti-cheat evasion
- EPT-based memory protection and introspection

## Hypervisor-Based Defense

### Concept
```
- Security approach using virtualization primitives to enforce protections
  from a higher privilege level than the guest kernel
- Moves security decisions into an isolated execution environment
  that a compromised kernel cannot easily tamper with
- Present across major OS platforms:
  - Windows: Virtualization-Based Security (VBS)
  - Android: Android Virtualization Framework (AVF)
  - Apple: Secure execution environments, hardware-backed isolation
```

### EPT Hooks as Defensive Primitives
```
Mechanism:
- Instead of patching the guest kernel, modify EPT permissions
- Specific memory accesses trigger EPT violations → VM exit
- Hypervisor inspects the access and decides: allow, deny, or log

Example: Watching writes to a sensitive region
1. Remove write permission from the EPT entry for target region
2. Guest runs normally until it attempts a write to that region
3. EPT violation → VM exit → hypervisor receives control
4. Hypervisor evaluates context:
   - Which module performed the access
   - What memory was touched
   - Whether the access is authorized
5. Decision: allow write, deny and return, or log and continue

Advantages over traditional kernel hooks:
- Operate outside the guest OS
- Remain effective even if guest kernel is compromised
- Transparent to guest-level detection
- Cannot be removed by kernel-level rootkits
```

### Protectable Assets via EPT
```
- Executable pages of EPP (Endpoint Protection Platform) drivers
  → Prevents silent patching of security software
- ETW-related structures
  → Unauthorized writes fault into hypervisor
- Callback/callout/routine lists (PsSetCreateProcessNotifyRoutine, etc.)
  → Write authorization moved outside the guest kernel
- Critical kernel data structures
  → PatchGuard-protected regions, SSDT, IDT
```

### Threat Model for Hypervisor Defense
```
Assumes kernel compromise has already happened:
- Attacker has kernel code execution
- Attacker can load vulnerable drivers (BYOVD)
- Attacker can modify kernel memory
- Traditional kernel-resident protections are untrustworthy

Hypervisor advantage:
- Sits above the guest kernel in privilege hierarchy
- Enforces policies from a higher privilege layer
- Kernel-level rootkits cannot disable hypervisor-level enforcement
```

### Attack Scenario: BYOVD vs EPT Protection
```
Without hypervisor defense:
1. Attacker loads vulnerable signed driver
2. Gains kernel R/W primitives
3. Patches callback list to remove EPP callbacks
4. EPP is blinded — attacker operates undetected

With EPT-based defense:
1. Attacker loads vulnerable signed driver
2. Gains kernel R/W primitives
3. Attempts to patch callback list
4. EPT violation triggers VM exit
5. Hypervisor catches the write, evaluates context
6. Write is denied — callback list remains intact
```

## Resource Organization

The README contains categorized links for:
- PatchGuard research and bypasses
- DSE bypass techniques
- Vulnerable driver exploits
- Kernel callback enumeration
- ETW/PMI/NMI handlers
- Intel PT integration

---

## Data Source

**Important**: This skill provides conceptual guidance and overview information. For detailed information use the following sources:

### 1. Project Overview & Resource Index

Fetch the main README for the full curated list of repositories, tools, and descriptions:

```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md
```

The main README contains thousands of curated links organized by category. When users ask for specific tools, projects, or implementations, retrieve and reference the appropriate sections from this source.

### 2. Repository Code Details (Archive)

For detailed repository information (file structure, source code, implementation details), the project maintains a local archive. If a repository has been archived, **always prefer fetching from the archive** over cloning or browsing GitHub directly.

**Archive URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/ufrisk/pcileech.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/000-aki-000/GameDebugMenu.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the archive URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name (no `.git` suffix).
3. Fetch the archive file — it contains a full code snapshot with file trees and source code generated by `code2prompt`.
4. If the fetch returns a 404, the repository has not been archived yet; fall back to the README or direct GitHub browsing.

### 3. Repository Descriptions

For a concise English summary of what a repository does, the project maintains auto-generated description files.

**Description URL format:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt
```

**Examples:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/00christian00/UnityDecompiled/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/ufrisk/pcileech/description_en.txt
```

**How to use:**
1. Identify the GitHub repository the user is asking about (owner and repo name from the URL).
2. Construct the description URL: replace `{owner}` with the GitHub username/org and `{repo}` with the repository name.
3. Fetch the description file — it contains a short, human-readable summary of the repository's purpose and contents.
4. If the fetch returns a 404, the description has not been generated yet; fall back to the README entry or the archive.

**Priority order when answering questions about a specific repository:**
1. Description (quick summary) — fetch first for concise context
2. Archive (full code snapshot) — fetch when deeper implementation details are needed
3. README entry — fallback when neither description nor archive is available
