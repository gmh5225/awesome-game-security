---
name: anti-cheat-systems
description: Guide for modern game anti-cheat architecture, Windows kernel monitoring, and detection tradeoffs. Use this skill when analyzing EAC, BattlEye, Vanguard, FACEIT AC, kernel callbacks, handle protection, manual-map detection, boot-start drivers, BYOVD, DMA threats, or behavioral telemetry in game security research.
---

# Anti-Cheat Systems & Analysis

## Overview

This skill covers layered anti-cheat design across kernel drivers, privileged services, in-game components, and backend telemetry. It is most useful for mapping how modern anti-cheats monitor process handles, image loads, memory integrity, driver trust, virtualization abuse, DMA threats, and suspicious input behavior on Windows.

## README Coverage

- `Anti Cheat > Guide`
- `Anti Cheat > Stress Testing`
- `Anti Cheat > Driver Unit Test Framework`
- `Anti Cheat > Anti Debugging`
- `Anti Cheat > Page Protection`
- `Anti Cheat > Binary Packer`
- `Anti Cheat > CLR Protection`
- `Anti Cheat > Anti Disassembly`
- `Anti Cheat > Sample Unpacker`
- `Anti Cheat > Dump Fix`
- `Anti Cheat > Encrypt Variable`
- `Anti Cheat > Lazy Importer`
- `Anti Cheat > Anti-Cheat Programming`
- `Anti Cheat > Compile Time`
- `Anti Cheat > Shellcode Engine & Tricks`
- `Anti Cheat > Obfuscation Engine`
- `Anti Cheat > Screenshot`
- `Anti Cheat > Game Engine Protection:*`
- `Anti Cheat > Open Source Anti Cheat System`
- `Anti Cheat > Analysis Framework`
- `Anti Cheat > Detection:*`
- `Anti Cheat > Signature Scanning`
- `Anti Cheat > Information System & Forensics`
- `Anti Cheat > Dynamic Script`
- `Anti Cheat > Kernel Mode Winsock`
- `Anti Cheat > Fuzzer`
- `Anti Cheat > Windows Ring3 Callback`
- `Anti Cheat > Windows Ring0 Callback`
- `Anti Cheat > Winows User Dump Analysis`
- `Anti Cheat > Winows Kernel Dump Analysis`
- `Anti Cheat > Sign Tools`
- `Anti Cheat > Backup File / Backup Drivers`
- `Anti Cheat > Black Signature`
- `Windows Security Features`

## Major Anti-Cheat Systems

### Easy Anti-Cheat (EAC)
- Multi-component architecture with service, driver, and game-facing protections
- Process integrity verification and memory inspection
- Runtime driver loading with strong client-side enforcement
- Used by: Fortnite, Apex Legends, Rust

### BattlEye
- Kernel driver plus service and game module coordination
- Handle protection, process monitoring, and memory scanning
- Strong focus on injected code and runtime tampering visibility
- Used by: PUBG, Rainbow Six Siege, DayZ

### Vanguard (Riot Games)
- Boot-start kernel driver with early visibility into later-loaded drivers
- Boot-time initialization
- Driver allowlisting and aggressive system trust checks
- Used by: Valorant, League of Legends

### FACEIT AC
- Kernel-level competitive anti-cheat with strong process and driver monitoring
- Emphasis on platform integrity and low tolerance for hostile drivers
- Often discussed alongside Vanguard in kernel anti-cheat research

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
- Code section hashing and integrity verification
- Executable private memory and manual-map detection
- Injected module and anomalous image mapping detection
- Memory modification and stack provenance monitoring
```

### Process Detection
```
- Handle access stripping and protected-process enforcement
- Thread start address, APC, and context inspection
- Debug register and hidden-thread monitoring
- Stack trace and module-correlation analysis
```

### Kernel-Level Detection
```
- Driver verification, signature policy, and blocklist checks
- Callback registration and object access monitoring
- System call, dispatch table, and hook integrity checks
- PatchGuard, test-signing, and kernel trust state checks
```

### Behavioral Analysis
```
- Raw input timing and pattern analysis
- Movement and aim anomaly detection
- Statistical improbability and ML-assisted scoring
- Telemetry collection and server-side review
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
- Hypervisor and driver trust detection
- VAD and executable memory inspection

### Hypervisor-Level Components
```
- EPT-based memory access monitoring
- Callback list write protection via EPT hooks
- ETW structure integrity enforcement
- AC driver code page protection (prevent patching)
- VMCALL interface for policy configuration from kernel driver
- VM exit handlers for EPT violations on protected regions
```

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
4. Map callback registrations and trust boundaries

