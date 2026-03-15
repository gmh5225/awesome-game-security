---
name: reverse-engineering-tools
description: Guide for reverse engineering protected games and anti-cheat components across user mode, kernel mode, and hypervisor-aware environments. Use this skill when analyzing drivers, IOCTL protocols, callback registration, injected-code artifacts, integrity checks, protected binaries, or debugging security-sensitive game components.
---

# Reverse Engineering Tools & Techniques

## Overview

This skill covers reverse engineering workflows for game security research, including protected game clients, anti-cheat user-mode modules, kernel drivers, memory artifacts, and debugging environments that must survive anti-analysis checks.

## Debugging Tools

### Windows Debuggers
- **Cheat Engine**: Memory scanner and debugger for games
- **x64dbg**: Open-source x86/x64 debugger
- **WinDbg**: Microsoft's kernel/user-mode debugger
- **ReClass.NET**: Memory structure reconstruction
- **HyperDbg**: Hypervisor-based debugger

### Specialized Debuggers
- **CE Mono Helper**: Unity/Mono game debugging
- **dnSpy**: .NET assembly debugger/decompiler
- **ILSpy**: .NET decompiler
- **frida**: Dynamic instrumentation toolkit

### Platform-Specific
- **edb-debugger**: Linux debugger
- **PINCE**: Linux game hacking tool
- **H5GG**: iOS cheat engine
- **Hardware Breakpoint Tools**: HWBP implementations

## Disassembly & Decompilation

### Multi-Platform
- **IDA Pro**: Industry standard disassembler
- **Ghidra**: NSA's reverse engineering framework
- **Binary Ninja**: Modern RE platform
- **Cutter**: Radare2 GUI

### Specialized Tools
- **IL2CPP Dumper**: Unity IL2CPP analysis
- **dnSpy**: .NET/Unity decompilation
- **jadx**: Android DEX decompiler
- **Recaf**: Java bytecode editor

## Memory Analysis

### Memory Scanners
```
- Cheat Engine: Pattern scanning, value searching
- ReClass.NET: Structure reconstruction
- Process Hacker: System analysis
```

### Dump Tools
```
- KsDumper: Kernel-space process dumping
- PE-bear: PE file analysis
- ImHex: Hex editor for RE
```

## Dynamic Binary Instrumentation (DBI)

### Frameworks
- **Frida**: Cross-platform DBI
- **DynamoRIO**: Runtime code manipulation
- **Pin**: Intel's DBI framework
- **TinyInst**: Lightweight instrumentation
- **QBDI**: QuarkslaB DBI

### Use Cases
1. API hooking and tracing
2. Code coverage analysis
3. Fuzzing harness creation
4. Behavioral analysis
5. Driver IOCTL and callback tracing

## Anti-Analysis Bypass

### Techniques
- Anti-debug detection bypass
- VM/Sandbox evasion
- Timing attack mitigation
- PatchGuard circumvention

### Tools
- **TitanHide**: Anti-debug hiding
- **HyperHide**: Hypervisor-based hiding
- **ScyllaHide**: Anti-anti-debug plugin

## Game-Specific Analysis

### Unity Games
1. Locate `GameAssembly.dll` (IL2CPP) or managed DLLs
2. Use IL2CPP Dumper for structure recovery
3. Apply dnSpy for Mono games
4. Hook via Unity-specific frameworks

### Unreal Engine Games
1. Identify UE version from signatures
2. Use SDK generators (Dumper-7)
3. Analyze Blueprint bytecode
4. Hook UObject/UFunction systems

### Native Games
1. Standard PE analysis
2. Import/export reconstruction
3. Pattern scanning for signatures
4. Runtime memory analysis

## Workflow Best Practices

### Initial Analysis
```
1. Identify protections (packer, obfuscator, anti-cheat)
2. Determine game engine and version
3. Collect symbol information if available
4. Map out key modules, callbacks, and trust boundaries
```

### Deep Analysis
```
1. Locate target functionality
2. Trace execution flow
3. Document structures, memory artifacts, and relationships
4. Correlate IOCTLs, callbacks, and runtime checks
```

## VMProtect/Themida Analysis

### Resources
- Devirtualization tools
- Control flow recovery
- Handler analysis techniques
- Unpacking methodologies

## ROP/Exploit Development

### Tools
- **ROPgadget**: Gadget finder
- **rp++**: Fast ROP gadget finder
- **angrop**: Automated ROP chain generation

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
