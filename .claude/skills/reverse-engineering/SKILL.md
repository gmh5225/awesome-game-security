---
name: reverse-engineering-tools
description: Guide for reverse engineering protected games and anti-cheat components across user mode, kernel mode, and hypervisor-aware environments. Use this skill when analyzing drivers, IOCTL protocols, callback registration, injected-code artifacts, integrity checks, protected binaries, or debugging security-sensitive game components.
---

# Reverse Engineering Tools & Techniques

## Overview

This skill covers reverse engineering workflows for game security research, including protected game clients, anti-cheat user-mode modules, kernel drivers, memory artifacts, and debugging environments that must survive anti-analysis checks.

## README Coverage

- `Cheat > Debugging`
- `Cheat > RE Tools`
- `Cheat > Mixed boolean-arithmetic`
- `Cheat > Dynamic Binary Instrumentation`
- `Cheat > Fix VMP`
- `Cheat > Fix Themida`
- `Cheat > Fix OLLVM`
- `Cheat > Virtual Environments`
- `Cheat > Decompiler`
- `Cheat > IDA themes`
- `Cheat > IDA Plugins`
- `Cheat > IDA Signature Database`
- `Cheat > Binary Ninja Plugins`
- `Cheat > Ghidra Plugins`
- `Cheat > Radare Plugins`
- `Cheat > Windbg Plugins`
- `Cheat > X64DBG Plugins`
- `Cheat > Cheat Engine Plugins`
- `Cheat > ROP Finder`
- `Cheat > ROP Generation`
- `Anti Cheat > Anti Debugging`
- `Anti Cheat > Anti Disassembly`
- `Anti Cheat > Dump Fix`
- `Anti Cheat > Sample Unpacker`
- `Anti Cheat > Obfuscation Engine`
- `Anti Cheat > Winows User Dump Analysis`
- `Anti Cheat > Winows Kernel Dump Analysis`

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

### Exception-Driven Lightweight DBI (Trap-and-Emulate)
```
Concept:
- Replace branch instructions with fault-generating sentinel opcodes
- Catch the resulting exception → emulate the original branch → log → resume
- Full cycle: patch → fault → capture → emulate → record → restore → continue

Sentinel Selection:
- HLT (0xF4) for ret → triggers STATUS_PRIVILEGED_INSTRUCTION
- SALC (0xD6) for jmp/jcc/call → triggers STATUS_ILLEGAL_INSTRUCTION
- Avoids INT3 (0xCC) which anti-debug/integrity checks commonly scan for
- Different sentinels can multiplex branch types

Exception Capture:
- Hook KiUserExceptionDispatcher (not VEH/SEH) for lowest-latency interception
- Assembly stub tail-calls into RtlDispatchException
- Handler dispatches by exception code to custom emulation logic

Branch Emulation Engine:
- Disassemble original (pre-patch) instruction at fault RIP
- jcc: 16-condition lookup table (ZF, SF, CF, OF, PF combinations)
- Direct call: push return address, update RIP
- Indirect branch: resolve effective address (register, memory, SIB, RIP-relative)
- ret: pop return address from stack, handle ret imm16 (extra pop)
- loop/jrcxz: decrement RCX, conditional branch

Instrumentation Strategies:
- Bounded Bulk Patching: scan a window from seed address, patch all branches
  → Simple but detectable by integrity checks
- Branch Chasing: patch only current branch, re-instrument at target on fault
  → Minimal memory footprint, highest stealth, best for unknown binaries
- CFG-Guided Patching: recursive-descent static CFG + chasing for unreached edges
  → Best coverage/safety balance

Integrity Check Evasion:
- PAGE_GUARD + Trap Flag (single-step) instead of direct code patching
- Trigger guard page exception → set TF → single-step through original instruction
- Avoids modifying .text section (defeats hash-based integrity checks)
```

