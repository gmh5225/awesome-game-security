---
title: Detector Operations
kind: concept
topics: [anti-cheat]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md
  - wiki/sources/descriptions/modcommunity__dot-server-security.md
  - wiki/sources/descriptions/IDELd__SAC-The-server-AntiCheat.md
  - wiki/sources/descriptions/ChmonyaStudio__cs2-anticheat-by-chmonya.md
  - wiki/sources/descriptions/ThoriumAC__Thorium-Minecraft-Plugin.md
  - wiki/sources/descriptions/Benardelys__H-AC.md
  - wiki/sources/descriptions/AbdulAmi09__SentinelAntiCheat.md
  - wiki/sources/descriptions/NetVar1337__apex-anticheat-lab.md
  - wiki/sources/descriptions/severrir__AntiCheat-Dashboard.md
  - wiki/sources/descriptions/kroshtan__esp-killer.md
  - wiki/sources/descriptions/TypeThe0ry__MCAce.md
  - wiki/sources/descriptions/maximumemails-cmd__RainInjectable.md
  - wiki/sources/descriptions/dhehdjebejen-beep__Bastion.md
  - wiki/sources/descriptions/Kotsasmin__key-value-checker.md
  - wiki/sources/descriptions/Chanhne-dev__AntiCheat.md
  - wiki/sources/descriptions/AODOJUST__gomoku-anti-cheat-detector.md
  - wiki/sources/descriptions/vylorq__anti-cheat.md
updated: 2026-10-03
confidence: high
---

# Detector Operations

Operational concerns for **running detectors in production**: service health, shadow/canary evaluation, rollout/recovery, and separating collector faults from misconduct attribution. Pair with [[research-rigor]] when a detector hit becomes an enforcement recommendation. (source: wiki/sources/skills/anti-cheat.md)

## State separation

| State | Record | Do not infer |
|-------|--------|--------------|
| Collector/service health | Version, restart, resource pressure, queue/pipeline errors | Player misconduct or innocence |
| Evidence validity | Source, coverage, delay, missing/duplicate records, schema compatibility | Missing data equals a measured zero |
| Detector execution | Evaluated/not-evaluated, rule/model version, assumptions, result | A score alone authorizes a sanction |
| Decision state | Evidence, policy version, actor, review/correction history | Infrastructure error is behavioral evidence |

Represent evidence as available, delayed, partial, invalid, unsupported, or not-collected; record evaluated/not-evaluated separately. Access continuity, authentication requirements, and sanctions need separately documented policies. (source: wiki/sources/skills/anti-cheat.md)

## Deployment lifecycle

1. **Shadow / canary** — run new rules without punitive action; measure prevalence, FPR/FNR, precision, recall, calibration, and expected review volume on representative held-out data.
2. **Rollout** — segment by game mode, patch, platform, input method, and population slices; report confidence intervals, not uncalibrated scores in `[0, 1]`.
3. **Recovery** — preserve counterevidence and appeal paths; use human review or independently trusted evidence before high-impact punitive action when false positives remain plausible.

## Collector health vs misconduct

Diagnose the observation path first:

- Heartbeat timing anomalies may reflect scheduling, transport, collector, or backend faults—not cheating.
- Apply documented **access-continuity policy** separately from misconduct attribution; heartbeat failure alone does not establish sanction grounds.
- Service faults, missing uploaded fields, and detector pipeline errors are operational incidents until corroborated by independent signals.

## Time domains

Distinguish source-event time, collector observation, server receipt, and decision time. Record expected/observed coverage window, delay budget, clock uncertainty, duplicates, ordering, and source of missingness. Compare anomalies by region, platform, collector version, and rollout cohort—simultaneous gaps support shared-failure investigation but do not settle root cause; a healthy collector is not proof that every client-origin field is true. (source: wiki/sources/skills/anti-cheat.md)

## Joint error measurement

