# Game Security Skill Coverage and Quality Roadmap

Review baseline: 2026-09-09, following the initial 10-skill enrichment.
This is a prioritized gap assessment of this repository, not a ranking against
all other skill libraries. Source quantity and document length are not quality scores.

## Coverage Status

| Area | Gap found in the baseline | This iteration | Further evidence needed |
|---|---|---|---|
| Server authority and backend economy | Mostly topic names and general server-authority advice | Dedicated operation, authorization, purchase and transaction review skill | Owned-service fixtures and provider/version-specific case studies |
| Build/update/mod supply chain | Plugin provenance and package signing without an end-to-end release model | Dedicated release-authority, update, provenance and content-boundary skill | Implementation-specific update/recovery and release-pipeline evidence |
| Desktop Linux and Proton | Scattered tool/platform mentions without a coherent trust model | Dedicated runtime, credential, namespace and policy skill | Representative distro/runtime/game compatibility matrix |
| Robustness and remediation | Tool names without a shared diagnostic-evidence workflow | Owned-build contracts, sanitizer limits and artifact-triage reference | Project-specific regression artifacts and reviewed fixes |
| Skill behavior | No checked-in routing and answer-quality case suite | Public scenario suite, local validator and evaluation rubric | Repeated model runs, comparison baselines and separately held-out cases |
| Legacy technical claims | New evidence rules coexist with older detailed catalogs | Existing catalogs retained; new material cites primary sources | Claim-by-claim review of historical thresholds, layouts, compatibility and detectability claims |

## Priorities Beyond This Iteration

1. **Evidence debt:** audit high-impact legacy assertions first. Record exact
   versions and direct support; remove universal rankings and unsupported
   certainty. Review contradictions where new rules meet old examples.
2. **Entry-point size:** seven baseline entrypoints exceed 500 lines; DMA is
   1,800 lines and Windows kernel 1,178. Refactor by actual task only after
   identifying necessary references and verifying routing/answer regressions.
   Preserve source provenance and working links during any extraction.
3. **Portable naming:** nine baseline `name` values differ from their containing
   folder names. Existing names are preserved in this iteration. Agent Skills
   portability requires evaluating a naming migration and its invocation/link
   impact before claiming strict cross-client compatibility.
4. **Independent evaluation:** compare the same cases with and without relevant
   skills and alongside unrelated skills. Track useful task completion,
   unsupported claims, references loaded, latency and context cost. Published
   regression cases are not a hidden benchmark.
5. **Remaining domain breadth:** assess concrete demand for macOS/Apple Silicon,
   console/cloud-streaming boundaries, script/WASM mod isolation, incident
   response and disclosure coordination before adding more entrypoints.

The line-budget and naming guidance comes from the
[Agent Skills specification](https://agentskills.io/specification) and
[Claude Code skill documentation](https://code.claude.com/docs/en/skills).
These are portability and authoring concerns, not proof that a large skill
always performs poorly. Runtime-specific behavior needs testing.

## Quality Claims Must Have a Comparison

For a claim of improved effectiveness, report the task population, model and
settings, repository revision, selected skills/references, baseline, raw outputs,
review rubric, reviewer independence, and observed failures. Evaluate correct
selection, appropriate non-selection, overlap, and ambiguous questions.
[Skill authoring and evaluation guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

Use the [evaluation guide](../../research-rigor/references/skill-evaluation.md)
for this repository's local case format. Do not turn a validator pass, one
reviewer's score, or a small smoke sample into a world-leading quality claim.
