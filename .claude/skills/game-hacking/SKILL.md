---
name: game-hacking-techniques
description: Guide for game-hacking technique taxonomy and threat modeling relevant to game security. Use this skill when researching memory access, code injection, overlays, input simulation, engine-specific attack surfaces, or how modern anti-cheat systems constrain user-mode, kernel-mode, hypervisor, and DMA-based cheat implementations.
---

# Game Hacking Techniques

## Overview

This skill covers game-hacking techniques documented in the awesome-game-security collection, with emphasis on how cheats move from user mode to kernel mode, hypervisors, and DMA when defenders raise the bar. It is best used to understand the offensive side of the threat model that anti-cheat systems are designed to detect.

## README Coverage

- `Cheat > Debugging`
- `Cheat > Packet Sniffer&Filter`
- `Cheat > Packet Capture&Parse`
- `Cheat > SpeedHack`
- `Cheat > Injection:Windows`
- `Cheat > Injection:Linux`
- `Cheat > Injection:Android`
- `Cheat > Injection:IOS`
- `Cheat > Injection:PlayStation`
- `Cheat > DLL Hijack`
- `Cheat > Hook`
- `Cheat > Anti Signature Scanning`
- `Cheat > RPM`
- `Cheat > DMA`
- `Cheat > W2S`
- `Cheat > Overlay`
- `Cheat > Render/Draw`
- `Cheat > UI Interface`
- `Cheat > Vulnerable Driver`
- `Cheat > Driver Communication`
- `Cheat > EFI Driver`
- `Cheat > QEMU/KVM/PVE/VBOX`
- `Cheat > Wine`
- `Cheat > Anti Screenshot`
- `Cheat > Spoof Stack`
- `Cheat > Hide`
- `Cheat > Anti Forensics`
- `Cheat > Triggerbot & Aimbot`
- `Cheat > WallHack`
- `Cheat > HWID`
- `Cheat > Bypass Page Protection`
- `Cheat > SDK CodeGen`
- `Cheat > Game Engine Explorer:*`
- `Cheat > Explore UWP`
- `Cheat > Explore AntiCheat System:*`
- `Cheat > Game:*`
- `Cheat > Launcher Abuser`
- `Cheat > Linux Kernel Explorer`
- `Cheat > Cheat Engine Plugins`
- `Some Tricks > Windows Ring0`
- `Some Tricks > Windows Ring3`
- `Some Tricks > Linux`
- `Some Tricks > Android`

## Escalation Model

### User-Mode
- Read and write process memory
- Inject DLLs or shellcode
- Hook graphics or input APIs

### Kernel-Mode
- Use signed or vulnerable drivers for direct memory access
- Bypass handle-based protections and inspect protected processes
- Interact with callbacks, page tables, or kernel objects directly

### Below the OS
- Virtualize the system with a hypervisor
- Read memory through PCIe DMA hardware
- Move logic to external devices or secondary machines

## Core Concepts

### Memory Manipulation
- Read Process Memory (RPM)
- Write Process Memory (WPM)
- Pattern scanning
- Pointer chains
- Structure reconstruction

### Process Injection
- DLL injection methods
- Manual mapping
- Shellcode injection
- Thread hijacking
- APC injection

### Hooking Techniques
- Inline hooking (detours)
- IAT/EAT hooking
- VTable hooking
- Hardware breakpoint hooks
- Syscall hooking

## Cheat Categories

### Visual Cheats (ESP)
```
- World-to-Screen transformation
- Player/entity rendering
- Box ESP, skeleton ESP
- Item highlighting
- Radar/minimap hacks
```

### Aim Assistance
```
- Aimbot algorithms
- Triggerbot (auto-fire)
- No recoil/no spread
- Bullet prediction
- Silent aim
```

### Movement Cheats
```
- Speed hacks
- Fly hacks
- No clip
- Teleportation
- Bunny hop automation
```