- Combine **causally distinct** signals; correlated detectors can fail together.
- Maximum-score aggregation or a fixed signal count does not guarantee a lower false-positive rate—measure joint error on held-out populations.
- Retrain periodically when adversaries adapt; validate session-level aggregation for cross-session dependence and drift.

Production server plugins such as [[anticheatsystem]] aggregate modular analyzer hits into JSON-configured suspicion scores before log/report/ban escalation via shared admin APIs—tune thresholds and module weights with shadow/canary runs before enabling automatic sanctions. (source: wiki/sources/descriptions/pavelinbs-afk__anticheatsystem.md) CS2 server plugins such as [[sac-the-server-anticheat]] implement four-stage progressive warning/ban ladders and elevate mass-check sensitivity after multiple in-game player reports—audit escalation thresholds before enabling automatic sanctions. (source: wiki/sources/descriptions/IDELd__SAC-The-server-AntiCheat.md) CounterStrikeSharp CS2 plugins such as [[cs2-anticheat-by-chmonya]] run per-tick modular heuristics (aim snap/jerk, DMA subpixel mouse emulation, triggerbot/prefire/wallbang, HvH anti-aim/spinbot) into a decaying suspicion score with JSON ban persistence, Discord webhook alerts, and in-game admin threshold/whitelist controls—calibrate module weights before enabling auto-ban. (source: wiki/sources/descriptions/ChmonyaStudio__cs2-anticheat-by-chmonya.md) Minecraft Paper/Spigot/Folia plugins such as [[thorium-minecraft-plugin]] split an **auditable open collector** (PacketEvents capture of movement, combat, block interaction, transactions, and nearby world geometry from server-received packets; WebSocket + protobuf transport) from a **closed-source remote inference engine**—treat engine outages, transport faults, and verdict latency as collector/service-health incidents distinct from misconduct attribution; audit optional staff-alert/warning/kick/ban enforcement wiring before enabling automatic sanctions. (source: wiki/sources/descriptions/ThoriumAC__Thorium-Minecraft-Plugin.md) Paper **1.21** plugins such as [[h-ac]] run dozens of isolated combat/movement/world checks with per-module thresholds, punishments, and **violation decay**; server TPS safeguards and asynchronous logging keep enforcement off the hot path—tune decay and punishment ladders with staff review commands before enabling automatic sanctions. (source: wiki/sources/descriptions/Benardelys__H-AC.md) Paper/Spigot plugins such as [[key-value-checker]] (Kotsasmin; Java; join-time PacketEvents translation-key probes via fake signs—unresolved keys on vanilla clients vs resolved mod strings on cheat clients—treat packet parse failures and join latency separately from hit attribution; tune blacklist/whitelist groups before enabling automatic kicks) (source: wiki/sources/descriptions/Kotsasmin__key-value-checker.md) Paper/Folia plugins such as [[chanhne-dev-anticheat]] (Chanhne-dev; Java; periodic scan tasks for movement/fly and illegal-item checks; Meteor/TrouserStreak/NoraTweaks client-specific modules; violation tracking with configurable enforcement, Discord webhooks, and optional movement logging—tune scan intervals and punishment ladders before enabling automatic sanctions) (source: wiki/sources/descriptions/Chanhne-dev__AntiCheat.md) Chess integrity platforms such as [[sentinel-anticheat-chess]] fuse seven statistical engine-assistance signal layers into explainable risk tiers with hash-chained audit logging, case management, and live monitoring—treat fused scores as review evidence for arbiters rather than autonomous sanction triggers. (source: wiki/sources/descriptions/AbdulAmi09__SentinelAntiCheat.md) Browser-side Gomoku triage tools such as [[gomoku-anti-cheat-detector]] (AODOJUST/Baishen; Chrome/Edge extension; local Rapfi WASM post-game replay with optional KataGomo/Rapfi backends; 0–100 risk scores; sample-library threshold learning, archive viewer, player blacklist, multilingual chat questioning; optional Supabase sync) produce moderator hints from engine-agreement signals—calibrate suspicion cutoffs from labeled samples before treating scores as misconduct evidence. (source: wiki/sources/descriptions/AODOJUST__gomoku-anti-cheat-detector.md) FPS behavioral research labs such as [[apex-anticheat-lab]] extract server-side aim-kinematics and triggerbot telemetry, fit per-cohort baselines, and rank players for analyst review with explainable threshold documentation—calibrate cohort segmentation and rank outputs in shadow mode before enabling automatic enforcement. (source: wiki/sources/descriptions/NetVar1337__apex-anticheat-lab.md) Roblox Luau server AC such as [[anticheat-dashboard]] fuse movement, combat, network, timing, and client-integrity signals through a **trust-scoring engine** that requires **corroboration before kicks**, pairing honeypots and bait traps with a Supabase-backed staff console for human-in-the-loop banning rather than fully automated punishment—audit corroboration thresholds and appeal workflows before enabling auto-kick. (source: wiki/sources/descriptions/severrir__AntiCheat-Dashboard.md) The Isle: Evrima server-side ESP detection such as [[esp-killer]] polls read-only RCON position snapshots and flags movement inconsistent with line-of-sight—heading toward hidden players or implausible arrival speeds—routing **admin alerts for human review** rather than automatic bans; calibrate heuristics on representative server traffic before enabling enforcement. (source: wiki/sources/descriptions/kroshtan__esp-killer.md) Minecraft network stacks such as [[mcace]] (TypeThe0ry; Fabric client mod + proxy/backend plugins; consent-gated signed client-visibility telemetry correlated with server-side AC evidence; Ed25519-signed frames; fail-closed policy evaluation; bounded disposition ladder observe/warn/challenge/quarantine rather than silent persistent monitoring) for administrators who need auditable admission workflows—audit policy thresholds before enabling quarantine or challenge actions. (source: wiki/sources/descriptions/TypeThe0ry__MCAce.md) Fabric **1.21.11** offline-mode security suites such as [[bastion]] (dhehdjebejen-beep; BastionAuth/BastionClaims/BastionAC three-mod stack; 38 outcome/signature AC checks with buffered violation levels and decay; Meteor/Wurst client coverage; configurable thresholds and staff panels; no client install) for server operators who need layered account, territory, and fair-play enforcement—tune violation decay and punishment thresholds before enabling automatic sanctions. (source: wiki/sources/descriptions/dhehdjebejen-beep__Bastion.md) Fabric **1.21.11** review-first AC such as [[vylorq-vigil]] (vylorq; Java; movement upper-bound prediction, lag-compensated reach/aim/autoclick checks, anti-x-ray ore hiding; Watcher telemetry; violations scored into admin review cases with evidence clips—no automatic bans; Vigil Panel GUI; optional Geyser/Floodgate crossplay) for operators who want human-in-the-loop disposition—audit case thresholds and evidence-clip workflows before enabling punitive actions. (source: wiki/sources/descriptions/vylorq__anti-cheat.md) Minecraft **1.8.9** injectable passive-observer runtimes such as [[rain-injectable]] (maximumemails-cmd; C++/JNI inject + Java 8 detection runtime; temporal analysis over other players' combat/movement; local evidence export and GUI review overlays without server telemetry or automatic sanctions) for researchers who need client-side cheat observation with human-in-the-loop disposition—calibrate review thresholds before treating flagged candidates as misconduct evidence. (source: wiki/sources/descriptions/maximumemails-cmd__RainInjectable.md) Godot dedicated-server addons such as [[dot-server-security]] ship **dry-run by default**, logging rule hits and escalation ladders (warn/gag/mute/kick/ban) without punitive action until operators finish auditing configuration. (source: wiki/sources/descriptions/modcommunity__dot-server-security.md)

## Related

[[research-rigor]] · [[input-provenance]] · [[ai-aimbot-detection]] · [[overviews/anti-cheat]]
