---
name: linux-platform-security
description: Analyze native Linux, SteamOS, Steam Deck and Proton game-security boundaries. Use for compatibility-versus-policy triage, ELF/process evidence, credentials and capabilities, namespaces, seccomp, LSMs and Linux memory forensics; select repository resources across Wine, kernel, WSL and forensic categories. Record the actual kernel, distribution, runtime and active policy; distinguish platform mismatch, observation gaps and suspicious behavior with explicit privilege prerequisites and benign comparisons.
---

# Linux, SteamOS, and Proton Security

Use this skill for Linux-specific interpretation of platform and process
evidence. Use [reverse-engineering](../reverse-engineering/SKILL.md) for binary
reconstruction, [graphics-api](../graphics-api/SKILL.md) for rendering/capture,
and [dma-attack](../dma-attack/SKILL.md) for device-originated memory access.

## Establish the Execution Stack

Record native ELF versus Windows code under Proton, architecture, game build,
runtime version, graphics stack, kernel/distribution, launch context, and active
policy. Separate game code, Wine/Proton user-space components, translation
libraries, and Linux kernel behavior.

Proton is a Wine-based compatibility tool. Its presence does not imply Windows
kernel mechanisms are available, nor is it evidence of malicious virtualization.
Wine components, DXVK/vkd3d-proton, different module layouts, and diagnostic
output can be expected artifacts.
[Valve Proton](https://github.com/ValveSoftware/Proton)

Platform and protection-component support are product/build-specific. Do not
assume a Windows kernel component runs through Proton. Distinguish launcher,
media, runtime, graphics, and policy failures before attributing failed startup
to an account restriction or malicious activity.
[Valve Proton compatibility guidance](https://partner.steamgames.com/doc/steamhardware/proton)

## Privilege and Isolation Boundaries

| Surface | Documented distinction | Review implication |
|---|---|---|
| Credentials/capabilities | Capabilities divide privilege and are per-thread attributes | Record effective credentials and capability sets before asserting authority |
| User namespaces | UID 0 in a user namespace need not have host-root authority | Interpret credentials alongside mappings and namespace context |
| Seccomp | System-call filtering reduces interfaces; it is not a complete sandbox | Record active filter context and remaining boundaries |
| LSM policy | Availability, enabled modules, and actual enforcement differ | Confirm the selected policy rather than assuming SELinux/AppArmor from the OS name |

[Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html),
[User namespaces](https://man7.org/linux/man-pages/man7/user_namespaces.7.html),
[Kernel seccomp documentation](https://docs.kernel.org/userspace-api/seccomp_filter.html),
[Kernel LSM documentation](https://docs.kernel.org/admin-guide/LSM/index.html)

## Threat Model and Benign Controls

Describe unauthorized process/data access, abuse of privileged helpers,
untrusted native modules, and misconfigured isolation by the actual credential,
policy, and object boundary involved. A namespace or capability observation
does not itself establish a successful attack.

Compare evidence against the same supported runtime and game build. Legitimate
translation libraries, overlays, supported launch options, debug builds, and
graphics differences are important controls. A library name does not establish
authenticity; use component provenance and observed loading where available.
Do not transplant Windows structure offsets, callback semantics, or driver
findings into Linux conclusions.

## Evidence and Result

Preserve kernel/distribution/SteamOS version, game/runtime build IDs, architecture,
graphics driver, component hashes where useful, policy state, credential and
namespace context, and sanitized diagnostics. Mark inaccessible policy or
privilege information as unknown.

Distinguish unsupported platform, runtime regression, graphics failure, policy
denial, account enforcement, and supported security findings. State the observer,
available evidence, benign alternatives, and unresolved scope. Use
[research-rigor](../research-rigor/SKILL.md) when making cross-version or
consequential claims.

Primary sources reviewed: 2026-09-09. Distribution defaults and supported
runtime/protection combinations must be checked for the actual target build.

## Repository Navigation

For project selection, load [repository resource selection](references/repository-resources.md) on demand. Use the shared [repository navigation](../overview/references/repository-navigation.md) for local discovery layers, filename case, missing snapshots and currentness. Generated descriptions and wiki pages are discovery aids, not independent evidence.
