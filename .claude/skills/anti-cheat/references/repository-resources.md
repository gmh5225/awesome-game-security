# Repository Resources for Detection Evidence

Repository categories and linked primary documentation reviewed: 2026-09-09.
Choose a family by the observation needed and the decision it can support. The
selection and evidence requirements below are defensive review criteria; no
listed project supplies a universal cheating or enforcement verdict.

## Match the Resource to Its Observation Scope

Locate the literal subsection labels under
[`Anti Cheat` in the README](../../../../README.md#anti-cheat). Several categories
mix observation, modification and demonstration projects, so inspect the selected
project's actual scope before adopting its description.

| README location and evidence question | Representative or resource family | Selection boundary and expected output |
|---|---|---|
| `Detection:Hook`: what process-memory anomaly was reported? | [hasherezade/pe-sieve](https://github.com/hasherezade/pe-sieve) | The author describes a single-process inspection engine for suspicious in-memory changes. Review the report against the exact build and legitimate instrumentation context. Preserve process/module provenance and reported regions; an anomaly label alone does not establish malicious intent or whole-host coverage. |
| `Information System & Forensics`: what remains in an acquired memory image? | [volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3) | Select the parser/plugin and symbols for the supplied artifact. Return image provenance, plugin/version, symbol identity, reported objects and unreadable ranges. Acquisition completeness and successful parsing remain separate; missing output can reflect unavailable data. |
| `Windows Ring0 Callback`: which operations can this observation represent? | Callback-reference family, including the indexed `gmh5225/kernel-callback-functions-list` | Verify each callback against its documented contract. For example, [ObRegisterCallbacks](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-obregistercallbacks) covers specified handle operations. Produce an event-to-operation coverage map with registration and collector context. One callback family is not an inventory of all host activity. |
| `Detection:Triggerbot & Aimbot`: what was measured and how reliable is its interpretation? | Behavioral-analysis resource family | Choose studies by data origin, labels, units, population and held-out evaluation. Use [input provenance](input-provenance-and-measurement.md) to separate raw device values, client uploads and server state. Deliver feature definitions, matched benign controls and measured error limits; a model architecture or repository score does not establish deployment accuracy. |
| `Black Signature`: which driver policy applies to the observed file? | Driver-policy index family | Use indexed lists as discovery and verify against [Microsoft's current driver block rules](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules). Preserve file/version/signer, policy identity and effective state. List membership and actual enforcement differ; absence from a list does not establish safety. |

## Avoid Decision and Domain Mismatches

Keep observation, detection inference, risk scoring and enforcement as separate
steps. Use [detector operations](detector-operations.md) for collector faults and
rollout decisions, [network evidence](network-environment-evidence.md) for network
association or restriction claims, and [research-rigor](../../research-rigor/SKILL.md)
for classifier evaluation and corroboration.

Memory acquisition architecture belongs to [dma-attack](../../dma-attack/SKILL.md),
driver correctness to [windows-kernel](../../windows-kernel/SKILL.md), and backend
authority to [game-server-security](../../game-server-security/SKILL.md). The
`Stress Testing` and `Fuzzer` headings also contain executable attack demonstrations;
their category names are not evidence that a project is an observation-only tool.
For owned-build diagnostics use the
[robustness reference](../../research-rigor/references/robustness-and-triage.md).

## Deliver an Evidence-to-Decision Record

Record the precise allegation, required attacker capability, chosen category and
project revision, observed artifact/event, collector health, build and policy
context, competing benign explanation, independent corroboration, measured
coverage limits, and the supported decision. A copied detector label is not a
substitute for the underlying evidence.

Use [shared repository navigation](../../overview/references/repository-navigation.md)
for local layers and upstream verification. Compiled descriptions and wiki pages
are discovery aids; multiple summaries of one project remain one source lineage.
