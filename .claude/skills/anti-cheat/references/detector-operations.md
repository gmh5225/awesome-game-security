# Detector Reliability, Rollout, and Decision Recovery

Primary-source review: 2026-09-09. This applies general observability,
reliability and incident-response principles to game-security detectors; it is
not a description of any provider's enforcement policy.

## Separate Health, Evidence, Results, and Decisions

| State | Record | Do not infer |
|---|---|---|
| Collector/service health | Version, restart, resource pressure, queue and pipeline errors | Player misconduct or innocence |
| Evidence validity | Source, coverage, delay, missing/duplicate records and schema compatibility | Missing data equals a measured zero |
| Detector execution | Evaluated/not-evaluated, model/rule version, assumptions and result | A score itself authorizes a sanction |
| Decision state | Evidence, policy version, actor, review and correction history | Infrastructure error is behavioral evidence |

This table is a local engineering model. OpenTelemetry provides collector
health metrics, but a send failure does not inherently establish permanent
data loss: retries may recover delivery.
[OpenTelemetry internal telemetry](https://opentelemetry.io/docs/collector/internal-telemetry/)

Represent evidence as available, delayed, partial, invalid, unsupported or
not-collected as appropriate; record evaluated/not-evaluated separately. Missing
evidence is neither a clean result nor proof of misconduct. Access continuity,
authentication requirements and sanctions need separately documented policies;
do not prescribe universal fail-open or fail-closed behavior for all of them.

## Time and Shared Failure Context

Distinguish source-event time, collector observation, server receipt and decision
time. OpenTelemetry's `Timestamp` and `ObservedTimestamp` illustrate this
distinction. Their difference need not be pure network latency; the clocks and
collection path also matter.
[OpenTelemetry logs model](https://opentelemetry.io/docs/specs/otel/logs/data-model/)

Record the expected and observed coverage window, delay budget, clock uncertainty,
duplicates, ordering, and source of missingness. Compare anomalies by region,
platform, collector version, rollout cohort and shared backend. Simultaneous
gaps support investigation of shared failure but do not settle root cause.
A healthy collector is also not proof that every client-origin field is true.

Preserve observations, alternatives and investigation records with integrity
and provenance. NIST distinguishes event analysis from declaring incidents and
emphasizes investigation evidence; the player-specific interpretation remains
the application's responsibility.
[NIST SP 800-61r3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

## Stage Collection, Feature, Rule, and Model Changes

Use offline review, shadow evaluation without sanction effects, and a bounded
candidate cohort with a suitable control before expanding a consequential
change. Isolate shadow writes, caches and derived state so they do not silently
influence real decisions.

Compare data coverage, delivery age, errors, evaluated counts, trigger rates
and review burden under matched windows. A lower trigger rate may reflect
missing input. Shared dependencies can contaminate both candidate and control;
a successful canary does not certify detector validity or low false positives.
[Google SRE canarying](https://sre.google/workbook/canarying-releases/)

Preserve collector, schema, feature transformation, rule/model, threshold,
configuration, policy and cohort versions. Define expansion/stop/recovery
criteria and owners for the deployment; avoid universal sample percentages
or observation durations.

## Recover Decisions as Well as Code

Rolling back a detector does not automatically reverse prior sanctions, repair
derived data or recover lost evidence. Identify affected decision windows and
versions, then review supporting and contrary evidence under the applicable
policy. Preserve the original decision and any correction as separate records.

Post-deployment monitoring, incident handling, overrides and review mechanisms
are addressed in voluntary general AI risk-management guidance. They are not
evidence that a particular game implements a specific appeal process.
[NIST AI RMF Playbook: Manage](https://airc.nist.gov/airmf-resources/playbook/manage/)

Minimum review record: session/cohort, observation window, health evidence,
event/observed/decision times, coverage and uncertainty, all relevant versions,
evaluated status, result, counterevidence, related incident, decision actor,
review/correction history and recovery owner. Apply
[research-rigor](../../research-rigor/SKILL.md) to the conclusion.
