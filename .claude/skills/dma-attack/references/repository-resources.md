# DMA Repository Resource Selection

Read this when choosing resources to classify a purported DMA setup, examine device-isolation claims, or interpret existing acquisition evidence. Start with [acquisition and transport](acquisition-and-transport.md); identify the memory initiator before selecting projects from the local [README](../../../../README.md).

Local index and linked primary documentation reviewed: **2026-09-09**. The rows below select documentation and evidence models for defensive review; they are not firmware, acquisition or bypass deployment instructions.

| Review question | Exact README location and representative source | Selection boundary and useful evidence |
|---|---|---|
| Is the claimed component a PCIe core or merely a cable/transport? | `Cheat` → `DMA`: [LitePCIe](https://github.com/enjoy-digital/litepcie) | The upstream describes a configurable PCIe core. Select its architecture vocabulary to distinguish requester, host interface and data path. A listed core, connector shape or FPGA model does not prove which design/configuration is running; deliver a topology with observed versus asserted components. |
| Does a familiar software name establish hardware acquisition? | `Cheat` → `DMA`: [PCILeech](https://github.com/ufrisk/pcileech) | Upstream documents both hardware and software acquisition via LeechCore. Use that distinction for component provenance, not acquisition procedures. LeechCore and WinPmem are supplemental primary sources in the [acquisition reference](acquisition-and-transport.md), not standalone project links in this README snapshot. Preserve library/driver identity and evidence of the active source; a filename alone cannot identify the backend. |
| What does a DMA-remapping example demonstrate? | `Anti Cheat` → `Detection:DMA`: [HelloIommuPkg](https://github.com/tandasat/HelloIommuPkg) | It is an Intel VT-d DXE runtime-driver learning example whose author explicitly excludes production use. Select it for conceptual review of isolation boundaries. Assess actual Windows behavior against [Kernel DMA Protection documentation](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt), recording firmware support, OS/build, device/driver policy and boot/runtime phase. A sample's presence does not prove active protection. |
| What can an already acquired image tell us? | `Anti Cheat` → `Information System & Forensics`: [Volatility 3](https://github.com/volatilityfoundation/volatility3) | Select for offline analysis, separately from the collector and transport. Record image hash, acquisition provenance, missing regions, OS/symbol match and analysis version; see [symbol matching requirements](https://volatility3.readthedocs.io/en/latest/symbol-tables.html). Parsed game data cannot alone identify the path by which it was acquired. |

## Avoid Misrouting

- Route host kernel drivers and their privileged interfaces to [windows-kernel](../../windows-kernel/SKILL.md). Device DMA isolation and host-driver authorization address different boundaries; a USB bridge does not supply evidence about either by itself.
- The `DMA` category also contains game-specific clients and firmware projects. Their branding or dependencies do not prove hardware presence, protected-memory access, undetectability or current mitigation coverage. Use them only to classify claimed prerequisites and potential observation points.
- A transport connector, shared library, image artifact or failed detector provides partial evidence. Do not infer an exact cable chipset/protocol, absence of hidden hardware, data integrity or a successful protection bypass from those observations. Keep supported architectures and alternatives explicit.

## Deliver a Review Record

Return a diagram separating memory source, transport, analysis host and optional input path. Attach a claim-to-evidence table with actual README locator and upstream revision/date, physical access or host privilege prerequisites, component provenance, OS/device-policy context, observable artifacts, benign uses and missing visibility. State which control covers each boundary and which architecture claims remain unresolved.

Use the shared [repository navigation](../../overview/references/repository-navigation.md) for local discovery layers, filename case, missing snapshots and currentness. Generated wiki and descriptions are lookup aids; corroborate technical conclusions with the primary source and the actual system evidence.
