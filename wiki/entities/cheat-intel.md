---
title: cheat-intel
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/NetVar1337__cheat-intel.md
updated: 2026-11-18
confidence: medium
---

# cheat-intel

**cheat-intel** (NetVar1337/cheat-intel) is an open knowledge base and reporting practice for monitoring public cheat communities and turning what they reveal into actionable game-security intelligence. The repository centers on Markdown methodology, collector runbooks, and periodic landscape reports rather than shipping runtime software, though it prescribes structured record keeping such as dated JSONL or SQLite captures. (source: wiki/sources/descriptions/NetVar1337__cheat-intel.md)

## Methodology

- **Observation sources** — forums, listings, patch notes, and official anti-cheat communications.
- **Claim grading** — primary artefacts through corroboration levels before trends enter reports.
- **Intel-to-detection loop** — translate market tempo into concrete detection and process actions with confidence bounds and falsifiers.

## Scope

Coverage spans loaders, spoofers, DMA and peripheral cheats, subscription delivery, and account markets. Emphasis is on **lawful OSINT only** and attribution hygiene so enforcement and detection teams can pace cheat-market tempo without relying on rumor or unverified forum chatter. (source: wiki/sources/descriptions/NetVar1337__cheat-intel.md)

## Audience

Anti-cheat engineers, threat researchers, and enforcement teams building repeatable intelligence workflows rather than one-off forum reads.

## Positioning

Pairs methodology and landscape reporting with technical FPS research stacks such as [[apex-anticheat-lab]]—telemetry detectors and YARA/host surveys on one side, graded OSINT and trend templates on the other. Feed graded trends into [[detector-operations]] shadow/canary planning and [[research-rigor]] before wiring new rules to sanctions.

## Peers

[[apex-anticheat-lab]] · [[screenshare-signatures]] · [[detect-fps-hackers]] · [[blc-gamesec-lab]] · [[anticheat-detection]]

## Links

- Repo: https://github.com/NetVar1337/cheat-intel

## Related

[[overviews/anti-cheat]] · [[detector-operations]] · [[research-rigor]] · [[cheat-attack-surface]]