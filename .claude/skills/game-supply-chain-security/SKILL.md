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
