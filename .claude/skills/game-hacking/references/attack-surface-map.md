# Attacker Capabilities and Defense Coverage

Primary-source review: 2026-09-09. This table is an analytical taxonomy of
threats, not a claim that every game exposes each surface or that a named tool
implements it. Capabilities can be combined; they do not form a required ladder.

## Threat Families

| Family and goal | Necessary capability or failed boundary | Defender observations and controls | Counterexample or coverage limit |
|---|---|---|---|
| Client-state observation: learn hidden game state | Access to relevant client-resident data | Minimize unnecessary replication; correlate host and process evidence | Read-only access can affect fairness without changing memory |
| State manipulation: influence consequential outcomes | Ability to modify local/submitted state plus insufficient authoritative validation | Validate consequential actions and state transitions on the server | Prediction, rollback, latency, and game bugs can resemble anomalies |
| Process injection or unauthorized code modification | A path enabling foreign code or modification in the process | Module/code provenance, integrity findings, and source of execution | Legitimate instrumentation and plugins can produce similar artifacts |
| Privileged driver/interface abuse | A reachable privileged interface and permissions or a flaw exposing sensitive operations | Driver inventory, interface authorization, input validation, active policy | Signature validity does not establish safe functionality |
| Hardware DMA observation or modification | A DMA-capable requester and accessible mappings | Device isolation, mapping policy, platform evidence | Control scope depends on topology, driver, firmware, and OS state |
| Host-mediated remote acquisition | Host acquisition access plus a transport path | Acquisition component provenance and appropriate host/device evidence | Remote analysis does not turn CPU/kernel acquisition into hardware DMA |
| Graphics modification or overlay abuse | Access to rendering state or a composition surface | Distinguish application, presentation, compositor, and capture evidence | Recording tools and accessibility overlays are legitimate controls |
| Visual automation: infer actions from rendered output | Available frames and a decision mechanism | Evaluate gameplay behavior and any available capture context | It need not create a game-memory access artifact |
| Input automation: submit non-human actions | An input-producing path accepted by the application | Correlate device context, input provenance, and longitudinal behavior | Accessibility tools, remappers, and device sharing are benign alternatives |
| Protocol or business-rule abuse | A server accepts untrusted requests or client assertions beyond its intended authority | Validate authorization, state, ordering, and replay-sensitive actions | Retries and reordering are normal and require protocol-aware interpretation |

## Documented Boundaries

In a server-authoritative design, the server's state, replicated client state,
prediction, and presentation are distinct. Investigate which information is
sent to which client and who validates each consequential action; do not assume
that a local change affects authoritative state.
[Epic networking overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine)

Windows Raw Input supports distinguishing source devices of the same type.
This can provide device context, but is not authentication of human intent.
`SendInput` has documented integrity-level restrictions; synthetic input APIs
are not universal guarantees of delivery. Neither fact establishes a detector
for every input automation technique.
[Raw Input overview](https://learn.microsoft.com/en-us/windows/win32/inputdev/about-raw-input),
[SendInput](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput)

Driver threat models must include interface access control and what privileged
operations an interface exposes. A trusted signature cannot substitute for
authorization, constrained functionality, or correct validation.
[Microsoft driver security checklist](https://learn.microsoft.com/en-us/windows-hardware/drivers/driversecurity/driver-security-checklist)

## Write a Useful Attack Description

For a selected family, explain the objective, prerequisite capability, exposed
resource, trust boundary, possible effect, and available evidence. Then state
which control prevents the behavior, which observation only detects a symptom,
which legitimate uses resemble it, and what the current evidence cannot settle.
Identify the source and version supporting each concrete assertion.

Do not substitute tool names or claims of invisibility for a mechanism. A clean
module list does not prove a clean host, an ordinary-looking HID report does
not prove human origin, and a suspicious artifact does not by itself prove
cheating. Detector effectiveness requires representative evaluation, not merely
a demonstration that one synthetic sample triggers a rule.

Follow the relevant domain reference for
[acquisition/transport](../../dma-attack/references/acquisition-and-transport.md),
[graphics observations](../../graphics-api/SKILL.md),
[engine authority](../../game-engine/SKILL.md),
[network restriction evidence](../../anti-cheat/references/network-environment-evidence.md),
and [research validity](../../research-rigor/SKILL.md).
