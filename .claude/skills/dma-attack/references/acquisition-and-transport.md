# Memory Acquisition, USB Bridges, and Hardware DMA

Primary-source review: 2026-09-09. This reference classifies architectures;
it does not verify the implementation of a third-party product or demonstration.

## Separate Four Roles

1. **Acquisition:** the component that obtains memory and its access authority.
2. **Transport:** the link carrying acquired data or requests between components.
3. **Analysis/presentation:** the software interpreting or displaying that data.
4. **Input/control:** any separate path that produces actions on the host.

Moving analysis to another computer does not establish how acquisition works.
The same network or USB transport can carry ordinary files or captured data.
The classification below is an analytical model, not a product implementation.

| Architecture | Memory source and prerequisite | Transport role | Main defensive boundary |
|---|---|---|---|
| Hardware DMA | DMA-capable device with a usable memory mapping | Carries control/results if the design has a remote controller | Device isolation, platform configuration, mapping lifecycle |
| Host-mediated capture | Host software with the necessary OS or kernel access | Carries data already acquired by host software | Driver trust, interface authorization, host telemetry |
| Offline image analysis | Previously acquired memory image | Moves an existing artifact | Image provenance, integrity, acquisition timestamps |
| Ordinary USB file transfer | Files exposed by host applications | Transfers application data between computers | Device/application access and data handling |

## What a USB Transfer Cable Establishes

[UGREEN's US516/90212 page](https://www.lulian.cn/product/1829.html) describes
a 2 m computer-to-computer transfer cable, a nominal 5 Gbps USB 3.0 rate,
USB/USB-C connectivity, bundled driver support, and shared keyboard/mouse use.
The nominal link rate is not measured application throughput. Its advertised
functionality does not establish arbitrary physical-memory access.

A USB bridge cable is an active interconnect, not merely an ordinary passive
lead with matching plugs. The
[Prolific PL-25A1 manual](https://prolificusa.com/wp-content/uploads/2018/02/um_pl25A1_v1.2.pdf)
documents a USB-to-USB bridge product category and transfer software; it does
not identify the chip in US516. Connector shape, including USB-A to USB-A,
does not prove chipset, protocol, driver compatibility, or acquisition ability.

Do not conflate ordinary USB peripherals with PCIe tunneling over Thunderbolt
or USB4. Microsoft distinguishes non-PCI USB peripherals from DMA-capable PCIe
devices; a USB host controller can itself use DMA without giving a connected
transfer cable unrestricted host-memory access.
[Microsoft Kernel DMA Protection](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)
and [Linux USB4/Thunderbolt documentation](https://docs.kernel.org/admin-guide/thunderbolt.html)
explain the platform and tunneling distinctions.

## LeechCore and WinPmem

[LeechCore](https://github.com/ufrisk/LeechCore) is an acquisition abstraction
used by PCILeech and MemProcFS. Its documented sources include hardware,
software acquisition, and memory images. LeechAgent provides a remote
connection; the underlying source may still be hardware or software.
A file named `LeechCore.dll` is an identification lead, not proof of the genuine
library, active use, FPGA hardware, or a selected acquisition backend. Validate
provenance and observed loading separately. A modified binary needs its own
identity and behavior evidence.

[WinPmem](https://github.com/Velocidex/WinPmem) is an open-source Windows
physical-memory acquisition project under Apache 2.0, formerly part of Rekall.
The documented standalone imager includes and loads an appropriate kernel
driver. Its read interface supports user-space imaging. This is host-mediated
acquisition, even when an application sends the resulting data elsewhere.
Availability and compatibility depend on the exact release and host policy;
the existence of a signed release does not guarantee it loads on every system.

The project documents multiple acquisition methods. Do not turn a historical
method into a universal driver recommendation:
[MmMapIoSpace's documented contract](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace)
limits its use to appropriate I/O space or locked pages. It is not a general
authorization to map arbitrary live RAM. No particular method is inferred
from a cable, filename, or video label.

## Protection and Observation Limits

IOMMU remapping governs device-originated DMA; it is not the access-control
mechanism for a CPU executing host kernel code. Software acquisition therefore
does not demonstrate an IOMMU bypass. Windows Kernel DMA Protection also has
specific device, driver, firmware, and boot-phase scope; its status is not a
certificate of whole-host integrity.
[Microsoft documentation](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)

For a suspected acquisition system, correlate evidence already available from
the relevant observation points: device inventory, driver/service provenance,
acquisition process identity, interface access, and collection timestamps.
Record which observations were unavailable. A second computer or bridge cable
also has ordinary collaboration uses; a memory imager has legitimate forensics
uses. Neither object alone proves cheating. Absence from the game process does
not establish absence from the host.

## Claim Ledger for USB Bridge Scenarios

| Claim | Evidence status | What remains necessary |
|---|---|---|
| US516/90212 transfers files and shares input | Vendor documented | Confirm actual unit/revision and supported host configuration |
| The link alone reads game memory | Not established by the product documentation | Identify the actual acquisition component and authority |
| A specific setup uses WinPmem and a modified LeechCore | Plausible architecture; particular implementation unverified | Versioned artifacts and independently supported observations |
| Only this SKU works; alternatives fall to about 13 MB/s | Unverified implementation/performance claims | Compatibility evidence and a stated benchmark method |
| A specific SmartLink package, virtual CD, VID, or chipset is required | Not established by the reviewed product page | Revision-specific vendor documentation or inspected unit evidence |
| No FPGA means no host memory acquisition | Invalid inference | Evaluate software sources separately |
| No process injection means undetectable | Unsupported generalization | Define collector coverage and consider host/device evidence |

This [video lead](https://www.youtube.com/watch?v=eg690EEpIOs) was not
retrievable during this review and is not used as verified support. Retail
availability, unpublished compatibility restrictions, and future product
behavior are not inferred from the architecture.

For the driver security boundary, continue with
[windows-kernel](../../windows-kernel/SKILL.md); for uncertain claims, use
[research-rigor](../../research-rigor/SKILL.md).