### Miscellaneous
```
- Wallhacks
- Skin changers
- Unlock all
- Economy manipulation
```

## Overlay & Rendering

### Overlay Methods
- **DirectX Hook**: D3D9/11/12 Present hook
- **Vulkan Hook**: vkQueuePresentKHR hook
- **OpenGL Hook**: wglSwapBuffers hook
- **DWM Overlay**: Desktop Window Manager
- **External Window**: Transparent overlay window
- **Steam Overlay**: Hijacking Steam's overlay
- **NVIDIA Overlay**: GeForce Experience hijack

### Rendering Libraries
- **Dear ImGui**: Immediate mode GUI
- **GDI/GDI+**: Windows graphics
- **Direct2D**: Hardware-accelerated 2D

## Memory Access Methods

### User-Mode
```
- OpenProcess + ReadProcessMemory
- NtReadVirtualMemory
- Memory-mapped files
- Shared memory sections
```

### Kernel-Mode
```
- Driver-based access
- Physical memory access
- MDL-based copying
- KeStackAttachProcess
```

### Advanced Methods
```
- DMA (Direct Memory Access)
- EFI runtime services
- Hypervisor-based access
- Hardware-based (FPGA)
```

## EFI/UEFI Cheats

### Boot-Time Loading
```
- EFI manual map: load unsigned driver payload during UEFI boot phase
- ExitBootServices hook: intercept Windows boot to inject kernel code
- Runtime DXE drivers: persist across OS boot via EFI runtime services
- GetVariable/SetVariable: communicate between EFI and OS runtime
```

### EFI-Based Memory Access
```
- Map physical memory via EFI runtime services
- Bypass DSE entirely (code runs before Windows kernel loads)
- Survive Secure Boot if firmware is compromised or test-signed
- Combine with DMA for maximum stealth
```

### Detection Challenges
```
- No driver load event (PsSetLoadImageNotifyRoutine never fires)
- Not visible in MmUnloadedDrivers or PiDDBCacheTable
- Secure Boot + TPM attestation is primary defense
- Firmware integrity measurement (UEFI capsule verification)
```

## HWID Spoofing

### Targets
```
- Disk serial: IOCTL_STORAGE_QUERY_PROPERTY, SMART data
- NIC MAC address: NDIS OID_802_3_PERMANENT_ADDRESS
- SMBIOS: motherboard serial, system UUID, BIOS vendor
- GPU serial: registry-based or NVAPI/ADL queries
- Monitor EDID: display serial number
- Volume serial: NtQueryVolumeInformationFile
- TPM EK: Endorsement Key fingerprint
```

### Techniques
```
- Disk filter driver: intercept IOCTL and replace serial in response
- Registry value spoofing: modify cached hardware IDs
- SMBIOS table patching: modify raw SMBIOS memory region
- NIC driver hook: replace MAC in NDIS miniport response
- Full HWID spoofer: coordinated spoofing across all identifiers
```

## Stack Spoofing

### Return Address Spoofing
```
- Replace return address on stack before API call
- Restore original after call returns
- Evades stack-walk-based detection (RtlWalkFrameChain)
- Techniques: JMP RBX gadget, synthetic frames, fiber-based
```

### Call Stack Reconstruction
```
- Build fake but plausible call stack frames
- Match expected module return addresses (ntdll, kernel32)
- Evade NtQueryInformationThread stack inspection
- Tools: SpoofCallStack, Vulcan, CallStackSpoofer
```

### Detection & Evasion
```
- Anti-cheat walks thread stacks looking for non-module returns
- Stack unwinding via .pdata / UNWIND_INFO validation
- Spoofed stacks must pass RtlVirtualUnwind consistency checks
```

## Driver Communication

