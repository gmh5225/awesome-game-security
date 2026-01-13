---
name: windows-kernel-security
description: Guide for Windows kernel security research including driver development, system callbacks, security features, and kernel exploitation. Use this skill when working with Windows drivers, PatchGuard, DSE, or kernel-level security mechanisms.
---

# Windows Kernel Security

## Overview

This skill covers Windows kernel security topics from the awesome-game-security collection, including driver development, system callbacks, security feature bypasses, and kernel-mode exploitation.

## Core Kernel Concepts

### Important Structures
- EPROCESS / ETHREAD
- PEB / TEB
- DRIVER_OBJECT
- DEVICE_OBJECT
- IRP (I/O Request Packet)

### Key Tables
- SSDT (System Service Descriptor Table)
- IDT (Interrupt Descriptor Table)
- GDT (Global Descriptor Table)
- PspCidTable (Process/Thread handle table)

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
