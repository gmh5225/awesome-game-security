---
name: anti-cheat-systems
description: Guide for understanding anti-cheat systems and bypass techniques. Use this skill when researching game protection systems (EAC, BattlEye, Vanguard), anti-cheat architecture, detection methods, or bypass strategies.
---

# Anti-Cheat Systems & Analysis

## Overview

This skill covers anti-cheat systems used in games, their detection mechanisms, and research techniques. Understanding anti-cheat helps both defenders (game developers) and security researchers.

## Major Anti-Cheat Systems

### Easy Anti-Cheat (EAC)
- Kernel-mode driver protection
- Process integrity verification
- Memory scanning
- Used by: Fortnite, Apex Legends, Rust

### BattlEye
- Kernel driver with ring-0 access
- Screenshot capture capability
- Network traffic analysis
- Used by: PUBG, Rainbow Six Siege, DayZ

### Vanguard (Riot Games)
- Always-on kernel driver
- Boot-time initialization
- Hypervisor detection
- Used by: Valorant, League of Legends

### Valve Anti-Cheat (VAC)
- User-mode detection
- Signature-based scanning
- Delayed ban waves
- Used by: CS2, Dota 2, TF2

### Other Systems
- **PunkBuster**: Legacy FPS anti-cheat
- **FairFight**: Server-side statistical analysis
- **nProtect GameGuard**: Korean anti-cheat solution
- **XIGNCODE3**: Mobile game protection
- **ACE (Tencent)**: Chinese market protection

## Detection Mechanisms

### Memory Detection
```
- Signature scanning for known cheats
- Code integrity verification
- Injected module detection
- Memory modification monitoring
```

### Process Detection
```
- Handle enumeration
- Thread context inspection
- Debug register monitoring
- Stack trace analysis
```

### Kernel-Level Detection
```
- Driver verification
- Callback registration monitoring
- System call hooking detection
- PatchGuard integration
```

### Behavioral Analysis
```
- Input pattern analysis
- Movement anomaly detection
- Statistical improbability flagging
- Network packet inspection
```

## Anti-Cheat Architecture

### User-Mode Components
- Process scanner
- Module verifier
- Overlay detector
- Screenshot capture

### Kernel-Mode Components
- Driver loader
- Memory protection
- System callback registration
- Hypervisor detection

### Server-Side Components
- Statistical analysis
- Replay verification
- Report processing
- Ban management

## Research Techniques

### Static Analysis
1. Dump and analyze AC drivers
2. Reverse engineer detection routines
3. Identify signature patterns
4. Map callback registrations

### Dynamic Analysis
1. Monitor system calls
2. Track driver communications
3. Analyze network traffic
4. Debug with hypervisor tools

## Bypass Categories

### Memory Access
- Physical memory read/write
- DMA-based access
- Hypervisor memory virtualization
- Driver-based access

### Code Execution
- Manual mapping
- Thread hijacking
- APC injection
- Kernel callbacks

### Detection Evasion
- Signature mutation
- Timing attack mitigation
- Stack spoofing
- Module hiding

## Security Features Interaction

### Windows Security
- Driver Signature Enforcement (DSE)
- PatchGuard/Kernel Patch Protection
- Hypervisor Code Integrity (HVCI)
- Secure Boot

### Virtualization
- VT-x/AMD-V detection
- Hypervisor presence checks
- VM escape detection
- Timing-based detection

## Ethical Considerations

### Research Guidelines
- Focus on understanding, not exploitation
- Report vulnerabilities responsibly
- Respect Terms of Service implications
- Consider impact on gaming communities

### Legal Aspects
- DMCA considerations
- CFAA implications
- Regional regulations
- ToS enforcement

## Resources Organization

### Detection Research
```markdown
- Anti-cheat driver analysis
- Detection routine documentation
- Callback enumeration tools
```

### Bypass Research
```markdown
- Memory access techniques
- Injection methods
- Evasion strategies
```

### Tools
```markdown
- Custom debuggers
- Driver loaders
- Analysis frameworks
```
