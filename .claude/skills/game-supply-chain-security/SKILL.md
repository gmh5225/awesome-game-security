---
name: game-supply-chain-security
description: Assess game build, launcher, update, distribution, and mod/plugin trust. Use to connect repository CI resources, editor acquisition, hot-patch runtimes, asset specifications, and parsers to release credentials, isolation, provenance, SBOMs, update freshness, ingestion boundaries, and recovery. Distinguish a build tool or script bridge from release authorization, and format acceptance from safe loading; report exact artifact, dependency version, channel, publisher, and verification policy.
---

# Game Build, Update, and Mod Supply Chains

Use this skill to review release and content trust boundaries. Route runtime
object models to [game-engine](../game-engine/SKILL.md), platform package signing
to [mobile-security](../mobile-security/SKILL.md), and privileged driver behavior
to [windows-kernel](../windows-kernel/SKILL.md).

For repository-backed choices, read the
[supply-chain resource guide](references/repository-resources.md) for CI entry
points, editor acquisition, hot-patch runtimes, and asset-parser dependencies.

## Map Release Authority

```text
Source and dependencies -> build -> artifact and provenance -> signing
  -> publication/channel -> delivery -> updater/install -> game or plugin load
```

Record who can change source, build instructions, signing policy, uploaded
artifacts, live channels, and installed files. Distinguish release credentials,
signing keys, build identities, and player sessions. A delivery service is one
part of this chain. SteamPipe distinguishes builds, depot manifests, and live
branches, and recommends dedicated, restricted build accounts.
[Valve SteamPipe uploads](https://partner.steamgames.com/doc/sdk/uploading)

## Threat Objectives and Evidence

| Objective | Boundary requiring review | Useful evidence |
|---|---|---|
| Substitute a release or dependency | Producer/build identity and artifact binding | Source revision, build inputs, provenance, artifact digest |
| Publish an unauthorized channel update | Signing and publication authority | Release approvals, credential scope, channel history |
| Keep a client on stale content or combine inconsistent metadata | Freshness, version, and metadata consistency | Trusted metadata versions, expiry, role and target relationships |
| Abuse build jobs to affect other releases | Build isolation and secret boundaries | Worker lifecycle, cache provenance, signing boundary |
| Obtain code execution through a mod/plugin | Import and execution permissions | Exact content version, format, validation and allowed capability |
| Overwrite protected files or exhaust import resources | Extraction/install path and resource boundaries | Staging location, destination policy, expanded-size and work budgets |

These are review categories, not evidence that a particular publisher or mod
platform is compromised.

## Update Verification and Recovery

Review trust roots, delegated roles, signature thresholds, target hashes and
lengths, metadata versions, expiry, and consistency across metadata files.
HTTPS or an executable signature alone does not cover every update decision.
Distinguish metadata rollback from an operator-authorized application rollback
published through new valid metadata. Record offline clients, clock uncertainty,
expired metadata, and the owner of recovery policy.

Expiry alone does not prove a freeze attack. Do not silently bypass freshness
checks; use the documented authenticated recovery process for the system.

TUF addresses update metadata trust and freshness; it does not establish safe
application behavior, compatible releases, or transactional installation.
[TUF specification 1.0.36](https://theupdateframework.github.io/specification/v1.0.36/index.html)

## Build Provenance and Isolation

Bind provenance to the actual artifact digest and verify its trusted builder,
canonical source, build type, and expected parameters. Merely finding a signed
attestation is insufficient. Record where verification happens and which
compromised components that observation could detect. Provenance is not a code
security audit.
[SLSA 1.2 artifact verification](https://slsa.dev/spec/v1.2/verifying-artifacts)

Treat scripts, plugins, compilers, caches, and user-controlled build inputs as
distinct influences. Review job isolation, transient environments, cross-build
effects, and separation of signing secrets from user-defined build steps.
State the assurance level actually achieved; SLSA Build L3 requirements do not
eliminate every insider, dependency, or platform risk.
[SLSA 1.2 build requirements](https://slsa.dev/spec/v1.2/build-requirements)

## Released Components and User Content

Associate the SBOM with the shipped artifact and platform. Distinguish build
dependencies, bundled runtime libraries, native SDKs, editor plugins, launchers,
and services. Record identity, version, digest, source, relationship, and owner
where available. Inventory completeness and vulnerability applicability require
separate verification; an SBOM alone is not a clean bill of health.
[CycloneDX SBOM](https://cyclonedx.org/capabilities/sbom/)

Separate data assets, scripts, native modules, and editor tools by their import
and execution permissions. Workshop has ready-to-use and curated models; not
all Workshop content undergoes the same developer approval. Platform delivery
does not establish a sandbox or safe execution. Bind review to a content version
and reassess material updates.
[Valve Workshop models](https://partner.steamgames.com/doc/features/workshop)

For archives, maps, saves, textures, and manifests, review actual format,
destination paths, protected-file boundaries, isolated staging, parser versions,
and processing budgets. Include expanded size and file count; extension, MIME,
or compressed download size alone is insufficient. These are defensive
applications of file-ingestion principles to games.
[OWASP file upload guidance](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

## Review Output

Report artifact/build/channel/platform, producer and source identity, build and
release authorities, expected verification policy, observed checks, affected
boundary, compatibility alternatives, recovery owner, and unresolved scope.
Keep signature validity, authorized publication, freshness, compatibility, and
runtime safety as separate conclusions. Apply
[research-rigor](../research-rigor/SKILL.md) to evidence and uncertainty.

Primary sources reviewed: 2026-09-09. TUF and SLSA references are explicitly
versioned examples; verify the implementation's chosen specification/version.

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
