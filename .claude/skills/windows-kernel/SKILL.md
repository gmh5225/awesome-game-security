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

### Hypervisor Code Integrity (HVCI)
```
- VBS-based protection
- Kernel code integrity
- Driver compatibility requirements
- Memory restrictions
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

### Intel VT-x
- VMCS configuration
- EPT (Extended Page Tables)
- VM exits handling

### AMD-V
- VMCB structure
- NPT (Nested Page Tables)
- SVM operations

### Use Cases
- Memory hiding
- Syscall interception
- Security monitoring
- Anti-cheat evasion

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