### Dynamic Analysis
1. Monitor system calls
2. Track driver communications
3. Inspect memory layout and module provenance
4. Debug with kernel or hypervisor tools

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
- TPM-backed attestation considerations

### Virtualization Detection
- VT-x/AMD-V detection
- Hypervisor presence checks
- VM escape detection
- Timing-based detection

### Hypervisor-Based Defense for Anti-Cheat
```
Concept:
- Use hypervisor (EPT/SLAT) to enforce anti-cheat protections
  from a privilege level above the kernel
- Even if attacker achieves kernel R/W (BYOVD, exploit),
  hypervisor-level enforcement remains intact
- EPT hooks replace traditional kernel hooks:
  operate outside the guest OS, invisible to kernel-level rootkits

EPT Hook Protection Targets:
- Anti-cheat driver executable pages
  → Prevents attackers from patching AC driver code in memory
- Kernel callback lists (PsSetCreateProcessNotifyRoutine, ObRegisterCallbacks)
  → Write authorization moved to hypervisor; kernel-level callback removal denied
- ETW-related structures
  → Unauthorized writes trigger EPT violations, caught by hypervisor
- EPP/AC process memory
  → Protects security software from silent tampering

Hypervisor vs Kernel-Level Threats:
- Common kernel-level attack chain:
  1. Attacker uses BYOVD or kernel exploit for R/W primitives
  2. Patches callbacks to remove AC notifications
  3. Tampers with ETW to disable telemetry
  4. Modifies AC driver code to blind detection
- With hypervisor defense:
  1. Same kernel R/W primitives obtained
  2. Write to protected callback list → EPT violation → VM exit
  3. Hypervisor evaluates context and denies unauthorized modification
  4. AC callbacks and telemetry remain intact

Advantages:
- Higher privilege than kernel — cannot be disabled by kernel rootkits
- Transparent to guest: no kernel patches needed
- Effective even after full kernel compromise
- Complements existing kernel-mode detection (callbacks, signatures, scans)

Limitations:
- Requires hardware virtualization support (VT-x/AMD-V)
- Performance overhead from VM exits on protected region access
- Complexity: must handle nested virtualization (VMware, Hyper-V)
- DMA attacks bypass hypervisor memory protections (separate threat)
```

## Code Protection Techniques

### Page Protection
```
- Executable page guard pages and trap-based integrity monitoring
- NX bit enforcement and DEP policy
- PAGE_GUARD + single-step trap for code coverage without patching
- VirtualProtect monitoring to detect runtime permission changes
```

### Binary Packing & Encryption
```
- PE packers: UPX, Themida, VMProtect, Enigma, MPRESS
- CLR protection: .NET obfuscation (ConfuserEx, Dotfuscator, .NET Reactor)
- Encrypt Variable: runtime value encryption to frustrate memory scanners
- Lazy Importer: compile-time import hiding to avoid IAT-based detection
- Compile-time techniques: string encryption, constexpr obfuscation, COFF obfuscation
```

### Shellcode & Obfuscation
```
- Shellcode engines: position-independent code generation, syscall stubs
- Obfuscation engines: OLLVM-based, custom LLVM passes, MBA (Mixed Boolean-Arithmetic)
- Anti-disassembly: opaque predicates, junk code insertion, control flow flattening
```

## Heartbeat & Screenshot

### Heartbeat Mechanisms
```
- Periodic client-to-server health check packets
- Encrypted challenge-response with server nonce
- Timing-based integrity: detect suspended or debugged processes
- Failure modes: silent disconnect, delayed ban, immediate kick
```

### Screenshot Capture
```
- AC-initiated screen capture for manual or automated review
- BitBlt / PrintWindow / DXGI desktop duplication
- Anti-screenshot evasion: overlay hiding, DWM composition bypass
- Server-side ML classifiers for ESP/overlay detection in captured frames
```

## Telemetry Pipeline

### Client-Side Collection
```
- Module list enumeration and hash reporting
- Handle table snapshots for suspicious access patterns
- Stack trace sampling at periodic intervals
- Driver load events and callback registration state
- Hardware fingerprint (disk serial, NIC MAC, SMBIOS, GPU)
```

### Transport & Server-Side
```
- Encrypted telemetry channel (TLS + custom encryption layer)
- Server-side aggregation and anomaly scoring
- ML-based behavioral clustering for ban waves
- Replay system integration for suspicious session review
```

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
