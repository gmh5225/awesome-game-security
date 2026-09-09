---
title: Engine Trust Boundaries
kind: concept
topics: [game-engine, anti-cheat, reverse-engineering]
sources:
  - wiki/sources/skills/game-engine.md
  - wiki/sources/descriptions/Timehue__ShinobiX.md
updated: 2026-09-09
confidence: high
---

# Engine Trust Boundaries

Game engines expose multiple **research surfaces** that fail independently. Security conclusions must name which boundary broke—not merely that an engine was identified or an object offset was found. (source: wiki/sources/skills/game-engine.md)

## Baseline before analysis

Record before generalizing signatures, SDK dumps, or exploit paths:

| Dimension | Why it matters |
|-----------|----------------|
| Engine branch + game build/hash | Layouts and globals drift per patch |
| Platform / ABI | Calling conventions, pointer width, metadata paths |
| Scripting backend | Mono vs IL2CPP vs Blueprint-only vs native-only |
| Stripping / symbol availability | Reflection and dump completeness |
| Plugin / mod versions | Editor vs shipped plugin sets differ |

Apply [[research-rigor]] when porting artifacts across builds. Separate **reflected metadata**, **native/managed execution**, **serialized assets**, **in-process plugins**, and **client/server replication**—each is a distinct trust surface.

## Boundary map

| Surface | Typical failure mode | Route elsewhere |
|---------|---------------------|-----------------|
| Reflected metadata | Schema accepted as full memory layout | [[unreal-object-model]], [[il2cpp]] |
| Serialized assets | Untrusted content accepted by importer | asset-format RE; supply-chain review |
| In-process plugins | Third-party code with engine privileges | mod/plugin inventory |
| Client replication | Client assertions treated as authoritative state | game-server-security (authority, sessions); browser SPA clients such as [[shinobix]] require server-side settlement receipts and ledgered economy mutations (source: wiki/sources/descriptions/Timehue__ShinobiX.md) |
| Build / update / mod distribution | Tampered binaries or mod channels | game-supply-chain-security |
| Tick / prediction / replay | Ordering or replay limits misunderstood | game-server-security (time-ordering evidence) |
| Graphics measurements | Present timing or draw counts misread | [[overviews/graphics-api]] |

Engine identification or object discovery **alone does not establish compromise**. Correlate asset provenance, plugin inventory, owned-build diagnostics, serialization checks, and server validation evidence.

## Engine-specific limits

- **Unreal** — reflection covers annotated members; native-only members and object lifetime need separate evidence. A reflected schema is not a complete C++ layout. See [[unreal-object-model]].
- **Unity IL2CPP** — managed assemblies, stripping, C++ generation, and native compilation interact; reconstructed names or metadata do not guarantee complete type coverage or original-source recovery. See [[il2cpp]].
- **Godot** — GDExtension compatibility is versioned (manifest documents engine release, platform, build, architecture); verify the target release rather than projecting one example onto all versions.
- **Source / SDK trees** — distinguish open-source engines, licensed engine source, SDK game code, and reference-source subsets. Source SDK 2013 carries its own non-commercial license; repository visibility does not imply unrestricted reuse. See [[source-netvars]].

## Evidence report fields

When documenting engine-related findings, include:

1. **Affected boundary** — which surface failed (importer, plugin, replication, metadata, etc.)
2. **Prerequisite** — build, platform, backend, and tooling versions
3. **Artifact** — dump, SDK, asset, or trace inspected
4. **Observed result** — what changed or was read/written
5. **Benign controls** — cases where the same API behaves safely
6. **Version-dependent limits** — what breaks on the next patch or backend switch

Owned-build diagnostic workflows belong with [[research-rigor]] robustness/triage guidance when triaging regressions on builds you control.

## Related

[[unreal-object-model]] · [[il2cpp]] · [[source-netvars]] · [[resource-selection]] · [[research-rigor]] · [[shinobix]] · [[overviews/game-engine]] · [[overviews/anti-cheat]]
