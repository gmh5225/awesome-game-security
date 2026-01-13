---
name: graphics-api-hooking
description: Guide for graphics API hooking and rendering techniques for DirectX, OpenGL, and Vulkan. Use this skill when working with graphics hooks, overlay rendering, shader manipulation, or game rendering pipeline analysis.
---

# Graphics API Hooking & Rendering

## Overview

This skill covers graphics API resources from the awesome-game-security collection, including DirectX, OpenGL, and Vulkan hooking techniques, overlay rendering, and graphics debugging.

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

## Anti-Detection Considerations

### Present Hook Detection
```
- VTable integrity checks
- Code section verification
- Call stack analysis
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
