---
name: dma-attack-techniques
description: Guide for Direct Memory Access (DMA) attack techniques using FPGA hardware. Use this skill when researching PCIe DMA attacks, pcileech, FPGA firmware development, or hardware-based memory access for game security research.
---

# DMA Attack Techniques

## Overview

This skill covers Direct Memory Access (DMA) attack resources from the awesome-game-security collection, focusing on FPGA-based PCIe attacks, pcileech usage, and hardware-level memory access techniques.

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
