# Time, Ordering, and Replay Evidence

Primary-source review: 2026-09-09. Pin the engine, networking package, game
build, collector and capture settings. The implementation examples below are
version-specific; they do not define every game's networking model.

## Separate Timelines and Clock Domains

Distinguish input sampling, local prediction, server receipt, authoritative
simulation, durable commitment, replication, presentation and replay playback.
Simulation ticks, network ticks, render frames, monotonic durations and UTC
timestamps are different quantities.

For each field record its source, units, epoch/session origin, resolution and
synchronization uncertainty. QPC supports interval measurement independently of
UTC; finer resolution does not establish cross-machine synchronization accuracy.
Do not subtract unrelated clocks without a justified mapping, or assert an
order when uncertainty exceeds the separation.
[Microsoft high-resolution timestamps](https://learn.microsoft.com/en-us/windows/win32/sysinfo/acquiring-high-resolution-time-stamps)

Unity Netcode for GameObjects distinguishes local and server-time estimates
and network ticks from frame updates. Netcode for Entities documents prediction,
partial ticks and repeated simulation work. These are different packages:
record which contract applies, including buffering and rate settings.
[Netcode for GameObjects 2.13 time](https://docs.unity3d.com/Packages/com.unity.netcode.gameobjects@2.13/manual/advanced-topics/networktime-ticks.html),
[Netcode for Entities 1.4 prediction](https://docs.unity3d.com/Packages/com.unity.netcode@1.4/manual/intro-to-prediction.html)

## Ordering Guarantees Have a Scope

Identify whether a guarantee applies to a connection, channel, actor, object or
application workflow. Unreal's documented reliable RPC ordering within an actor
does not establish cross-actor order. Reliable/unreliable mixtures and separate
RepNotify callbacks do not supply a universal ordering of state changes.
[Epic replicated object execution order](https://dev.epicgames.com/documentation/en-us/unreal-engine/replicated-object-execution-order-in-unreal-engine)

Review authoritative dependencies and state transitions. Client callback order,
visual effects and log arrival order are not interchangeable with committed
gameplay-effect order.

## Prediction, Correction and Resimulation

Unreal character movement can combine submitted moves, apply authoritative
corrections and replay saved moves; remote presentation can use smoothing.
These streams represent different stages of an action.
[Epic networked movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine)

A correction alone does not establish cheating. Preserve simulation tick,
prediction-pass, aggregation and missing-input context where available. Revisited
ticks or several simulation steps in one frame are not necessarily new user
actions. Review effect ownership so recalculation does not become a duplicate
persistent reward, notification or counter update.

## Classify the Recording Before Reconstructing It

An authoritative event log, server-origin replication replay, client-origin
replay, raw-input trace and video capture contain different observations.
Record source perspective, relevance/culling, schema, sampling, checkpoints,
quantization, playback transforms and build compatibility.

Unreal documents that amortized checkpoints can contain actor data from
different frames and cause playback visual errors. It also describes replay
actors affecting shared live objects unless effects are separated. A server
recording therefore does not guarantee a complete synchronous world snapshot
or the player's exact displayed view.
[Epic DemoNetDriver and streamers](https://dev.epicgames.com/documentation/en-us/unreal-engine/demonetdriver-and-streamers-in-unreal-engine)

Reconstruct only supported trajectories and ordering; preserve gaps and
interpolation. Server world visibility, replicated availability, replay
visibility and displayed visibility are separate definitions. State which one
supports a reaction-time measurement.

## Threat and Correctness Review

| Objective or failure | Boundary requiring review | Defensive evidence |
|---|---|---|
| Influence temporal rules with client assertions | Authority over accepted time/state | Validator ownership, provenance and allowed transitions |
| Create inconsistent cross-object effects | Assumed ordering exceeds the delivery contract | Explicit dependencies and authoritative state/version records |
| Duplicate effects during resimulation | Recalculation mistaken for a new committed action | Simulation context, effect ownership and durable operation identity |
| Mislead review using incomplete recordings | Transformed evidence treated as complete truth | Capture provenance, coverage, transformations and counterevidence |
| Playback changes live state | Replay shares consequential effects with live execution | Context separation and shared-object review |

These are conceptual prerequisites, not findings about a particular product.
Use existing records, owned-source review and internal correctness fixtures.
Report event identity, collector, clock domain, simulation context, ordering
scope, observed/committed state, reconstruction and uncertainty. For input units
and collector provenance, use
[input measurement](../../anti-cheat/references/input-provenance-and-measurement.md).
