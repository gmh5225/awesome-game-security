---
name: graphics-api-hooking
description: Guide for graphics API interception, overlay rendering, and render-pipeline analysis across DirectX, OpenGL, and Vulkan. Use this skill when working with Present or SwapBuffers hooks, DXGI swap chains, shader or draw-call interception, screenshot-sensitive overlays, or graphics debugging in game security research.
---

# Graphics API Hooking & Rendering

## Overview

This skill covers graphics API resources from the awesome-game-security collection, including DirectX, OpenGL, and Vulkan hooking techniques, overlay rendering, and graphics debugging.

## README Coverage

- `DirectX > Guide`
- `DirectX > Hook`
- `DirectX > Tools`
- `DirectX > Emulation`
- `DirectX > Compatibility`
- `DirectX > Overlay`
- `OpenGL > Guide`
- `OpenGL > Source`
- `OpenGL > Hook`
- `Vulkan > Guide`
- `Vulkan > API`
- `Vulkan > Hook`
- `Cheat > Overlay`
- `Cheat > Render/Draw`
- `Cheat > Anti Screenshot`
- `Anti Cheat > Screenshot`
- `Anti Cheat > Detection:Overlay`

## DirectX

### DirectX 9
```cpp
// Key functions to hook
IDirect3DDevice9::EndScene
IDirect3DDevice9::Reset
IDirect3DDevice9::Present
```

### DirectX 11
```cpp
// Key functions to hook
IDXGISwapChain::Present
ID3D11DeviceContext::DrawIndexed
ID3D11DeviceContext::Draw
```

### DirectX 12
```cpp
// Key functions to hook
IDXGISwapChain::Present
ID3D12CommandQueue::ExecuteCommandLists
```

### VTable Hooking
```cpp
// DX11 Example
typedef HRESULT(__stdcall* Present)(IDXGISwapChain*, UINT, UINT);
Present oPresent;

HRESULT __stdcall hkPresent(IDXGISwapChain* swapChain, UINT syncInterval, UINT flags) {
    // Render overlay here
    return oPresent(swapChain, syncInterval, flags);
}

// Hook via vtable
void* swapChainVtable = *(void**)swapChain;
oPresent = (Present)swapChainVtable[8];  // Present is index 8
```

## OpenGL

### Key Functions
```cpp
wglSwapBuffers
glDrawElements
glDrawArrays
glBegin/glEnd (legacy)
```

### Hook Example
```cpp
typedef BOOL(WINAPI* wglSwapBuffers_t)(HDC);
wglSwapBuffers_t owglSwapBuffers;

BOOL WINAPI hkwglSwapBuffers(HDC hdc) {
    // Render overlay
    return owglSwapBuffers(hdc);
}
```

## Vulkan

### Key Functions
```cpp
vkQueuePresentKHR
vkCreateSwapchainKHR
vkCmdDraw
vkCmdDrawIndexed
```

### Instance/Device Layers
- Use validation layers for debugging
- Custom layers for interception
- Layer manifest configuration

## Universal Hook Libraries

### Kiero
- Cross-API hook library
- Supports DX9/10/11/12, OpenGL, Vulkan
- Automatic method detection

### Universal ImGui Hook
- Pre-built ImGui integration
- Multiple API support
- Easy deployment

## ImGui Integration

### Setup (DX11)
```cpp
// In Present hook
ImGui_ImplDX11_Init(device, context);
ImGui_ImplWin32_Init(hwnd);

// Render
ImGui_ImplDX11_NewFrame();
ImGui_ImplWin32_NewFrame();
ImGui::NewFrame();

// Your rendering code
ImGui::Begin("Overlay");
// ...
ImGui::End();

ImGui::Render();
ImGui_ImplDX11_RenderDrawData(ImGui::GetDrawData());
```

### Window Procedure Hook
```cpp
// Required for ImGui input
LRESULT CALLBACK WndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    if (ImGui_ImplWin32_WndProcHandler(hWnd, msg, wParam, lParam))
        return true;
    return CallWindowProc(oWndProc, hWnd, msg, wParam, lParam);
}
```

