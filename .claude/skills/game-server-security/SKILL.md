---
name: game-server-security
description: Review multiplayer authority and backend trust across RPCs, sessions, object authorization, inventory, economy, and purchases. Use when choosing or assessing KCP, GameNetworkingSockets, Steam networking interfaces, server frameworks, or token-validation resources; distinguish delivery reliability, transport identity, game permission, and durable state. Cover retries, provider contracts, clock domains, replication order, prediction, and replay, producing operation maps and evidence-based invariants.
---

# Game Server and Backend Security

Use this skill for architecture and owned-source review of consequential game
operations. Treat client, listen server, dedicated server, backend, store, and
administrative tools as separate authorities. For connection restrictions and
ban-duration reports, use [network evidence](../anti-cheat/references/network-environment-evidence.md).

When matching repository resources to a network or backend layer, read the
[server resource guide](references/repository-resources.md). It locates the
actual README categories and separates protocol, platform service, framework,
and token-validation responsibilities.

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

For timing anomalies, replication order, prediction/correction, resimulation
or replay evidence, read [time, ordering and replay](references/time-ordering-and-replay.md).
Determine the observation timeline and ordering scope before asserting an invariant.

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

## Data Source

Use the following repository sources directly when applying this skill. Prefer
available local files for discovery and scoped historical inspection; use the
raw URLs when the collection is not installed locally. These entrypoint details
are retained here so source lookup does not depend on loading another skill.

### 0. Compiled Wiki

Start with [wiki/index.md](../../../wiki/index.md) for topical synthesis and
cross-project connections. [Wiki schema](../../../wiki/AGENTS.md) describes its
structure. Generated wiki pages are discovery aids; follow their original
citations before adopting technical claims.

Raw catalog: [wiki/index.md](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/wiki/index.md).
This skill does not currently have a matching wiki overview. Use its local
references and the wiki catalog to find related pages; do not invent a path.

A direct project question can start with its README entry or description below;
reading the entire wiki is unnecessary.

### 1. Project Overview and Resource Index

[README.md](../../../README.md) contains the collection's actual categories,
subcategories, project URLs and short descriptions. Find the relevant category
and retain the original URL, including any specific file or revision suffix.

Raw index: [README.md](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/README.md).

### 2. Repository Descriptions

For a concise project summary, look for the actual local path:

```text
description/{owner}/{repo}/description_en.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/{owner}/{repo}/description_en.txt
```

Example: [bgfx description](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/description/bkaradzic/bgfx/description_en.txt).
Extract owner/repository from the original GitHub project URL, omitting a .git
suffix. Resolve existing path casing before constructing a local/raw path.
Descriptions are generated summaries, not independent verification. If absent
or inaccessible, use the README entry, relevant archive or original project.

### 3. Repository Source Archives

For deeper inspection of an available captured source tree, locate:

```text
archive/{owner}/{repo}.txt
https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/{owner}/{repo}.txt
```

Example: [bgfx archive](https://raw.githubusercontent.com/gmh5225/awesome-game-security/refs/heads/main/archive/bkaradzic/bgfx.txt).
Prefer inspecting the relevant portion of an existing archive over re-cloning
merely to inspect the same captured material. Archives may exclude files, use
fallback extraction or contain truncation; they are not guaranteed complete
checkouts. Record any upstream revision evidence and included-file limits.
If missing or insufficient, follow the README's original upstream URL.

### Choose and Verify the Source

For a specific project, locate its README identity, use a description or wiki
page for orientation when helpful, then inspect the relevant archive/source
artifact for the question. For current compatibility or exact implementation,
verify the matching upstream documentation, release or immutable source revision.
Keep the collection revision and capture/generation dates separate from the
upstream version. Multiple generated layers from one source are not independent
corroboration, and missing archive content does not establish upstream absence.

The per-domain resource guide above helps choose useful artifacts. Shared
[repository navigation](../overview/references/repository-navigation.md) adds the optional read-only indexer,
case-ambiguity handling and maintenance details; it supplements this Data Source
section rather than replacing it.