### Full Taxonomy (40+ methods in README)
```
IOCTL-based:
- Standard DeviceIoControl with custom control codes
- Buffered I/O, Direct I/O, METHOD_NEITHER

Data pointer swaps (abusing legitimate syscalls):
- NtUserGetObjectInformation
- NtConvertBetweenAuxiliaryCounterAndPerformanceCounter
- NtUserRegisterRawInputDevices
- NtGdiGetCOPPCompatibleOPMInformation
- NtDxgkGetTrackedWorkloadStatistics
- NtUserGetPointerInfoList
- NtUserSetInformationThread
- NtDCompositionSetChildRootVisual
- Win32k syscall hooks

Shared memory:
- Named shared sections (ZwCreateSection + ZwMapViewOfSection)
- Physical memory mapping
- Shared event objects for signaling

Callback-based:
- Registry callbacks (CmRegisterCallbackEx)
- Minifilter communication ports (FltCreateCommunicationPort)
- Object callbacks with embedded data

Unconventional channels:
- Named pipes from kernel
- Window messages (NtUserPostMessage)
- ETW provider channels
- Socket from kernel (Winsock Kernel / WSK)
- File system filter callbacks
- Debugging APIs (DbgPrint interception)
```

## World-to-Screen Calculation

### Basic Formula
```cpp
Vector2 WorldToScreen(Vector3 worldPos, Matrix viewMatrix) {
    Vector4 clipCoords;
    clipCoords.x = worldPos.x * viewMatrix[0] + worldPos.y * viewMatrix[4] + 
                   worldPos.z * viewMatrix[8] + viewMatrix[12];
    clipCoords.y = worldPos.x * viewMatrix[1] + worldPos.y * viewMatrix[5] + 
                   worldPos.z * viewMatrix[9] + viewMatrix[13];
    clipCoords.w = worldPos.x * viewMatrix[3] + worldPos.y * viewMatrix[7] + 
                   worldPos.z * viewMatrix[11] + viewMatrix[15];
    
    if (clipCoords.w < 0.1f) return invalid;
    
    Vector2 NDC;
    NDC.x = clipCoords.x / clipCoords.w;
    NDC.y = clipCoords.y / clipCoords.w;
    
    Vector2 screen;
    screen.x = (screenWidth / 2) * (NDC.x + 1);
    screen.y = (screenHeight / 2) * (1 - NDC.y);
    
    return screen;
}
```

## Engine-Specific Techniques

### Unity (Mono)
- Assembly-CSharp.dll analysis
- Mono JIT hooking
- Il2CppDumper for IL2CPP builds
- Method address resolution

### Unity (IL2CPP)
- GameAssembly.dll analysis
- Metadata recovery
- Type reconstruction
- Native hooking

### Unreal Engine
- GObjects/GNames enumeration
- UWorld traversal
- SDK generation (Dumper-7)
- Blueprint hooking

### Source Engine
- Entity list enumeration
- NetVars parsing
- ConVar manipulation
- Signature scanning

## Input Simulation

### Methods
- SendInput API
- mouse_event/keybd_event
- DirectInput hooking
- Raw input injection
- Driver-based input (mouclass)

### Kernel-Level
- Mouse class service callback
- Keyboard filter drivers
- HID manipulation

## Anti-Detection Techniques

### Code Protection
- Polymorphic code
- Code virtualization
- Anti-dump techniques
- String encryption

### Runtime Evasion
- Stack spoofing
- Return address manipulation
- Thread context hiding
- Module concealment

## Development Workflow

### External Cheat
```
1. Pattern scan for signatures
2. Read game memory externally
3. Process data in separate process
4. Render overlay or use input simulation
```

### Internal Cheat
```
1. Inject into game process
2. Hook rendering functions
3. Access game objects directly
4. Render through game's graphics context
```

## Learning Resources

### Communities
- UnknownCheats
- GuidedHacking
- Game Hacking Academy

### Practice Targets
- PWN Adventure (intentionally vulnerable)
- CTF game challenges
- Older/unsupported games

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