## Overlay Techniques

### External Overlay
```
1. Create transparent window
2. Set WS_EX_LAYERED | WS_EX_TRANSPARENT
3. Use SetLayeredWindowAttributes
4. Render with GDI+/D2D
5. Position over game window
```

### DWM Overlay
```
- Hook Desktop Window Manager
- Render in DWM composition
- Higher privilege requirements
- Better anti-detection
```

### Steam Overlay Hijack
```
- Hook Steam's overlay functions
- Use existing overlay infrastructure
- Requires Steam running
```

### NVIDIA Overlay Hijack
```
- Hook GeForce Experience overlay
- Native-looking overlay
- May require specific drivers
```

## Shader Manipulation

### Wallhack Implementation
```hlsl
// Disable depth testing
OMSetDepthStencilState(depthDisabledState, 0);

// Or in pixel shader
float4 PSMain(VS_OUTPUT input) : SV_Target {
    // Always pass depth test
    return float4(1, 0, 0, 0.5);  // Red transparent
}
```

### Chams (Character Highlighting)
```hlsl
// Replace model shader
float4 PSChams(VS_OUTPUT input) : SV_Target {
    if (isEnemy) {
        return float4(1, 0, 0, 1);  // Red
    }
    return float4(0, 1, 0, 1);      // Green
}
```

## Rendering Concepts

### World-to-Screen
```cpp
D3DXVECTOR3 WorldToScreen(D3DXVECTOR3 pos, D3DXMATRIX viewProjection) {
    D3DXVECTOR4 clipCoords;
    D3DXVec3Transform(&clipCoords, &pos, &viewProjection);
    
    if (clipCoords.w < 0.1f) return invalid;
    
    D3DXVECTOR3 NDC;
    NDC.x = clipCoords.x / clipCoords.w;
    NDC.y = clipCoords.y / clipCoords.w;
    
    D3DXVECTOR3 screen;
    screen.x = (viewport.Width / 2) * (NDC.x + 1);
    screen.y = (viewport.Height / 2) * (1 - NDC.y);
    
    return screen;
}
```

### View Matrix Extraction
```
- From device constants
- Pattern scanning
- Engine-specific locations
- Reverse engineered addresses
```

## Debugging Tools

### PIX for Windows
- Frame capture and analysis
- GPU profiling
- Shader debugging

### RenderDoc
- Open-source frame debugger
- Multi-API support
- Resource inspection

### NVIDIA Nsight
- Performance analysis
- Shader debugging
- Frame profiling

## Anti-Screenshot Techniques

### How Anti-Cheat Captures Screenshots
```
- BitBlt from game window DC: captures visible content including overlays
- DXGI Desktop Duplication API: captures composited desktop output
- IDXGISwapChain::Present interception: grab backbuffer before present
- PrintWindow: capture specific window contents
- DirectX/Vulkan frame readback: copy render target to CPU-readable buffer
- Scheduled captures: random intervals to catch intermittent overlays
```

### Overlay Evasion Against Screenshot
```
- Disable overlay rendering during screenshot frame:
  - Detect screenshot by hooking BitBlt/PrintWindow in AC module
  - Suppress ImGui rendering for captured frame
- DWM composition tricks:
  - Render to a separate window that DWM excludes from capture
  - Use WDA_EXCLUDEFROMCAPTURE (SetWindowDisplayAffinity) on overlay window
- Hardware overlay planes:
  - Use IDXGIOutput::FindClosestMatchingMode + hardware overlay
  - Content on hardware overlay plane may not appear in software capture
- External rendering:
  - Render on secondary display or capture card output
  - OBS virtual camera trick: render to virtual camera feed
```

### Cheat-Side Anti-Screenshot (README > Anti Screenshot)
```
- Projects that detect and evade AC screenshot capture
- Techniques: hook Present to suppress overlay on screenshot frames
- DWM-based overlays that survive PrintWindow but not BitBlt
- Kernel-level: suppress screenshot by blocking DC access
```

