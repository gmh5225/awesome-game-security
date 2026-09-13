---
title: Network Environment Evidence
kind: concept
topics: [anti-cheat]
sources:
  - wiki/sources/skills/anti-cheat.md
  - wiki/sources/descriptions/aryribeiro__cobra.md
updated: 2026-09-13
confidence: medium
---

# Network Environment Evidence

Evidence about **shared networks**, account/device association, reported connection restrictions, or claimed sanction duration. Keep **connection failure**, **rate limiting**, **detection**, and **enforcement** as separate events—a common address, acquisition driver, or unusual input device needs context and corroboration before attribution. (source: wiki/sources/skills/anti-cheat.md)

## Outcome vs decision key

| Observed outcome | Possible decision unit | Does not establish |
|------------------|------------------------|--------------------|
| Authentication or connection failure | Request, session, route, or service | A sanction was imposed |
| Rate limit (HTTP 429 + optional `Retry-After`) | Service-defined request/user grouping | Every account at an address was banned |
| Explicit account sanction | Named account and documented scope | A hardware or network restriction |
| Explicit device restriction | Provider-defined device association | Which properties define that association |
| Several devices lose access | Shared dependency or correlated condition | Common person, trigger, or enforcement mechanism |

Neither retry delay nor error code alone establishes a game sanction. (source: wiki/sources/skills/anti-cheat.md)

Browser leaderboard backends such as [[cobra-snake]] apply **submission rate limits** on score POST endpoints separately from plausibility checks and HMAC session binding—throttled requests are a service-level control, not proof of account sanction. (source: wiki/sources/descriptions/aryribeiro__cobra.md)

## Event separation

| Event type | Examples | Not equivalent to |
|------------|----------|-------------------|
| Connection failure | Timeouts, TLS errors, blocked ports | Cheating detection |
| Rate limiting | Throttled API or game-server responses | Ban decision |
| Detection | Rule hit, risk score, anomaly flag | Actor intent proof |
| Enforcement | Restriction, kick, ban, device block | Network topology alone |

## Observable signals

- Shared LAN or public IP between accounts (association hint, not proof).
- KMBox Net–style **UDP traffic** on local network between a secondary device and injector hardware—requires a collector with visibility into relevant traffic; shared address alone does not reveal inter-device exchanges.
- Reported network restrictions or claimed sanction duration from operator telemetry—verify against authoritative backend records.

## Identity boundaries

- **Account identity:** authenticated service identifier has its own scope; session association does not prove who physically operated a device.
- **Internet endpoint:** observed address/port is time-bounded; home NAT and carrier-grade NAT can place many unrelated subscribers behind one public IPv4.
- **Local network evidence:** router, switch, host, and server collectors see different traffic—sharing a LAN or public IP does not expose every inter-device exchange to a game server or local process.
- **IPv6 temporary addresses:** interface identifiers can change while prefix or authenticated session context may remain correlated; neither a full address nor a prefix is a universal device/person ID.

Address-based penalties can affect unrelated users behind shared addresses—document collateral-effect risk, not assumed provider policy. (source: wiki/sources/skills/anti-cheat.md)

## Analysis discipline

- Record collector coverage limits explicitly.
- Test benign explanations (NAT, VPN, family/household, café networks, cloud gaming).
- Cross-reference with causally distinct layers ([[hardware-input-injection]], process memory, replay telemetry) before enforcement.

## Related

[[hardware-input-injection]] · [[detector-operations]] · [[research-rigor]] · [[overviews/anti-cheat]] · [[overviews/dma-attack]]
