---
name: awesome-game-security-overview
description: Find, select and maintain resources in awesome-game-security using its actual README taxonomy, skill catalog, compiled wiki, generated descriptions and source archives. Use for repository-specific discovery, category placement, duplicate or identity review, missing/case-mismatched local paths, and choosing the right domain skill. Return a focused selection with provenance and limitations; route technical conclusions to the matching domain rather than treating collection membership as proof.
---

# Awesome Game Security: Resource Selection

Use this skill to connect a concrete question to the collection. Start with the
question's object and desired output, then select the relevant domain and only
the resource layers needed to answer it. Repository membership is a discovery
signal, not a capability, endorsement or compatibility guarantee.

## Select a Domain

Folder IDs below locate skills; installed invocation names come from each
SKILL.md frontmatter. Existing names and folders are not all identical.

| Question or artifact | Primary skill | Boundary / related work |
|---|---|---|
| Detector architecture, input evidence, telemetry faults or decisions | [anti-cheat](../anti-cheat/SKILL.md) | Platform signals need the relevant platform contract; conclusions need research-rigor |
| Physical-memory source, PCIe/USB bridge, FPGA, IOMMU or host acquisition | [dma-attack](../dma-attack/SKILL.md) | Separate memory initiator, transport and analysis backend |
| Engine source, runtime metadata, plugins or asset boundaries | [game-engine](../game-engine/SKILL.md) | Editor tools are distinct from shipped runtime; persistent state goes to server security |
| Attack classes, prerequisite access and defensive coverage | [game-hacking](../game-hacking/SKILL.md) | Identify the boundary before choosing a specialized domain |
| Rendering API, capture, translation or frame/performance artifacts | [graphics-api](../graphics-api/SKILL.md) | Timing output, captured pixels and game-state evidence differ |
| Binary identity, static analysis, symbols, dumps or code comparison | [reverse-engineering](../reverse-engineering/SKILL.md) | Recovered structure does not by itself prove runtime behavior |
| Windows drivers, callbacks, telemetry and platform policy | [windows-kernel](../windows-kernel/SKILL.md) | Runtime privileges, observation scope and preventive policy are separate |
| Android/iOS package, device-integrity or mobile runtime evidence | [mobile-security](../mobile-security/SKILL.md) | Local root observations, remote attestations and enforcement differ |
| Linux, SteamOS, Proton, credentials or namespaces | [linux-platform-security](../linux-platform-security/SKILL.md) | Compatibility layers and isolation mechanisms have different roles |
| RPC authorization, sessions, economy, timing and replay consistency | [game-server-security](../game-server-security/SKILL.md) | Transport reliability does not authorize a gameplay effect |
| CI, dependencies, launchers, update trust, mods or content distribution | [game-supply-chain-security](../game-supply-chain-security/SKILL.md) | Build provenance, artifact signing and runtime safety are distinct |
| Conflicting claims, source lineage, evaluation or uncertain attribution | [research-rigor](../research-rigor/SKILL.md) | Pair with the domain that supplies the actual technical contract |

Resource discovery can finish here when the user only needs locations or a
shortlist. Do not force a security review onto ordinary graphics, game-development
or library-usage questions merely because their resources occur in this collection.

## Use the Actual Repository

Read [repository navigation](references/repository-navigation.md) for current
layer roles, exact-path lookup, archive limitations and the read-only indexer.
Each domain entrypoint links a focused repository resource guide; load only the
one relevant to the question.

The top-level README uses H2 categories, blockquote subcategories and resource
bullets. Category names are current data, not a fixed count to memorize. Important
cross-category relationships include:

| README area | Typical routing |
|---|---|
| Game Engine; Game Develop; Game Assets; Game Hot Patch | Engine/runtime, package and release boundaries |
| Renderer; DirectX; OpenGL; Vulkan; Game Testing | Rendering, capture, compatibility and performance evidence |
| Game Network; Game CI | Transport/session contracts and release authority |
| Cheat; Anti Cheat; Some Tricks; Windows Security Features | Threat classes, observation mechanisms and platform controls |
| Platform/console emulator categories; WSL; WSA | Match the actual host, guest, compatibility layer and target format |
| Mathematics; AI; Image Codec; Wavefront Obj; PhysX SDK | Supporting algorithms, measurement and parser/asset context |

Do not flatten a resource's category into a capability claim. Some Linux kernel
references are listed in Android-related subcategories; organizations and sample
projects can appear alongside libraries. Read the actual entry and its scope.

Current root layers are README.md, .claude/skills/, wiki/, description/, archive/,
scripts/ and .github/workflows/. Individual skill installation may omit the rest.
Check available files and use verified upstream sources when a local layer is absent.
A corresponding wiki page is not guaranteed for every skill. Check
[the catalog](../../../wiki/index.md) or the directory before constructing a path.

## Produce a Useful Selection

For each chosen resource, provide the original identity/URL, README location,
reason it fits this task, expected artifact, version/platform scope, and a material
limitation. Use a small comparative table when alternatives serve different roles.
Distinguish resources already listed from supplemental sources discovered upstream.

For exact capability claims, inspect primary documentation or a source file at a
known revision. Follow [repository evidence reconciliation](../research-rigor/references/repository-evidence.md)
when generated layers or historical snapshots disagree. A popular project, working
link or large archive does not settle technical quality.

## Maintain the Collection When Requested

Check existing occurrences, original/fork relationships and the chosen category
before adding an entry. Preserve deep links and document meaningful redirects;
changing the owner is not enough to establish equivalent source identity.

Use the existing bullet convention:

```markdown
## Category
> Subcategory
- https://github.com/owner/project [Purpose; platform/scope; distinctive value or limitation]
```

Keep the public skills table aligned with actual frontmatter names. Check links,
category placement and the exact diff. Repository maintenance scripts can call
services and write or publish data; inspect the chosen script instead of running
bulk automation as a retrieval shortcut.

For skill-library changes, use the [coverage roadmap](references/coverage-roadmap.md)
and [evaluation guide](../research-rigor/references/skill-evaluation.md). Structural
validation and a successful lookup are not evidence of superior model performance.

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
For this domain, read [wiki/overviews/overview.md](../../../wiki/overviews/overview.md).
Raw URL: [overview overview](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/wiki/overviews/overview.md).

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

The routing and evidence references above help choose useful artifacts. Shared
[repository navigation](references/repository-navigation.md) adds the optional read-only indexer,
case-ambiguity handling and maintenance details; it supplements this Data Source
section rather than replacing it.
