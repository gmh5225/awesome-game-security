---
name: dma-attack-techniques
description: Guide for PCIe DMA threat modeling, FPGA-based memory access, and defensive implications in game security. Use this skill when researching pcileech, BAR and TLP behavior, page-table walking, IOMMU or VT-d, device impersonation, firmware mimicry, or DMA detection and mitigation in game security research.
---

# DMA Attack Techniques

## Overview

This skill covers Direct Memory Access research from the awesome-game-security collection, focusing on FPGA-based PCIe attacks, pcileech usage, physical-memory access workflows, and the defensive limits of software anti-cheat once a hostile device can read memory below the OS.

## DMA Fundamentals

### What is DMA Attack?
```
DMA attacks exploit the ability of PCIe devices to directly access
system memory without CPU involvement. An attacker can:
- Read arbitrary physical memory
- Write to physical memory
- Bypass software-based protections
- Remain invisible to OS-level detection
```

### Hardware Requirements
```
- FPGA development board (Xilinx/Altera)
- PCIe interface capability
- Sufficient logic resources
- Development environment
```

## Defensive Context

### Why DMA Matters for Anti-Cheat
```
- No hostile process needs to exist on the game PC
- No suspicious driver or injected module is required
- Reads can occur from a second machine over PCIe-attached hardware
- Traditional kernel callbacks and handle protection do not see the access
```

### Key Defensive Constraints
```
- IOMMU / VT-d policy determines whether DMA can access arbitrary memory
- Device impersonation can blur the line between legitimate hardware and FPGA firmware
- Secure Boot and TPM help with platform trust, but do not eliminate physical DMA risk
- Enumeration-based detection is useful but not sufficient against good firmware mimicry
```

## pcileech Framework

### Overview
pcileech is the primary framework for DMA-based memory access:
- Open-source memory forensics tool
- Supports multiple FPGA boards
- Extensive plugin ecosystem
- Active development community

### Supported Hardware
```
- Screamer PCIe (Xilinx Artix-7)
- PCIe Squirrel
- AC701 (Xilinx Artix-7)
- SP605 (Xilinx Spartan-6)
- Custom FPGA boards
```

### Basic Usage
```bash
# Memory dump
pcileech dump -out memory.raw -min 0 -max 0x200000000

# Process listing
pcileech pslist

# Read specific address
pcileech read -a 0x12345000 -l 0x1000

# Write to address
pcileech write -a 0x12345000 -v 0x41414141
```

## FPGA Firmware

### Development Tools
```
- Vivado (Xilinx)
- Quartus (Intel/Altera)
- Open-source toolchains
```

### Firmware Features
```
- TLP packet generation
- Configuration space emulation
- MSI/MSI-X interrupt handling
- DMA read/write implementation
```

### Anti-Detection Features
```
- Device ID spoofing
- Vendor ID masquerading
- Serial number randomization
- Capability structure emulation
```

## Device Emulation

### Common Emulation Targets
```
- Network adapters (Intel I210/I226)
- Storage controllers
- USB controllers
- Sound cards
```

### Emulation Requirements
```
1. Correct PCI configuration space
2. Proper capability structures
3. BAR (Base Address Register) setup
4. Interrupt handling
```

### Example: Network Adapter Emulation
```
- Emulate Intel I210 NIC
- Proper device/vendor ID
- PHY register emulation
- Minimal functionality for detection evasion
```

## Memory Access Techniques

### Physical Memory Reading
```c
// Typical pcileech API usage
HANDLE hDevice;
BYTE buffer[0x1000];

// Read physical memory
pcileech_read_phys(hDevice, physAddr, buffer, sizeof(buffer));
```

### Virtual Address Translation
```c
// Walk page tables to translate VA to PA
PHYSICAL_ADDRESS TranslateVA(UINT64 cr3, UINT64 virtualAddr) {
    // PML4 -> PDPT -> PD -> PT -> Physical
    UINT64 pml4e = ReadPhys(cr3 + PML4_INDEX(virtualAddr) * 8);
    UINT64 pdpte = ReadPhys(PFN(pml4e) + PDPT_INDEX(virtualAddr) * 8);
    UINT64 pde = ReadPhys(PFN(pdpte) + PD_INDEX(virtualAddr) * 8);
    UINT64 pte = ReadPhys(PFN(pde) + PT_INDEX(virtualAddr) * 8);
    return PFN(pte) + PAGE_OFFSET(virtualAddr);
}
```

### DTB (Directory Table Base) Finding
```
- Scan physical memory for valid CR3 values
- Look for kernel structures
- Use signature scanning
- Validate page table entries
```

## Integration with Tools

### Cheat Engine DMA Plugin
```
- CE server for DMA access
- Process memory reading via DMA
- Remote debugging capability
```

### ReClass DMA
```
- Structure reconstruction
- Live memory viewing
- Pointer scanning
```

### Custom Implementations
```
- DMA libraries (DMALib)
- Minimal VM libraries
- Game-specific cheats
```

## Anti-Cheat Bypass

### Why DMA Bypasses Anti-Cheat
```
1. No process attachment
2. No suspicious API calls
3. No kernel driver needed
4. No code injection
5. Operates below OS level
```

### Limitations
```
- Read-only for some implementations
- Timing-based detection possible
- Hardware fingerprinting
- Memory encryption (on newer systems)
```

### Detection Methods
```
- PCIe device enumeration
- IOMMU/VT-d monitoring
- DMA buffer analysis
- Performance counter anomalies
- Device identity consistency checks
- Platform attestation and boot-state validation
```

## Advanced Techniques

### Wireless DMA
```
- pcileech-wifi: Wireless card emulation
- Remote memory access
- Extended range operation
```

### SMM (System Management Mode)
```
- Ring -2 execution
- Highest privilege level
- Extremely stealthy
- Complex implementation
```

### VMD Controller Emulation
```
- Virtual Management Device
- Hide behind Intel VMD
- Complex detection evasion
```

## Firmware Development Guide

### Project Structure
```
/firmware
├── src/
│   ├── pcie_core.v       # PCIe core
│   ├── tlp_handler.v     # TLP processing
│   ├── dma_engine.v      # DMA implementation
│   └── config_space.v    # Config emulation
├── constraints/
│   └── board.xdc         # Pin constraints
└── scripts/
    └── build.tcl         # Build script
```

### Key Components
```verilog
// TLP packet handling
module tlp_handler (
    input wire clk,
    input wire [127:0] rx_data,
    output reg [127:0] tx_data,
    // DMA interface
    output reg [63:0] dma_addr,
    output reg [31:0] dma_data,
    output reg dma_read,
    output reg dma_write
);
```

## Security Considerations

### Ethical Use
```
- Security research only
- Authorized testing environments
- Responsible disclosure
- Legal compliance
```

### Risk Awareness
```
- Physical hardware access required
- Potential system instability
- Detection by advanced anti-cheat
- Legal implications
```

## Resource Organization

The README contains:
- pcileech and derivatives
- FPGA firmware projects
- DMA libraries
- Integration tools
- Device emulation firmware
- Anti-detection implementations

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
