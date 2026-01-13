---
name: mobile-security
description: Guide for mobile game security on Android and iOS platforms. Use this skill when working with Android/iOS reverse engineering, mobile game hacking, APK analysis, root/jailbreak detection bypass, or mobile anti-cheat systems.
---

# Mobile Game Security

## Overview

This skill covers mobile security resources from the awesome-game-security collection, focusing on Android and iOS game security research, reverse engineering, and protection bypass techniques.

## Android Security

### APK Analysis

#### Tools
- **apktool**: Decompile/recompile APKs
- **jadx**: DEX to Java decompiler
- **APKiD**: Identify packers/protectors
- **Frida**: Dynamic instrumentation
- **APKLab**: VS Code integration

#### Workflow
```bash
# Decompile APK
apktool d game.apk

# Analyze DEX files
jadx -d output game.apk

# Identify protection
apkid game.apk
```

### Native Library Analysis

#### IL2CPP Games (Unity)
```
1. Extract libil2cpp.so from APK
2. Use IL2CPP Dumper to generate headers
3. Analyze with IDA/Ghidra
4. Hook using Frida or native hooks
```

#### Native Games
```
1. Identify target libraries (.so files)
2. Analyze with reverse engineering tools
3. Pattern scan for functions
4. Apply hooks/patches
```

### Memory Manipulation

#### Tools
- **GameGuardian**: Memory editor
- **Cheat Engine (ceserver)**: Remote debugging
- **Custom memory tools**: Direct /proc/pid/mem access

#### Access Methods
```c
// Via /proc filesystem
int fd = open("/proc/pid/mem", O_RDWR);
pread64(fd, buffer, size, address);
pwrite64(fd, buffer, size, address);
```

### Hooking Frameworks

#### Frida
```javascript
// Basic function hook
Interceptor.attach(Module.findExportByName("libgame.so", "function_name"), {
    onEnter: function(args) {
        console.log("Called with: " + args[0]);
    },
    onLeave: function(retval) {
        retval.replace(0);
    }
});
```

#### Native Hooks
- **Substrate**: Inline hooking framework
- **And64InlineHook**: ARM64 inline hooks
- **xHook**: PLT hook library
- **Dobby**: Multi-platform hook framework

### Root Detection Bypass

#### Common Checks
```
- /system/bin/su existence
- /system/xbin/su existence  
- Build.TAGS contains "test-keys"
- ro.build.selinux property
- Magisk files/folders
- Package manager checks
```

#### Bypass Methods
- **Magisk Hide**: Built-in root hiding
- **LSPosed/EdXposed**: Xposed framework hooks
- **Frida scripts**: Hook detection functions
- **APK patching**: Remove detection code

### Zygisk Modules

```cpp
// Zygisk module structure
class Module : public zygisk::ModuleBase {
    void onLoad(zygisk::Api *api, JNIEnv *env) override {
        this->api = api;
        this->env = env;
    }
    
    void preAppSpecialize(zygisk::AppSpecializeArgs *args) override {
        // Before app loads
    }
    
    void postAppSpecialize(const zygisk::AppSpecializeArgs *args) override {
        // After app loads - inject here
    }
};
```

### Android Protections

#### Common Protectors
- **Tencent ACE**: Chinese market protection
- **AppSealing**: Commercial protection
- **DexGuard/ProGuard**: Obfuscation
- **Arxan**: Enterprise protection

## iOS Security

### Analysis Tools
- **Hopper**: Disassembler
- **IDA Pro**: Industry standard
- **class-dump**: Objective-C header extraction
- **Frida**: Dynamic instrumentation
- **Clutch/dumpdecrypted**: App decryption

### Jailbreak Tools
- **H5GG**: iOS cheat engine
- **Flex**: Runtime patching
- **Cycript**: Runtime manipulation
- **ceserver-ios**: Cheat Engine for iOS

### Hooking (Jailbroken)
```objc
// Using Logos (Theos)
%hook TargetClass
- (int)targetMethod:(int)arg {
    int result = %orig;
    return result * 2;  // Modify return
}
%end
```

### Non-Jailbreak Techniques
- **Sideloading**: Modified IPAs
- **Enterprise certificates**: Custom signing
- **AltStore**: Self-signing tool

## Unity Mobile Games

### IL2CPP Analysis
```
1. Locate libil2cpp.so (Android) or UnityFramework (iOS)
2. Find global-metadata.dat
3. Run IL2CPPDumper
4. Generate SDK/headers
5. Hook target functions
```

### Mono Analysis
```
1. Extract managed DLLs
2. Decompile with dnSpy/ILSpy
3. Modify and repackage
4. Or hook at runtime
```

### Common Targets
```
- Currency/coins values
- Player stats (health, damage)
- Inventory manipulation
- Premium unlocks
- Ad removal
```

## Unreal Mobile Games

### Analysis Approach
```
1. Identify UE version
2. Dump SDK using appropriate tool
3. Locate GObjects, GNames
4. Find target functionality
5. Apply memory patches or hooks
```

## Overlay Rendering (Android)

### Surface-Based
```cpp
// Native surface overlay
ANativeWindow* window = ANativeWindow_fromSurface(env, surface);
// Render using OpenGL ES or Vulkan
```

### ImGui Integration
- Zygisk + ImGui modules
- Surface hijacking
- Direct framebuffer access

## Network Analysis

### Tools
- **mitmproxy**: MITM proxy
- **Charles Proxy**: Traffic analysis
- **Frida SSL bypass**: Certificate pinning bypass

### Certificate Pinning Bypass
```javascript
// Frida universal SSL bypass
Java.perform(function() {
    var TrustManager = Java.registerClass({
        implements: [X509TrustManager],
        methods: {
            checkClientTrusted: function() {},
            checkServerTrusted: function() {},
            getAcceptedIssuers: function() { return []; }
        }
    });
    // Install custom TrustManager
});
```

## Anti-Cheat on Mobile

### Common Systems
- **Tencent ACE**: Chinese games
- **NetEase Protection**: NetEase games
- **Custom solutions**: Per-game implementations

### Detection Methods
```
- Root/jailbreak detection
- Frida detection
- Emulator detection
- Integrity checks
- Debugger detection
- Hook detection
```

### Bypass Strategies
```
1. Static analysis of detection code
2. Hook detection functions
3. Hide injection footprint
4. Timing attack consideration
5. Clean environment emulation
```

## Emulator Considerations

### Android Emulators
- **LDPlayer**: Gaming focused
- **BlueStacks**: Popular emulator
- **NoxPlayer**: Game optimization
- **MEmu**: Android gaming

### Emulator Detection
```
- Build.FINGERPRINT checks
- Hardware sensor verification
- File system characteristics
- Performance timing
```

## Resource Organization

The README contains:
- Android hooking frameworks
- iOS jailbreak tools
- Memory manipulation utilities
- Root/jailbreak bypass tools
- Mobile anti-cheat research
- Emulator resources
