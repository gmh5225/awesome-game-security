# DMA and Hypervisor Assurance Boundaries

Use this reference when a report promises certain detection, universal protection,
or runtime integrity from a device label or platform feature. This is a bounded
correction of five claim families, not a validation of the entire legacy catalog.
Primary documents below were reviewed on 2026-09-09.

## Device Labels and Detection Evidence

A firmware nickname, price, public/private status, or claimed sophistication tier
does not provide measured detector coverage. Replace rankings with observed
identity, configuration, functionality, topology, and access-policy evidence.
Record collection method, exact hardware/firmware/driver, workload, matched benign
controls, and false-positive uncertainty. An unexpected identifier or absent
driver can justify investigation without establishing unauthorized memory access.

This is an evidence rule, not a claim that one class of device is undetectable.
Use [research rigor](../../research-rigor/SKILL.md) for evaluation design. PCI
identity inspection, remapping enforcement, and boot attestation observe different
properties; their documented mechanisms do not establish a universal tier ladder.

## CPU Access and Device Access

EPT concerns processor memory virtualization; VT-d supplies independent device
DMA remapping. Therefore an EPT violation is not, by itself, a record of a PCIe
DMA transaction. A hypervisor may manage both mechanisms, but its presence does
not establish that either policy covers the relevant access path.
[Intel processor datasheet, sections 2.2.1–2.2.2](https://cdrdv2-public.intel.com/634963/634963-005.pdf)

For a protected-page or decoy claim, identify the requester and collector: CPU
access under the active EPT policy, device request under an active IOMMU domain,
or an application event. Report denied permission separately from malicious
intent. No EPT event does not prove no DMA access.

Execution outside a guest kernel does not imply invisibility. Hyper-V explicitly
documents guest-visible feature discovery. Enforcement also depends on the
trusted hypervisor, policy/configuration interface, correct page coverage, and
protected backing memory; assess those assumptions instead of promising survival
of every kernel compromise.
[Microsoft hypervisor discovery](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/tlfs/feature-discovery)

## Separate Platform Features and Deployment State

Memory integrity isolates kernel code-integrity decisions using VBS. Treat
code integrity, vulnerable-driver blocking, and DMA policy as distinct controls.
Microsoft notes that a vulnerable-driver blocklist cannot cover every vulnerable
driver. Check the effective policy and component versions rather than asserting
that HVCI prevents all abuse of signed drivers.
[Memory integrity](https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity),
[Microsoft blocklist limits](https://support.microsoft.com/en-us/servicing/os/windows/2022/10/kb5020779-the-vulnerable-driver-blocklist-after-the-october-2022-preview-release)

Kernel DMA Protection does not require VBS; device DMA remapping can be enabled
independently of that overall feature. Runtime protection and firmware's pre-boot
responsibilities are separate. Review actual device/driver remapping and platform
policy, not one UI flag. A missing feature is a policy/compatibility question,
not a misconduct finding.
[Microsoft Kernel DMA Protection](https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)

## Attestation Has a Defined Subject

A TPM quote signs an attestation containing selected PCR information and
caller-supplied qualifying data. PCR banks, reset/extend permissions, and platform
profiles matter; neither all PCRs nor all boot measurements have one universal
allocation or reset rule. Preserve the selected bank, PCRs, nonce, and event-log
relationship when interpreting a result.
[TCG TPM 2.0 Library Architecture v185, sections 14 and 28](https://trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-2.0-Library-Part-1-Architecture_Version-185_pub.pdf)

Verifier trust includes key enrollment and the applicable trust chain; an
attestation key is not automatically a manufacturer-certified identity. Windows
documents a cloud CA flow for AIK certificates. A valid quote or accepted boot
policy does not enumerate current PCIe devices, current IOMMU mappings, or every
runtime action. Obtain separate evidence for those unmeasured properties.
[Microsoft health-attestation keys and flow](https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/protect-high-value-assets-by-controlling-the-health-of-windows-10-based-devices)

Secure Launch uses DRTM during startup to establish a measured execution path;
do not describe it as an arbitrary post-boot application launch or a complete
runtime scan. The Windows OEM DMA contract specifies a PCR 7 event for a reduced
DMA-protection state; absence is meaningful only with an applicable, trustworthy
and complete measurement path.
[Microsoft System Guard](https://learn.microsoft.com/en-us/windows/security/hardware-security/how-hardware-based-root-of-trust-helps-protect-windows),
[Microsoft OEM DMA requirements](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-kernel-dma-protection)

## Containment Belongs to the Platform Owner

Windows reserves PCI configuration headers and capability registers to the OS;
supported configuration interfaces do not grant arbitrary write authority over
them. A generic game-security collector should not rewrite another driver's
bus-master, interrupt, BAR, or remapping state. Review documented OS/driver
lifecycle and policy controls, effects on other devices, in-flight work, recovery,
and observed completion of isolation.
[Microsoft PCI configuration ownership](https://learn.microsoft.com/en-us/windows-hardware/drivers/pci/accessing-pci-device-configuration-space)

Containment success depends on the actual platform path and verified state, not
on a firmware tier. Preserve evidence before applying an authorized response and
keep access restriction separate from a sanction decision. Prefer an explicit
unsupported/unknown state over claims that a direct register change or a TPM
quote closes every remaining gap.
