# Server and Network Resource Selection

Load this guide to select repository resources for one network or backend
boundary. Locations below match the local [README](../../../../README.md),
checked on 2026-09-09. Use
[repository navigation](../../overview/references/repository-navigation.md) for
local discovery and evidence limits.

## Select by Responsibility

| README location and representative | Select when | Contract and common confusion | Expected review output |
|---|---|---|---|
| `Game Network > Source`: [KCP](https://github.com/skywind3000/kcp) | Reviewing how a project integrates a reliable ARQ protocol | Upstream delegates lower-layer packet I/O and clock input to the caller. Review the integration's transport security, scheduler, bounds, and identity separately. Pin the actual branch/version; a transport conversation identifier is not an authenticated game account. | Protocol/integration split, timing source, delivery requirements, connection lifecycle, and unresolved security responsibilities |
| `Game Network > Source`: [GameNetworkingSockets](https://github.com/ValveSoftware/GameNetworkingSockets); `Game Network > Guide`: [ISteamNetworkingMessages](https://partner.steamgames.com/doc/api/ISteamNetworkingMessages) | Separating a messaging library from platform services and an implicit-session API | The open-source library provides a subset of the Steamworks functionality; platform authentication, signaling, and relay services have separate availability contracts. Messages establishes underlying connections implicitly, while Sockets exposes explicit connection management. Neither choice decides game-object permissions. | Exact implementation/SDK, enabled services, identity-validation state, delivery/ordering scope, and per-operation authorization owner |
| `Game Network > Source`: [Pitaya](https://github.com/topfreegames/pitaya) | Mapping a distributed game's frontends, backend handlers, and service dependencies | This is a game-server framework with clustering support. A framework's RPC or session abstraction is not evidence that the application's ownership, economy, or admin rules are enforced. Match framework version and deployed topology. | Principal-to-handler-to-state map, service trust boundaries, validation owner, persistence effects, and missing policy evidence |
| `Game Network > JWT / Auth Token`: the repository's token-tool discovery lane | Reviewing token validation in owned backend code | A testing/inspection tool category is not an identity provider or production validation library. Use the actual issuer/library contract and [RFC 8725](https://www.rfc-editor.org/rfc/rfc8725.html) for algorithm verification, trusted issuer/key binding, audience rules, and separation of token purposes. Decoding claims is not validation. | Token-purpose and trust map, required claims, issuer/key authority, acceptance state, and downstream object-permission checks |

Upstream role and contract sources were reviewed on 2026-09-09. RFC 8725 is an
external standards reference supporting this workflow, not a claimed README
entry. Network-library names or generated descriptions do not prove which
implementation or service a game actually uses. Do not generalize upstream
latency comparisons into performance guarantees for a different workload.

## Follow One Operation

Identify delivery, connection identity, authenticated account, action permission,
authoritative simulation, and durable transaction as separate stages. Read only
the selected resource's contract and the application's relevant integration.
Then connect an existing trace or owned-source path to the stage under review.

An unauthorized-object objective requires a missing or incorrect permission
boundary; encryption or reliable delivery does not resolve it. Duplicate economy
effects require an application transaction failure, not merely a retransmission.
Review bounds, validation ownership, logical-operation identity, and reconciliation.
Loss, reconnects, callback delays, and clock-domain differences are ordinary
alternative explanations for abnormal-looking traces.

Return the exact component/service versions, an operation map, transport and
application invariants, available evidence, and remaining uncertainty. Use
[time and replay evidence](time-ordering-and-replay.md) for order and prediction,
and the [parent skill](../SKILL.md) for provider-specific authentication,
inventory, and purchase contracts.
