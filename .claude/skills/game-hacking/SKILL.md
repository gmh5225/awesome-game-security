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
- `Cheat > SpeedHack`
- `Cheat > Injection:*`
- `Cheat > Hook`
- `Cheat > RPM`
- `Cheat > DMA`
- `Cheat > W2S`
- `Cheat > Overlay`
- `Cheat > Driver Communication`
- `Cheat > HWID`
- `Cheat > Game Engine Explorer:*`
- `Cheat > Explore AntiCheat System:*`
- `Cheat > Game:*`

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

## Driver Communication

### Methods
- IOCTL-based
- Shared memory
- Registry callbacks
- Syscall hooks
- Data pointer swaps

### Common Patterns
```cpp
// Data pointer swap example
NtUserGetObjectInformation
NtConvertBetweenAuxiliaryCounterAndPerformanceCounter
Win32k syscall hooks
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
