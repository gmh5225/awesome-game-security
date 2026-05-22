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
- Aimbot algorithms (memory-based and AI visual)
- Triggerbot (auto-fire on crosshair detection)
- No recoil/no spread
- Bullet prediction and lead calculation
- Silent aim (server-side angle manipulation)
- AI visual aimbot (YOLO-based, no memory access required)
```

### AI Visual Cheats (Computer Vision Aimbot)
```
Architecture overview:
"Zero memory, zero driver injection" paradigm — uses screen capture +
AI object detection + hardware input injection. No process attachment,
no kernel driver, no game memory reading.

Typical setup:
┌─────────────────┐     screen capture      ┌──────────────────┐
│  Gaming PC      │ ───────────────────────▶ │  AI Pipeline     │
│  Game + OBS     │                          │  (same PC, or    │
│                 │ ◀─────────────────────── │   second PC)     │
└─────────────────┘     hardware input       │  YOLO model      │
                        (KMBox / Logitech)   │  TensorRT/CUDA   │
                                             └──────────────────┘

Dual-machine variant (maximum isolation):
- Machine A (game): only runs game + OBS, sends frames via NDI/capture card
- Machine B (cheat): runs AI model, sends mouse commands via USB/network
  to hardware input device on Machine A
- Game machine has zero cheat code/process

Single-machine variant:
- OBS + AI model run on the same PC
- AI implemented as OBS filter plugin (looks like "OBS is running")
- Mouse output via hardware device or driver-level injection

Pipeline stages:

1. Frame Capture:
   - OBS Game Capture (injects graphics hook DLL into game process)
   - OBS Window Capture (no injection, uses DXGI Desktop Duplication)
   - OBS plugin filter form (AI as OBS filter, minimal footprint)
   - Direct framebuffer copy from GPU output layer (60+ FPS)
   - Capture card (for dual-machine: HDMI/DP input on cheat PC)

2. AI Object Detection:
   - Model: YOLOv5 / YOLOv8 / YOLOv10 / YOLO11 (lightweight variants)
   - Training: fine-tuned on game-specific screenshots
     (enemy bodies, heads, torsos as labeled bounding boxes)
   - Input: cropped region around crosshair (320x320 or 640x640)
     to reduce inference cost
   - Output: bounding boxes with class (head/body/enemy) + confidence score
   - Acceleration: TensorRT (NVIDIA), CUDA, DirectML, OpenVINO
   - Target latency: < 20–30 ms per frame for competitive play

3. Coordinate Transform and Aiming Logic:
   - Convert pixel coordinates to mouse movement delta:
     delta_x = (target_x - screen_center_x) * sensitivity
     delta_y = (target_y - screen_center_y) * sensitivity
   - Target selection: closest to crosshair, highest confidence,
     head priority, or combined scoring
   - FOV (Field of View) lock: only engage targets within
     configurable pixel radius from crosshair center

4. Human-like Trajectory Smoothing:
   - Not instant snap — gradual movement with acceleration curve
   - Micro-jitter injection (simulates hand tremor)
   - Bézier curve or cubic interpolation for path
   - End-point correction (overshoot then settle)
   - Random engagement probability (e.g., 85-90% lock rate)
   - Slight intentional offset (not pixel-perfect center-mass)
   - Variable reaction delay (50-200 ms simulated human response)

5. Mouse Movement Execution:
   - Hardware input devices (see Input Simulation section below)
   - Movement commands sent as physical HID reports
   - Game sees genuine hardware mouse input, not API calls

Why OBS specifically:
- Legitimate streaming software, used by millions of streamers
- Anti-cheat cannot ban OBS-related processes without collateral damage
- Game Capture provides fast, low-latency frame access
- Plugin system allows embedding AI as a filter (invisible to AC)
- Supports D3D11, D3D12, Vulkan, OpenGL capture paths
```

### YOLO Model Training Pipeline (for Game AI Aimbot)
```
End-to-end workflow from raw game screenshots to deployed TensorRT model.

1. Data Collection:
   - Capture game screenshots during actual gameplay (OBS recording or replay)
   - Capture diverse scenarios: different maps, lighting, character skins,
     distances, poses, partial occlusion, smoke/flash effects
   - Aim for 2,000-10,000+ labeled images for robust detection
   - Include negative samples (empty scenes, friendlies, environment objects)

