---
title: Input Provenance
kind: concept
topics: [anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/AtakanKeser__BlastScale.md
  - wiki/sources/descriptions/GloriousBrendon__rearguard.md
  - wiki/sources/descriptions/DoomSalat__PEAK-mode-AntiCheat-Sentinel.md
  - wiki/sources/descriptions/Ajitha-2001__aimguard.md
  - wiki/sources/descriptions/multiplayeragent__chompchomp-io.md
  - wiki/sources/descriptions/ToldByNun__earlybuffering-gd.md
updated: 2026-10-30
confidence: high
---

# Input Provenance

Discipline for labeling **where input telemetry came from** and **what it actually measures** before using it in behavioral detectors, replay analysis, or enforcement. Client-uploaded fields are adversarial; server authority improves trust but does not eliminate clock, replication, schema, or game-logic errors. (source: wiki/sources/skills/anti-cheat.md)

## Observation coverage

| Observation | Can establish | Remains separate |
|-------------|---------------|------------------|
| Raw input on client | Values reported through that local path | Human intent, collector integrity, game interpretation |
| Client-uploaded fields | What the protocol supplied to the receiver | Hardware origin and completeness |
| Server-observed state | State recorded at that server stage | Every input sample and rendered view |
| Replication replay or video | Content the capture path retained | Omitted states, transforms, original timing |
| Callback/provider event | Observation within that channel's scope | Coverage of other operations or the whole host |

Server storage does not turn a client-supplied field into an independently measured fact; movement pipelines may combine, correct, or smooth data. (source: wiki/sources/skills/anti-cheat.md)

## Trust labels

For each telemetry field record:

| Label | Meaning |
|-------|---------|
| Server-observed | Measured or derived on authoritative server state |
| Server-derived | Computed from trusted server inputs |
| Client-reported | Uploaded by client; treat as untrusted until validated |
| Reconstructed | Interpolated or inferred from partial samples |

Separate **server tick records** from **raw-device or sub-tick coverage**—tick logs alone do not establish HID polling granularity.

## Measurement prerequisites

Before measuring reaction time, time-to-lock, or aim trajectories:

- Declare coordinate spaces (device-relative, normalized absolute, viewport pixels, view-angle degrees); pixel metrics require supported pixel data or documented conversion.
- Record origin, units, sample rate, aggregation, and validation per field.
- Use the highest reliable timestamp precision supported by input, engine, transport, and clock sync.
- Distinguish **world**, **replicated**, **replay**, and **displayed** visibility when defining target-visibility intervals.

## Replay fidelity

Server-side replay reconstruction must:

- Preserve missing intervals, transformations, and interpolation uncertainty.
- Reconstruct only the sampled trajectory supported by recorded data.
- Pair with [[research-rigor]] time/ordering checks before interpreting trajectories or latency distributions.

Mobile puzzle backends such as [[blastscale]] issue level seeds and replay submitted moves through a deterministic board engine before a chain-of-responsibility pipeline validates timing, score bounds, and move sequences—treat replayed server state as **server-derived**, not client-reported scoring. (source: wiki/sources/descriptions/AtakanKeser__BlastScale.md)

## Missing-event discipline

Before interpreting absent callbacks, ETW events, or input samples as evasion:

- Record provider enablement, collector continuity, schema compatibility, observation window, and buffer-loss statistics—empty output may reflect collection failure.
- Treat undocumented cross-subsystem effects as unverified unless supported for the actual build and provider.
- Losing one callback channel (e.g. `ObRegisterCallbacks` handle operations) does not prove all independent evidence sources are unavailable.

Behavioral features remain hypotheses until provenance, units, and collector coverage are documented. (source: wiki/sources/skills/anti-cheat.md)

Open-source SDKs such as [[rearguard]] (GloriousBrendon; Rust server + Godot 4 GDExtension; per-match server-seeded probes in mouse sensitivity and recoil parameters—clients reacting to hidden cues expose automation; treat probe parameters as **server-derived** gameplay state and client input reactions as **client-reported** evidence requiring corroboration) illustrate probe-based input-trust labeling without kernel drivers. (source: wiki/sources/descriptions/GloriousBrendon__rearguard.md)

BepInEx host plugins such as [[peak-mode-anticheat-sentinel]] attribute PEAK item-spawn RPCs and network instantiations to the **Photon message sender** assigned by the server—label that sender as **server-observed** network identity before blocking forged pickups or inventory rewrites on the host. (source: wiki/sources/descriptions/DoomSalat__PEAK-mode-AntiCheat-Sentinel.md)

Server-side AC prototypes such as [[aimguard]] apply grid-based **potential visibility sets (PVS)** to cap client replication—treat aim/movement features validated through lag-compensated server rules as **server-derived** while keeping replication-bound visibility intervals separate from raw **client-reported** aim samples. (source: wiki/sources/descriptions/Ajitha-2001__aimguard.md)

Browser `.io` reference [[chompchomp-io]] narrows the client protocol to validated **steer, boost, and fire** commands at 20 Hz while authoritative simulation covers movement, pickups, bullets, collisions, and scoring—label those commands **client-reported** and treat world/combat outcomes as **server-derived** unless independently measured. (source: wiki/sources/descriptions/multiplayeragent__chompchomp-io.md)

Geode timing-assist mod [[earlybuffering-gd]] holds slightly early jump presses until an internal **shadow physics** tick still classifies release as safe—label emitted jump events **client-reported**; the planner, buffer state machine, and optional per-level learning run entirely on the client with no server corroboration of raw HID timing or shadow-tick decisions. (source: wiki/sources/descriptions/ToldByNun__earlybuffering-gd.md)

## Related

[[ai-aimbot-detection]] · [[blastscale]] · [[rearguard]] · [[peak-mode-anticheat-sentinel]] · [[chompchomp-io]] · [[earlybuffering-gd]] · [[hardware-input-injection]] · [[research-rigor]] · [[overviews/anti-cheat]] · [[overviews/game-hacking]]
