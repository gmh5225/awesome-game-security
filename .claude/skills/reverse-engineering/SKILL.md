---
name: reverse-engineering-tools
description: Guide for reverse engineering tools and techniques used in game security research. Use this skill when working with debuggers, disassemblers, memory analysis tools, binary analysis, or decompilers for game security research.
---

# Reverse Engineering Tools & Techniques

## Overview

This skill covers reverse engineering resources for game security research, including debuggers, disassemblers, memory analysis tools, and specialized game hacking utilities.

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
4. Map out key modules and dependencies
```

### Deep Analysis
```
1. Locate target functionality
2. Trace execution flow
3. Document structures and relationships
4. Develop hooking strategy
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

**Important**: This skill provides conceptual guidance and overview information. For detailed information including:
- Specific GitHub repository links
- Complete project lists with descriptions
- Up-to-date tools and resources
- Code examples and implementations

**Please fetch the complete data from the main repository:**
```
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md
```

The main README contains thousands of curated links organized by category. When users ask for specific tools, projects, or implementations, retrieve and reference the appropriate sections from this source.
