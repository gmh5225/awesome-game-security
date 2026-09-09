# Network Environment, Association, and Restriction Evidence

Primary-source review: 2026-09-09. This reference is vendor-neutral. The
standards below explain network evidence; they do not document a game's
private enforcement algorithm.

## Separate the Outcome from the Suspected Decision Key

| Observed or documented outcome | Possible decision unit | What it does not establish |
|---|---|---|
| Authentication or connection failure | Request, session, route, or service | A sanction was imposed |
| Rate limit | A service-defined request/user grouping | Every account at an address was banned |
| Explicit account sanction | The named account and documented scope | A hardware or network restriction |
| Explicit device restriction | The provider-defined device association | Which properties define that association |
| Several devices lose access | A shared dependency or correlated condition | A common person, trigger, or enforcement mechanism |

For HTTP-based endpoints, `429` denotes rate limiting and may carry a
`Retry-After` value. The standard does not fix how a service counts or identifies
users. Neither a retry delay nor an error code alone establishes a game sanction.
[RFC 6585, section 4](https://www.rfc-editor.org/rfc/rfc6585.html#section-4)

## Identity and Visibility Boundaries

- **Account identity:** an authenticated service identifier has its own scope;
  association with a session does not prove who physically operated a device.
- **Device evidence:** client-reported properties, locally verified state, and
  server-associated device records have different trust and availability.
- **Internet endpoint:** an observed address/port is a time-bounded connection
  fact. Home NAT and carrier-grade NAT can place many devices or unrelated
  subscribers behind one public IPv4 address.
- **Local network evidence:** router, switch, host, and server collectors see
  different traffic. Sharing a LAN or public IP does not expose every other
  device or inter-device exchange to a game server or local process.

Address-based penalties can affect unrelated users behind shared addresses.
This is a documented collateral-effect problem, not proof that any particular
game uses such a policy.
[RFC 6269, section 13.1](https://www.rfc-editor.org/rfc/rfc6269.html#section-13.1)

Where connection attribution is necessary, source address, source port,
transport protocol, accurate timestamp, and authorized provider mapping records
may matter. A public server's endpoint log does not automatically reveal the
subscriber, device, local MAC address, or person.
[RFC 6888, section 4](https://www.rfc-editor.org/rfc/rfc6888.html#section-4),
[RFC 6302, section 2](https://www.rfc-editor.org/rfc/rfc6302.html#section-2)

IPv6 temporary addresses can change the observed interface identifier; other
context, including a prefix or authenticated session, may remain correlated.
Neither a complete IPv6 address nor a prefix is a universal device/person ID.
[RFC 8981, section 8](https://www.rfc-editor.org/rfc/rfc8981.html#section-8)

## Review a Reported Incident

Use existing legitimate logs, provider notices, and authorized operator records.
Record the service/build/region, exact notice or error, issuer, UTC timestamps,
pseudonymous account/device references, endpoint family, and known affected
sessions. Separate user recollection from preserved evidence. Retain only
identifiers necessary for the investigation and protect raw logs.

Consider shared-address rate limits, service incidents, authentication faults,
stale sessions, and previously imposed account restrictions alongside network
enforcement. Distinguish an explicit sanction notice from an inferred cause.
Keep contrary observations, including unaffected sessions, where already
available; do not treat missing observations as success or failure.

Report observations rather than inventing a configured timer: failure at time
A and success at B establish those two outcomes. Only when they belong to the
same continuous restriction, without intermittent recovery or another failure
cause, can its removal be bounded between A and B. A next-day recovery does not
establish an exact 24-hour duration, its start event, or whether retries reset
anything.

## Evidence Standard for Network-Wide Claims

The following are separate claims requiring separate evidence:

1. A restriction exists, rather than an access failure.
2. It applies to an address/prefix or another network grouping.
3. It affects all devices or accounts in that grouping.
4. Its duration is exactly 24 hours, with a known start and reset rule.
5. It is a staged rollout or will become permanent.

The reviewed primary sources do not establish the combined claim that one
device's sanction causes every device on the network to receive an automatic
24-hour ban. Treat that report as an unverified hypothesis. Repeated symptoms
alone cannot reveal an undocumented backend key or future enforcement policy.
Route disputed restrictions through the provider's documented review process.

For reports, use four fields: **documented policy**, **observed outcome**,
**candidate explanations**, and **unknown mechanism/scope**. Use
[research-rigor](../../research-rigor/SKILL.md) when interpreting timing,
correlation, or false-positive evidence.