2. Annotation / Labeling:
   - Tools: LabelImg (YOLO format), CVAT (collaborative), Roboflow (cloud),
     Label Studio, makesense.ai (browser-based)
   - YOLO format: one .txt per image, each line:
     <class_id> <center_x> <center_y> <width> <height>
     (all values normalized to 0-1 relative to image dimensions)
   - Class definitions (typical):
     0: enemy_body (full body bounding box)
     1: enemy_head (head-only bounding box, for headshot targeting)
     2: friendly (to avoid shooting teammates)
   - Label head separately from body for head-priority targeting
   - Quality control: consistent label boundaries, no missed instances

3. Data Augmentation:
   - Built-in Ultralytics augmentations (mosaic, mixup, copy-paste)
   - Game-specific augmentations:
     - Brightness/contrast variation (simulate different map lighting)
     - Random crop around crosshair area (match inference ROI)
     - Motion blur (simulate fast movement)
     - Noise injection (simulate compression artifacts)
   - Avoid augmentations that distort aspect ratio
     (characters would look unnatural, hurting accuracy)

4. Training:
   - Framework: Ultralytics YOLOv8/v10/v11/YOLO11
   - Base model: yolov8n.pt or yolov8s.pt (nano/small for speed)
     or yolo11n.pt for latest architecture
   - Training command:
     yolo detect train data=game_dataset.yaml model=yolov8n.pt
       epochs=100 imgsz=640 batch=16 device=0
   - dataset.yaml structure:
     path: /path/to/dataset
     train: images/train
     val: images/val
     names: {0: enemy_body, 1: enemy_head, 2: friendly}
   - Key hyperparameters to tune:
     - imgsz: 320 (fastest) or 640 (more accurate)
     - lr0: initial learning rate (default 0.01)
     - conf: confidence threshold for inference (typically 0.4-0.6)
     - iou: IoU threshold for NMS (typically 0.45-0.7)
   - Training time: 1-4 hours on RTX 3060+ for nano model

5. Validation and Testing:
   - Evaluate mAP@0.5 and mAP@0.5:0.95 on validation set
   - Target: mAP@0.5 > 0.85 for reliable game detection
   - Test inference speed on target hardware
   - Visual inspection on held-out game screenshots

6. Export to TensorRT (deployment):
   - Step 1: Export to ONNX
     yolo export model=best.pt format=onnx simplify=True opset=17
   - Step 2: Convert ONNX to TensorRT engine
     yolo export model=best.pt format=engine half=True device=0
     (half=True enables FP16 precision)
   - Or use trtexec directly:
     trtexec --onnx=best.onnx --saveEngine=best.engine
       --fp16 --workspace=4096
   - FP16 performance: ~17 ms latency, ~57 FPS throughput,
     ~0.9% mAP drop vs FP32 (acceptable trade-off)
   - INT8 quantization: even faster but requires calibration dataset
     and careful accuracy validation

7. Runtime Integration:
   - Load TensorRT engine in C++/Python inference loop
   - Input: preprocessed frame (resize, normalize, HWC→CHW, float32/16)
   - Output: [N, 6] tensor (x1, y1, x2, y2, confidence, class_id)
   - Apply NMS (Non-Maximum Suppression) to deduplicate detections
   - Select target based on: closest to crosshair + highest confidence
   - Convert pixel coordinates to mouse delta

Alternative acceleration backends:
- DirectML (AMD GPUs, Windows native)
- OpenVINO (Intel GPUs/CPUs)
- ONNX Runtime with CUDA EP (cross-platform)
- CoreML (macOS, less common for game cheats)
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

### Software Methods
- SendInput API
- mouse_event/keybd_event
- DirectInput hooking
- Raw input injection
- Driver-based input (mouclass)

### Kernel-Level
- Mouse class service callback
- Keyboard filter drivers
- HID manipulation

