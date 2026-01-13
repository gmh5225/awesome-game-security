---
name: game-hacking-techniques
description: Guide for game hacking techniques and cheat development. Use this skill when researching memory manipulation, code injection, ESP/aimbot development, overlay rendering, or game exploitation methodologies.
---

# Game Hacking Techniques

## Overview

This skill covers game hacking techniques documented in the awesome-game-security collection, including memory manipulation, rendering overlays, input simulation, and exploitation methods.

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
