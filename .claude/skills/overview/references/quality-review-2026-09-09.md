# Skill Quality Review — 2026-09-09

This review found and corrected material errors. It does not establish perfection
or a world-leading rank. The supported outcome is a more consistent research
library with inspected source contracts and recorded, limited model evaluations.
Baseline: [ddf9d7f](https://github.com/gmh5225/awesome-game-security/commit/ddf9d7fea2d8e802ef532f235f02fca63ae8c49a).

## Corrections to Existing Guidance

| Finding | Corrected interpretation and location |
|---|---|
| Informal firmware tiers predicted certain detection or a mandatory TPM path | Device labels require observed dimensions and evaluated coverage; see [DMA assurance boundaries](../../dma-attack/references/assurance-boundaries.md) and [anti-cheat](../../anti-cheat/SKILL.md) |
| EPT events, device DMA, platform-feature flags and complete protection were conflated | Distinguish requester, CPU/device translation, supported/configured/running state, policy authority and observed enforcement |
| TPM/PCR summaries overgeneralized reset rules, key trust and runtime coverage | Preserve profile, selected measurements, enrollment, freshness and appraisal scope; do not certify unmeasured behavior |
| Generic live device-register changes were recommended as classification or containment | Follow documented platform ownership and lifecycle; require isolation-completion and recovery evidence |
| Root privileges and tool names implied kernel execution or fixed concealment rankings | [Mobile security](../../mobile-security/SKILL.md) separates credentials, components, tool modes, observation scope and actual TLS configuration |
| Historical kernel layouts, thresholds and pool tags were promoted to universal interfaces or identity | [Windows kernel](../../windows-kernel/SKILL.md) now uses public allocation contracts, matched symbols and corroborated attribution; Pool2 has no automatic old-kernel fallback |
| WHP was described as a user-process hypervisor with a generic syscall exit | Windows and [reverse engineering](../../reverse-engineering/SKILL.md) now agree on host/guest scope, API-specific support, capabilities and documented exit context |
| Instrumentation and binary-diff tools received unsupported best-tool or completeness claims | Evaluate semantic fidelity, input/coverage scope, observer effects and independently checked matches |
| Screenshot methods, Present calls and physical display contents were equated | [Graphics evidence](../../graphics-api/SKILL.md) distinguishes capture and presentation stages, missing data and relevant controls |
| Pixel color/alpha was said to establish depth-test bypass | Shader output requires pipeline, depth/stencil, blending and event context before a visibility conclusion |
| Firmware/DMA and input-device categories implied universal concealment advantages | [Game threat analysis](../../game-hacking/SKILL.md) records prerequisites, observation channels, benign uses and unresolved coverage |

The relevant skills cite primary contracts beside the corrected claims. This was
a targeted audit of these families, including duplicate assertions in related
skills. Remaining historical examples are not thereby revalidated.

## Actual Evaluation Results

[Inputs, raw outputs and judgments](../../research-rigor/assets/review-2026-09-09.json)
are retained for inspection. Expected routes and reviewer rubrics were withheld
from the answering agents; each evaluator started without conversation history.

| Evaluation | Result | Meaning and limit |
|---|---|---|
| Description-only routing on the original 40 public cases | 38 primary choices matched the predefined acceptable set | Routing agreement, not task-answer accuracy |
| Review of the two mismatches | One underspecified generic sanitizer question; one capability omitted from the description | Choosing no game-security skill for the original generic question was reasonable |
| Targeted follow-up after description/fixture edits | 5/5 agreed, including three unrelated controls | Small follow-up; not a repeated full 40-case comparison |
| Six separate document-based technical answers | No material error identified in the bounded review | Firmware, EPT/DMA, attestation, presentation, depth state and trace/diff scope; no hardware experiments |
| Expanded public suite | 48 cases: 13 positive, 32 boundary, 3 unrelated | Metadata validation is separate from model execution; all 48 were not run as a new batch |

The sanitizer fixture now specifies a game-asset parser review. The research-rigor
description exposes owned-game diagnostics, sanitizer limits and untrusted
retrieved instructions already supported by its body. Keep the original mismatch
and changed fixture visible; do not report these edits as a clean paired increase
from 38/40 to 40/40.

The evaluation used inherited model/settings without an override. Exact backend
revision and sampling settings were not independently recorded. There was no
skills-disabled, competing-library or cross-model baseline, repeated trial, or
held-out population. These limits prevent comparative leadership or production
error-rate claims.

## Structural Review and Preserved Requirements

All 13 skill entrypoints retain their original invocation names. Their complete
Data Source suffixes were compared with the baseline and preserved byte-for-byte,
including direct wiki/README links, description/archive URL templates and fallback
guidance. Supporting references supplement those sections.

Frontmatter and changed local links were checked; the offline repository indexer's
six functional tests and the evaluation metadata validator passed. These checks
cover document structure and local helper behavior, not every external link or
every old technical assertion.

## Remaining Work Before Stronger Claims

- Nine frontmatter names differ from their containing folder names. Strict
  Agent Skills portability is not established; preserve existing invocations
  while planning and checking a migration.
- Seven entrypoints still exceed 500 lines, including the required direct
  Data Source material. Refactor conditional catalogs by task without removing
  those source sections, and measure the resulting reference use and behavior.
- Historical protocol fields, hardware parameters, driver/tool inventories,
  VMCS tables, mobile platform compatibility and old code examples still need
  version-specific review. Public repository availability is not verification.
- Use representative owned artifacts, legitimate edge cases, repeated runs,
  separately held-out tasks and matched baselines for broader effectiveness
  claims. Device, runtime and production behavior remain unevaluated here.

The naming and progressive-disclosure criteria come from the
[Agent Skills specification](https://agentskills.io/specification). The emphasis
on realistic evaluations follows
[Claude skill-authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
Neither source is a certification or a ranking of this collection.