### Hardware Input Devices (for AI Visual Cheats)
```
Hardware input devices produce genuine HID reports indistinguishable
from real mouse/keyboard at the USB protocol level. This is the
critical stealth layer for AI visual aimbot setups.

KMBox series (KMBox Net, KMBox B Pro, KMBox B+):
- Standalone hardware device connected via USB or network
- Receives mouse/keyboard commands over TCP/UDP or serial
- Generates real USB HID reports to the gaming PC
- Gaming PC sees a standard USB mouse, not API-injected input
- Network variant enables dual-machine setups
- Supports relative movement, absolute positioning, button events
- API: simple serial/network protocol for move(dx, dy), click, etc.

Arduino / Teensy / STM32 microcontroller:
- Custom firmware emulating USB HID device
- Receives commands from cheat PC via serial/USB CDC
- Generates USB HID mouse reports
- Cheapest hardware option, fully customizable
- Leonardo / Pro Micro (ATmega32U4) most common for native USB HID

Logitech driver exploitation:
- Older versions of G HUB / LGS (Logitech Gaming Software) expose
  internal APIs for mouse movement
- ghub_mouse_move() or lgs_mouse_move() via DLL injection into GHUB
- Logitech devices have driver-level whitelist advantage
- Specific driver versions required (newer versions patched)
- No external hardware needed, but driver-version-dependent

Interception driver (interception.sys):
- Open-source keyboard/mouse filter driver
- Intercepts and injects input at driver level
- Commonly used with AI aimbots for zero-hardware-cost injection
- Detectable by anti-cheat (driver signature known)

HDMI/DP KVM-style middleman:
- Hardware device sitting between mouse and PC
- Intercepts real mouse data, injects AI-calculated deltas
- Transparent to both the mouse and the PC
- Highest stealth but most complex hardware setup

Detection difficulty ranking:
1. Dedicated hardware (KMBox, Arduino HID) — hardest to detect
   (genuine USB HID, no driver anomaly)
2. KVM middleman — very hard (transparent hardware interposer)
3. Logitech driver method — moderate (known driver versions)
4. Interception driver — easier (known driver signature)
5. SendInput / mouse_event — easiest (API-level, trivially detected)
```

### KMBox Protocol Details
```
KMBox Net (network variant) — UDP-based protocol:

Packet header (16 bytes, Little-Endian):
Offset  Field      Size   Description
0x00    MAC        4 B    Device UUID (unique per device, used for auth)
0x04    RAND       4 B    Random value or parameter
0x08    INDEXPTS   4 B    Incrementing sequence number (replay protection)
0x0C    CMD        4 B    Command code

Key command codes:
Code          Command          Description
0xAF3C2828    connect          Establish connection with device
0xAEDE7345    mouse_move       Direct mouse movement (dx, dy)
0xAEDE7346    mouse_automove   Human-like movement with interpolation
0xA238455A    mouse_beizer     Bézier curve mouse movement
0x9823AE8D    mouse_left       Left button press/release
0x238D8212    mouse_right      Right button press/release
0x97A3AE8D    mouse_middle     Middle button press/release
0xFFEEAD38    mouse_wheel      Scroll wheel
0x123C2C2F    keyboard_all     Keyboard key event

Mouse API functions:
- move(x, y):                 Direct relative movement, no interpolation
- move_auto(x, y, ms):        Human-like movement over ms milliseconds,
                               built-in Bézier curve interpolation
- move_beizer(x, y, ms,       Second-order Bézier curve with custom
    x1, y1, x2, y2):          control points for trajectory shaping

Encrypted variants (enc_*):   Same functions with packet-level encryption
                               to resist network packet analysis

Performance:
- Network (UDP): ~1,000 commands/second
- Serial (KMBox B/B+, 115200 baud): ~300 commands/second
- Network latency: < 2 ms per command (LAN)

KMBox B / B Pro (serial variant):
- USB CDC serial communication (COM port)
- Baud rate: 115200 or higher
- Simpler protocol: ASCII or binary command frames
- move(x, y) over serial: ~3 ms round trip

Physical keyboard/mouse monitoring:
- monitor() function reads real user input from the device
- Enables "pass-through + inject" mode:
  real user input flows through normally,
  AI-calculated deltas are added on top

Arduino / Teensy HID protocol:
- Custom serial command format (typically simple ASCII):
  "M,dx,dy\n"      — mouse move
  "C,button\n"      — click (1=left, 2=right, 3=middle)
  "K,keycode\n"     — keypress
- USB HID report generated by ATmega32U4 (Leonardo)
  or ARM-based Teensy (3.2, 4.0, 4.1)
- HID report descriptor mimics standard mouse:
  buttons (3 bits) + X delta (8-16 bits) + Y delta (8-16 bits)
- No custom driver needed — OS uses generic HID driver

Logitech driver API (exploitable versions):
- G HUB versions prior to certain patches expose internal functions
- Key DLLs: LGS (lcore.dll), G HUB (ghub_mouse.dll or internal APIs)
- ghub_mouse_move(dx, dy) or equivalent internal symbol
- Accessed via DLL injection into GHUB process
  or LoadLibrary + GetProcAddress
- Movement appears as Logitech device input in the HID stack
- Patched in newer G HUB versions; specific version numbers
  circulate in cheat communities
```

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
