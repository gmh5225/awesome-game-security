---
name: game-server-security
description: Review multiplayer authority and game backend trust across gameplay RPCs, authentication, object authorization, inventory, virtual economy, purchases, and asynchronous events. Use for client/server boundaries, session verification, entitlement validation, transaction consistency, duplicate delivery, and network failure handling. Produce operation maps, supported invariants, defensive checks, and evidence-based findings; distinguish client intent, verified identity, permission, and committed state.
---

# Game Server and Backend Security

Use this skill for architecture and owned-source review of consequential game
operations. Treat client, listen server, dedicated server, backend, store, and
administrative tools as separate authorities. For connection restrictions and
ban-duration reports, use [network evidence](../anti-cheat/references/network-environment-evidence.md).

## Map One Consequential Operation

Record the initiating principal, authenticated identity, object owner,
requested action, authoritative validator, allowed preconditions, state change,
persistence boundary, external dependencies, and observable result. Follow the
specific operation through the system before generalizing to all endpoints.

Separate client intent, prediction, authoritative simulation, replicated
visibility, and durable account state. Server execution does not establish
correct validation, and a player-controlled host has a different trust model
from an operator-controlled server.
[Epic networking overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine)

## Attack Objectives and Failed Boundaries

| Objective | Required capability or failed boundary | Defensive review |
|---|---|---|
| Read or alter another player's objects | Reachable operation lacks object/account authorization | Principal-to-object permission for each consequential operation |
| Influence rewards with client assertions | A service accepts data outside the client's authority | Reward provenance, authoritative rules, allowed transitions |
| Produce duplicate or inconsistent economy effects | Duplicate/concurrent processing escapes defined transaction semantics | Logical-operation identity, state versions, atomicity and reconciliation |
| Receive unearned or misassigned purchase benefits | Unverified or mismatched purchase evidence is trusted | Provider verification, purchase state, intended-account association |
| Act through an unverified or obsolete session | Pending validation, expiry, or revocation is mishandled | Explicit session states and permitted capabilities |
| Exhaust service resources | Expensive work or queues have inadequate bounds | Per-operation budgets, bounded work, congestion-aware retry handling |

This is a conceptual threat model. A possibility in the table does not establish
an exploitable defect in a particular service.

## Authentication Is One Input to Authorization

Distinguish pending, validated, invalid, expired, and revoked session states.
An initial ticket/API result may precede the provider's authoritative verification
callback. Identity and game ownership are distinct conditions; a particular
ticket flow may validate both together. Follow that flow's documented contract.
[Steamworks authentication and ownership](https://partner.steamgames.com/doc/features/auth?l=english)

Independently verify permission for the action, account, target object, title or
tenant, and workflow state. Include account linking, support/admin tools, and
service credentials in the operation map. Client-side UI restrictions or opaque
object identifiers do not replace authorization at the responsible service.
[OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

## Economy, Inventory, and Purchase State

Define intended grant, spend, transfer, consume, mint, burn, refund, and
administrative adjustment paths before asserting conservation or nonnegative
balances. Document transaction boundaries, concurrent changes, partial external
failures, reconciliation ownership, and audit evidence.

Distinguish retry deduplication from stale-write rejection. PlayFab Economy v2
documents different contracts for `IdempotencyId` and ETags, and advises against
combining them in the same request because of conflicting retry semantics.
Check the chosen API and version instead of recommending one universal pattern.
[Idempotent transactions](https://learn.microsoft.com/en-us/xbox/playfab/economy-monetization/economy-v2/tutorials/idempotent-transactions-and-retries),
[ETags and concurrency](https://learn.microsoft.com/en-us/xbox/playfab/economy-monetization/economy-v2/tutorials/etags-and-concurrency-control)

Model purchase UI results, provider verification, eligible ownership, entitlement
grant, acknowledgement/consumption, renewal, refund, and revocation separately.
Bind verified purchase evidence to its intended game account and durable grant
record. For Google Play, a pending purchase does not authorize an entitlement
grant; follow documented purchase-state and backend-verification requirements.
[Google Play billing security](https://developer.android.com/google/play/billing/security)

## Network Failure Is Part of the State Model

Model loss, duplication, reordering, delayed messages, disconnects, reconnects,
and uncertain responses. A timeout does not establish that a write failed.
Separate repeat delivery of one logical operation from a new operation, a stale
write, and a repeated notification; record deduplication scope and lifetime.

UDP supplies neither delivery/ordering guarantees nor communication security.
Review application requirements and established transport-security mechanisms;
retries still need congestion-aware behavior. Packet irregularity alone is not
evidence of malicious intent.
[RFC 8085](https://www.rfc-editor.org/rfc/rfc8085.html)

## Review Output and Verification

Produce an operation map, authoritative-state inventory, invariant ledger,
available evidence, and unresolved questions. Use existing logs, owned-source
review, internal fixtures, and documented provider sandbox events for legitimate
retries, concurrent updates, pending authentication, and entitlement transitions.
Record expected and observed durable effects, including partial failure.

Keep correctness findings separate from cheating attribution. Use
[research-rigor](../research-rigor/SKILL.md) for evidence strength,
[game-engine](../game-engine/SKILL.md) for replication details, and
[game-supply-chain-security](../game-supply-chain-security/SKILL.md) for deployment authority.

Primary sources reviewed: 2026-09-09. Provider examples are version-specific
contracts, not universal guarantees for every backend.
