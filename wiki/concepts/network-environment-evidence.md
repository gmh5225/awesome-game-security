---
title: Network Environment Evidence
kind: concept
topics: [anti-cheat]
sources:
  - wiki/sources/skills/anti-cheat.md
updated: 2026-09-09
confidence: medium
---

# Network Environment Evidence

Evidence about **shared networks**, account/device association, reported connection restrictions, or claimed sanction duration. Keep **connection failure**, **rate limiting**, **detection**, and **enforcement** as separate events—a common address, acquisition driver, or unusual input device needs context and corroboration before attribution. (source: wiki/sources/skills/anti-cheat.md)

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

## Analysis discipline

- Record collector coverage limits explicitly.
- Test benign explanations (NAT, VPN, family/household, café networks, cloud gaming).
- Cross-reference with causally distinct layers ([[hardware-input-injection]], process memory, replay telemetry) before enforcement.

## Related

[[hardware-input-injection]] · [[detector-operations]] · [[research-rigor]] · [[overviews/anti-cheat]] · [[overviews/dma-attack]]
