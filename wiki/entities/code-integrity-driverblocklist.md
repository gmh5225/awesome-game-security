---
title: Code Integrity DriverBlocklist
kind: entity
topics: [windows-kernel, anti-cheat]
sources:
  - wiki/sources/descriptions/Harvester57__CodeIntegrity-DriverBlocklist.md
updated: 2026-08-24
confidence: medium
---

# Code Integrity DriverBlocklist

Data repository of **Windows Code Integrity** policy blocklists for vulnerable or abuse-prone kernel drivers. Ships large XML policy files with deny rules keyed on hashes and driver identities, including anti-cheat-relevant kernel modules. Content is configuration data—not executable source—intended for consumption by **WDAC** or related CI policy tooling. Primary use case is defensive hardening, kernel attack-surface reduction, and anti-cheat environment protection. (source: wiki/sources/descriptions/Harvester57__CodeIntegrity-DriverBlocklist.md)

Complements Microsoft's Recommended Driver Block Rules reference [[msft-driverblocklist]] and WDAC authoring tooling such as [[wdactools]] in the same trust pipeline [[hvci]] enforces at runtime.

## Links

- Repo: https://github.com/Harvester57/CodeIntegrity-DriverBlocklist

## Related

[[msft-driverblocklist]] · [[wdactools]] · [[solemn]] · [[driver-risk-scout]] · [[loldrivers]] · [[byovd]] · [[hvci]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
