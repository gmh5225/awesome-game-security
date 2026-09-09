# Reconcile Claims Across Repository Layers

Use when README, generated descriptions, compiled wiki, archived source and
current upstream material disagree. Local pipeline review: 2026-09-09.

## Trace the Claim, Not the Number of Pages

Start with the exact claim the user needs answered: project identity, declared
capability, implementation behavior, compatibility, measured outcome or defensive
effectiveness. These require different evidence.

| Repository evidence | Supported interpretation | Unsupported promotion |
|---|---|---|
| README entry and category | The collection lists this URL here | The tool works, is maintained or defeats a defense |
| Generated English summary or translation | A summary contains this claim | A second language independently confirms it |
| Wiki entity/concept linking that summary | A discovery path to the same source | Independent corroboration |
| Archive text containing a relevant implementation | These captured files contain this logic | Complete build, deployed behavior or current upstream support |
| Current official documentation | The stated interface/support contract | Every older release or third-party integration follows it |
| Versioned observation from a defined environment | The observed result in that environment | A universal capability, absence of detection or attribution |

The repository's [description generator](../../../../scripts/generate-descriptions-cli.py)
uses archived material, and its [wiki updater](../../../../scripts/update-wiki-cli.py)
builds compiled pages. Trace the actual inputs for the claim instead of assuming
every page followed the same pipeline. Derived pages can amplify one mistake.

## Resolve a Conflict

Record a compact chain: collection location → generated claim → available
archive file/revision evidence → original source → supported conclusion.
Preserve exact URLs and distinguish archive review date, generation date,
upstream version and event date.

If a summary claims broad platform support but only one platform's files are
available, the archive establishes partial captured coverage. It neither
confirms broad support nor disproves uncaptured support. Check the matching
upstream release/documentation and leave the unresolved portion explicit.

If README and upstream differ, first check identity, redirects, fork lineage,
version and whether one statement describes a plan rather than shipped behavior.
Do not silently overwrite a historical finding with current documentation.
Keep both scopes when both statements are accurate for different versions.

## Select the Next Artifact

| Uncertainty | Useful next artifact |
|---|---|
| Is this the original project? | Maintainer identity, repository relationship and recorded redirect |
| Was this implementation present? | Relevant source file at an immutable revision |
| Is the archive complete enough? | Included file boundaries, truncation/fallback markers and archiver settings |
| Is this supported in the target build? | Versioned official contract and target configuration |
| Does this detect the asserted behavior? | Representative evaluation, counterexamples and observation coverage |

Use existing artifacts and source review for this reconciliation. A curated
attack reference is not authorization to execute its payload or reproduce an
intrusion. Report the conceptual prerequisite and defensive evidence relevant to
the question.

## Finish with an Auditable Answer

Name the selected resource and selection reason, cite the exact supporting
artifact, state its scope and identify the unresolved gap. Avoid replacing the
answer with a long undifferentiated tool list. For a resource-description edit,
write purpose + platform/scope + distinctive value + material limitation.

Use [repository navigation](../../overview/references/repository-navigation.md)
for path resolution and
[skill evaluation](skill-evaluation.md) to review whether the selected material
actually improved the answer.