### Control Flow Tracing (CFT) Applications
```
- Runtime call graph generation with register context at each edge
- Divergence testing: compare traces across different inputs/environments
  → Quickly locates input validation, anti-debug, anti-tamper trigger points
- Deobfuscation: resolve all indirect branches in virtualized code
- Hot path analysis, branch coverage measurement
- Performance: ~600x slowdown (exception per branch), not suitable for
  timing-sensitive targets (rdtsc checks, session timeouts)
- Portable to other architectures: ARM (UDF), RISC-V (illegal instruction)
```

### User-Mode Hypervisor-Assisted Tracing
```
Concept:
- Use Windows Hypervisor Platform (WHP) API to run guest code in user mode
- No kernel driver required — standard user-mode process hosts the hypervisor
- Map host memory pages into guest address space
- Configure page-level traps (read/write/execute permissions per page)
- Guest execution triggers VM exits on configured events

Trap-Driven Execution:
- Page fault traps: set per-page R/W/X permissions via EPT-equivalent API
  → Execute fault = code coverage, Write fault = memory write monitoring
  → Read fault = data access tracking
- CPUID interception: guest executes CPUID → VM exit → host decides response
  → Useful for fingerprinting guest environment queries
- Syscall interception: guest executes syscall → VM exit → host emulates
  → Controlled experiments without real kernel interaction

Workflow:
1. Prepare initial CPU state (registers, segments, control registers)
2. Map target code + data pages with desired permissions
3. Enter guest execution loop
4. On VM exit: inspect reason, handle trap, optionally modify state
5. Resume or terminate guest

Advantages:
- Pure user-mode: no driver signing, no PatchGuard concerns
- Deterministic: full control over guest memory and execution
- Composable: combine with disassemblers/emulators for hybrid analysis
- Debuggable: host process can be debugged normally

Limitations:
- Requires hardware virtualization support (VT-x/AMD-V)
- Windows-specific (WHP API is Windows 10+)
- Cannot run full OS — suited for code snippets and function-level analysis
- Nested virtualization considerations when host is already a VM
```

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

## Obfuscation Taxonomy

### Mixed Boolean-Arithmetic (MBA)
```
- Linear MBA: e.g., x + y = (x ^ y) + 2*(x & y)
- Polynomial MBA: higher-degree expressions over boolean/arithmetic mix
- Tools: SSPAM, MBA-Blast, SiMBA for simplification
- Common in: VMProtect, Themida, custom LLVM passes
```

### Control Flow Flattening (CFF)
```
- OLLVM-style: all basic blocks behind a dispatcher switch
- Recovery: symbolic execution, pattern matching, deobfuscation passes
- Tools: D-810 (IDA), de-ollvm scripts, SATURN
- Variants: nested dispatchers, encrypted state variables
```

### Opaque Predicates
```
- Invariant conditions injected to confuse static analysis
- Number-theoretic (x² mod 4 ∈ {0,1}), pointer-aliasing based
- Detection: abstract interpretation, SMT solvers (Z3)
```

### Virtualization-Based Obfuscation
```
VMProtect / Themida / Code Virtualizer:
- Custom bytecode VM with randomized opcode set per build
- Handler table dispatch loop: fetch → decode → execute
- Devirtualization approaches:
  - Trace-based: record handler execution, lift to IR
  - Pattern-based: identify handler semantics by structure
  - Symbolic: concolic execution through VM dispatch
- Tools: VMPAttack, NoVmp, Oreans UnVirtualizer, vtil
```

### Binary Lifting
```
- Lift machine code to compiler IR (LLVM IR, VEX, ESIL)
- Enables compiler-level optimization passes for deobfuscation
- Tools: McSema, remill, RetDec, Binary Ninja MLIL/HLIL
```

## Disassembler Plugin Ecosystem

### IDA Pro Plugins
```
Categories found in README (> IDA Plugins, 150+ entries):
- Decompiler enhancers: HexRaysPyTools, HRDevHelper
- Type recovery: ClassInformer, auto_struct
- Signature: FLIRT, Lumina, IDA Signature Database
- Scripting: IDAPython, IDC, LazyIDA
- Visualization: IDAGraph, Lighthouse (coverage)
- Anti-obfuscation: D-810 (MBA), de-ollvm, Patfinder
- Game-specific: SDK loaders, structure importers
```

