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

## Data Source

Use the following repository sources directly when applying this skill. Prefer
available local files for discovery and scoped historical inspection; use the
raw URLs when the collection is not installed locally. These entrypoint details
are retained here so source lookup does not depend on loading another skill.

### 0. Compiled Wiki

Start with [wiki/index.md](../../../wiki/index.md) for topical synthesis and
cross-project connections. [Wiki schema](../../../wiki/AGENTS.md) describes its
structure. Generated wiki pages are discovery aids; follow their original
citations before adopting technical claims.

Raw catalog: [wiki/index.md](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/wiki/index.md).
This skill does not currently have a matching wiki overview. Use its local
references and the wiki catalog to find related pages; do not invent a path.

A direct project question can start with its README entry or description below;
reading the entire wiki is unnecessary.

### 1. Project Overview and Resource Index

[README.md](../../../README.md) contains the collection's actual categories,
subcategories, project URLs and short descriptions. Find the relevant category
and retain the original URL, including any specific file or revision suffix.

Raw index: [README.md](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md).

### 2. Repository Descriptions

For a concise project summary, look for the actual local path:

```text
description/{owner}/{repo}/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt
```

Example: [bgfx description](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/bkaradzic/bgfx/description_en.txt).
Extract owner/repository from the original GitHub project URL, omitting a .git
suffix. Resolve existing path casing before constructing a local/raw path.
Descriptions are generated summaries, not independent verification. If absent
or inaccessible, use the README entry, relevant archive or original project.

### 3. Repository Source Archives

For deeper inspection of an available captured source tree, locate:

```text
archive/{owner}/{repo}.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt
```

Example: [bgfx archive](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/bkaradzic/bgfx.txt).
Prefer inspecting the relevant portion of an existing archive over re-cloning
merely to inspect the same captured material. Archives may exclude files, use
fallback extraction or contain truncation; they are not guaranteed complete
checkouts. Record any upstream revision evidence and included-file limits.
If missing or insufficient, follow the README's original upstream URL.

### Choose and Verify the Source

For a specific project, locate its README identity, use a description or wiki
page for orientation when helpful, then inspect the relevant archive/source
artifact for the question. For current compatibility or exact implementation,
verify the matching upstream documentation, release or immutable source revision.
Keep the collection revision and capture/generation dates separate from the
upstream version. Multiple generated layers from one source are not independent
corroboration, and missing archive content does not establish upstream absence.

The per-domain resource guide above helps choose useful artifacts. Shared
[repository navigation](../overview/references/repository-navigation.md) adds the optional read-only indexer,
case-ambiguity handling and maintenance details; it supplements this Data Source
section rather than replacing it.
