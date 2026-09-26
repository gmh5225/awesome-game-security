# Classification And Threat Model

## Classify the Acquisition Path First

For USB transfer cables, two-computer setups, LeechCore, or WinPmem, read
[Memory acquisition and transport](acquisition-and-transport.md).
Use it to distinguish hardware bus access from host-mediated software capture
and to evaluate US516/90212 implementation claims against primary sources.

- Identify the memory source: PCIe requester, host kernel component, hypervisor
  interface, or offline image. A library name or second computer does not settle it.
- Record source access requirements, transport endpoints, analysis location,
  write capability, and input functionality separately; leave unknowns explicit.
- Map controls to the actual boundary: device DMA remapping, driver/interface
  security, authenticated transport, or server-side information exposure.
- Report available artifacts, benign uses, missing visibility, and confidence.
  A clean process module list or absent FPGA is not a clean-host finding.

Use [research-rigor](../../research-rigor/SKILL.md) for disputed implementation,
performance, compatibility, or detectability claims. This classification does
not establish that a particular commercial setup uses the components it advertises.

For certainty claims about firmware classes, EPT, HVCI, containment, or TPM
proof, read [assurance boundaries](assurance-boundaries.md). It
separates mechanism, deployed policy, evidence coverage, and attribution.

## README Coverage

- `Cheat > DMA`
- `Anti Cheat > Detection:DMA`
- `Anti Cheat > Detection: Hacked Hypervisor`
- `Anti Cheat > Detection:Virtual Environments`
- `Anti Cheat > Detection:HWID`
- `Windows Security Features`

## Threat Model

### External DMA Cheat Architecture
```
A modern external DMA cheat consists of three components:

1. Cheat PC — runs the cheat application, signature databases,
   aim assistance, ESP rendering, and a network/USB link to the gaming PC.

2. DMA Card — an FPGA-based PCIe endpoint installed in the gaming PC
   (typically M.2 NVMe slot). Exposes a memory-read/write interface to
   the cheat PC. Uses Bus Master capability to issue Memory Read TLPs
   against the gaming PC's RAM.

3. Actuator (optional) — a USB HID emulator (microcontroller-based) that
   injects keyboard/mouse input on the gaming PC according to commands
   from the cheat PC, closing the loop.

This hardware-only model need not use a host memory-acquisition process.
The device initiates memory transactions subject to platform routing and
IOMMU mappings. Host agents and mixed hardware/software designs are separate
cases. Visibility depends on the observer and platform; device presence,
configuration, policy state, and available fault telemetry are different
observations, none of which alone establishes malicious intent.
```

### Complementary Control Families

| Layer | Property evaluated | Limits |
|---|---|---|
| PCIe identity and behavior | Consistency with an identified device and matched baseline | A mismatch needs version, topology, driver, workload, and benign-device context; an identifier is not proof of intent |
| IOMMU enforcement | Device requests permitted by the active remapping policy | Verify actual path, mappings, lifecycle, and available fault evidence; enforcement and observation are separate |
| External attestation | Authenticity and policy appraisal of selected measurements | Boot evidence does not automatically cover current device behavior or runtime mapping state |

This control-family map is not a staged detector or a four-step verdict. For
anti-cheat inventory and IOMMU-state collection, use the [defensive PCIe pipeline](detection-and-forensics.md#defensive-anti-cheat-inventory-and-correlation)
and [IOMMU state verification](iommu-state-verification.md).

Use the [assurance reference](assurance-boundaries.md) for the underlying
platform contracts and the limits of each evidence source.