### Binary Ninja Plugins
```
- Sidekick, snippets, type libraries
- HLIL-based analysis scripts
- Custom architectures and loaders
- Headless analysis for batch processing
```

### Ghidra Plugins
```
- GhidraScript (Java/Python), Ghidra extensions
- Ghidraaas (Ghidra-as-a-Service)
- Type importers, signature matchers
- Firmware analysis (SVD loader, embedded)
```

### Radare2 / iaito Plugins
```
- r2pipe scripting (Python, JS, Rust)
- iaito: official radare2 Qt GUI
- r2ghidra: Ghidra decompiler integration
- r2dec: lightweight decompiler
```

### WinDbg Plugins
```
- SwishDbgExt, WinDbgX
- Time Travel Debugging (TTD) extensions
- !analyze extensions, custom formatters
- Kernel debugging helpers
```

### x64dbg Plugins
```
- ScyllaHide (anti-anti-debug)
- TitanEngine, x64dbgpy
- Trace plugins, pattern scanners
- Conditional breakpoint scripts
```

### Cheat Engine Plugins
```
- Mono/IL2CPP helpers
- Auto-assembler templates
- Structure dissectors
- Pointer scanner extensions
```

## MCP-Based RE Tools

```
The README's MCP server section and RE tool ecosystem now include
AI-assisted reverse engineering through Model Context Protocol:

- IDA MCP: AI agent controls IDA Pro (rename, annotate, navigate)
- Ghidra MCP: AI agent queries Ghidra decompilation and PCODE
- Binary Ninja MCP: AI agent interacts with Binary Ninja API
- radare2 MCP: AI agent drives r2 sessions via r2pipe
- x64dbg MCP: AI agent controls live debugging sessions

Workflow: LLM ↔ MCP server ↔ RE tool, enabling natural-language
queries like "find all functions calling CreateRemoteThread" or
"rename this function based on its decompiled logic"
```

## Binary Diffing

```
Tools for comparing binary versions (patch analysis, vulnerability research):
- BinDiff (Google): graph-based structural comparison
- Diaphora: IDA plugin, best open-source binary diff
- ghidriff: Ghidra-based diffing, command-line and scriptable
- DarunGrim: patch analysis focused differ
- turbodiff: lightweight IDA diffing plugin

Use cases in game security:
- Tracking anti-cheat driver updates between versions
- Identifying patched vulnerabilities in game clients
- Comparing obfuscated builds to isolate logic changes
```

## Anti-Debug Techniques Catalog

### User-Mode Anti-Debug
```
- IsDebuggerPresent / CheckRemoteDebuggerPresent
- NtQueryInformationProcess (ProcessDebugPort, ProcessDebugFlags, ProcessDebugObjectHandle)
- NtSetInformationThread (ThreadHideFromDebugger)
- PEB.BeingDebugged, PEB.NtGlobalFlag, heap flags
- INT 2D, INT 3 scanning, OutputDebugString tricks
- Timing checks: rdtsc, QueryPerformanceCounter, GetTickCount64
- TLS callbacks for early detection
- Exception-based: unhandled exception filter, VEH chain inspection
- Parent process checks (csrss.exe verification)
- Self-debugging: NtCreateDebugObject
```

### Kernel-Mode Anti-Debug
```
- KdDebuggerEnabled / KdDebuggerNotPresent
- Debug register (DR0-DR7) monitoring and clearing
- KPROCESS.DebugPort zeroing
- NMI callbacks for debugger detection
- Hardware breakpoint detection via context inspection
```

### Anti-Debug Bypass Tools
```
- ScyllaHide: comprehensive anti-anti-debug (x64dbg/IDA/standalone)
- TitanHide: kernel-mode debugger hiding
- HyperHide: hypervisor-based anti-debug bypass
- SharpOD: OllyDbg anti-anti-debug plugin
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
