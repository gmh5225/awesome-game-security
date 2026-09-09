# Input Provenance, Units, and Observation Coverage

Primary-source review: 2026-09-09. Use this reference before turning input,
trajectory, callback or missing-event observations into a detector claim.

## Identify What Was Actually Observed

| Observation | What it can establish | What remains separate |
|---|---|---|
| Raw input collected on a client | Values reported through that local collection path | Human intent, collector integrity and game interpretation |
| Client-uploaded input fields | What the protocol supplied to the receiver | Actual hardware origin and completeness |
| Server-observed view/action state | The state recorded at that server stage | Every input sample and the player's rendered view |
| Replication replay or video | The content that the capture path retained | Omitted states, transforms and exact original timing |
| A callback/provider event | An observation within that channel's documented scope | Coverage of other operations or the whole host |

Server storage does not change a client-supplied field into an independently
measured fact. Movement pipelines can combine, correct and smooth data; this
limits what a server tick record alone establishes.
[Epic networked movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine)

## Preserve Units and Transformations

Windows `RAWMOUSE` distinguishes relative motion from normalized absolute
coordinates. Its values are not automatically viewport pixels or view-angle
degrees. Raw input also differs from legacy cursor movement processing.
[Microsoft RAWMOUSE](https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-rawmouse)

For every feature declare the observed coordinate space, transformation, viewport,
sensitivity/input configuration, sampling interval and aggregation. Use pixels
only when a pixel-space observation or supported conversion exists. Specify a
rate's denominator: input samples, simulation ticks, elapsed time or engagements.
A fixed small-pixel cutoff is not a universal micro-correction definition.

Reconstruct only the sampled trajectory supported by the data. Label gaps,
quantization and interpolation; additional decimal places cannot recover lost
samples. Use the [time and replay reference](../../game-server-security/references/time-ordering-and-replay.md)
for clock-domain and visibility distinctions.

## Missing Events Need a Collector Explanation

Debugger behavior, ETW collection and object callbacks are different mechanisms.
The documented `NtSetInformationThread` contract does not establish the general
claim that a debugger-related thread setting makes a thread invisible to ETW.
Treat undocumented cross-subsystem effects as unverified unless supported for
the actual build/provider.
[Microsoft NtSetInformationThread](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationthread),
[ETW model](https://learn.microsoft.com/en-us/windows/win32/etw/about-event-tracing)

`ObRegisterCallbacks` concerns specified handle operations, not every operation
on the host. Losing one callback channel does not prove all independent evidence
sources are unavailable.
[Microsoft ObRegisterCallbacks](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-obregistercallbacks)

Before interpreting absent events, record provider enablement, collector
continuity, event class, schema compatibility, observation window and available
event/buffer-loss statistics. ETW exposes loss counters; empty output can reflect
collection failure rather than an absence of activity.
[ETW session properties](https://learn.microsoft.com/en-us/windows/win32/api/evntrace/ns-evntrace-event_trace_properties)

## Interpret Behavioral Features as Hypotheses

Consistency, field-of-view boundaries, engagement rate and switching regularity
are candidate measurements, not universal definitions of automation or human
play. Validate on matched game/input/skill populations with legitimate assistive
tools, preserve contrary examples, and separate correlated features from
independent evidence. Use [research-rigor](../../research-rigor/SKILL.md).

Report field origin, observer, coordinate/time space, transforms, coverage,
validation limits and the narrow supported finding. For operational failures,
continue with [detector operations](detector-operations.md).