## OBS Capture Pipeline and AI Visual Cheat Surface

### OBS Frame Capture Modes
```
OBS (Open Broadcaster Software) is the primary frame source for
AI visual cheats. Its capture modes have distinct detection profiles:

Game Capture (most common for cheats):
- Injects obs-graphics-hook64.dll into game process
- Hooks IDXGISwapChain::Present (D3D11/12) or SwapBuffers (OpenGL)
  or vkQueuePresentKHR (Vulkan) inside the game process
- Copies backbuffer to shared texture/memory each frame
- Lowest latency, highest quality (pre-composition, native resolution)
- Detection: DLL appears in game process module list;
  shared texture handle creation visible to kernel callbacks

Window Capture:
- Uses DXGI Desktop Duplication API (no injection into game)
- Captures composited window output from DWM
- Slightly higher latency (post-composition)
- Detection: IDXGIOutputDuplication usage from non-game process

Display Capture:
- Captures entire monitor output
- Highest latency, captures everything including overlays
- No per-process interaction

OBS Virtual Camera:
- Outputs captured frames as a virtual camera device
- Can feed AI model running in separate process or machine
- Detectable via virtual camera driver enumeration
```

### Frame Pipeline for AI Aimbot
```
Capture path (latency-critical):
  Game render → Present hook copies backbuffer
  → Shared GPU texture (ID3D11Texture2D, GPU-side)
  → GPU→CPU readback (staging texture + Map/Unmap)
  → CPU-side frame buffer (system memory)
  → Crop to ROI (Region of Interest, e.g., 640x640 around crosshair)
  → AI inference input (CUDA/TensorRT/DirectML)

OBS plugin form factor:
  AI model implemented as OBS video filter plugin
  → Receives frames through obs_source_frame callback
  → Runs inference in-process
  → Outputs mouse commands to hardware device
  → Appears as "OBS running a filter" to the system

Dual-machine pipeline:
  Game PC OBS → NDI (Network Device Interface) or capture card
  → Cheat PC receives video stream
  → AI inference on cheat PC GPU
  → Mouse commands sent via network to KMBox on game PC
  Latency: +5-15 ms for NDI, +2-5 ms for hardware capture card

Performance targets:
  Capture: < 5 ms (GPU shared texture copy)
  Crop + preprocess: < 2 ms
  YOLO inference: 5-15 ms (TensorRT FP16 on RTX 3060+)
  Coordinate calc + smoothing: < 1 ms
  Hardware input transmission: < 2 ms (USB) or < 5 ms (network)
  Total pipeline: 15-40 ms end-to-end
```

### Detection-Relevant Graphics Signals
```
- obs-graphics-hook64.dll in game process module list
- IDXGISwapChain::Present hook or detour in game process
- Staging texture creation at frame rate (ID3D11Texture2D with
  D3D11_USAGE_STAGING + CPU_ACCESS_READ created per frame)
- GPU-to-CPU memory copy bandwidth anomaly (Map/Unmap calls
  at 60+ FPS on backbuffer-sized resources)
- DXGI shared handle creation from game process to external process
- NDI SDK DLLs loaded (Processing.NDI.Lib.*.dll)
- Virtual camera driver (obs-virtualcam) registered
```

## Anti-Detection Considerations

### Present Hook Detection
```
- VTable integrity checks
- Code section verification
- Call stack analysis
- Module list scanning for known capture DLLs
```

### Evasion Techniques
```
- Trampoline hooks
- Hardware breakpoints
- Timing obfuscation
```

## Performance Optimization

### Best Practices
```
1. Minimize state changes
2. Batch draw calls
3. Use instancing
4. Cache resources
5. Profile regularly
```

### Common Issues
```
- Flickering: Double buffer sync
- Artifacts: Clear state properly
- Performance: Reduce overdraw
```

## Resource Organization

The README contains:
- DirectX 9/11/12 hook implementations
- OpenGL hook libraries
- Vulkan interception tools
- ImGui integration examples
- Overlay frameworks
- Shader modification tools

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
