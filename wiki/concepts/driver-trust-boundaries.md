---
title: Driver Trust Boundaries
kind: concept
topics: [windows-kernel, anti-cheat, game-hacking]
sources:
  - wiki/sources/skills/windows-kernel.md
  - wiki/sources/skills/anti-cheat.md
updated: 2026-09-09
confidence: high
---

# Driver Trust Boundaries

Windows kernel driver interfaces, authorization, and provenance framing for game-security research. Signed code can still expose unsafe IOCTL paths; reachability and defensive value require evidence for the specific build and configuration — not the driver name alone. (source: wiki/sources/skills/windows-kernel.md)

## Threat-model synthesis

| Threat class | Necessary capability or boundary | Evidence and defensive focus |
|---|---|---|
| Dangerous privileged interface | Caller can reach sensitive driver operations | Device ACLs, per-operation authorization, constrained functionality |
| Vulnerable signed-driver abuse | Affected driver is loaded or loadable and its interface reachable | Exact hash/version, provenance, loaded inventory, applicable policy |
| Driver-mediated acquisition | Host kernel acquisition component and usable interface | Driver/service identity, acquisition process, interface access, timeline |
| Kernel code/data tampering | Ability to modify affected protected state | Trusted comparison evidence, ownership, protection and integrity events |

The table is a synthesis lane; actual reachability requires build/configuration evidence. Review buffer lengths, output initialization, object lifetime, cancellation, and **IRQL** alongside caller authorization. (source: wiki/sources/skills/windows-kernel.md)

## Three evidence layers

1. **Documented contracts** — public WDK APIs, IOCTL contracts, Microsoft driver security checklists.
2. **Observed host state** — loaded-module inventory, blocklist/policy version, HVCI/VBS running state, ETW/callback telemetry.
3. **Inferred internals** — undocumented structure layouts, allocator routing, internal table walks — treat as **build-specific hypotheses** until verified with symbols and runtime for the exact Windows build; pair with [[research-rigor]].

## Policy and mitigation scope

- **VBS/[[hvci]]:** distinguish capability, configuration, and running state; compatibility lists do not prove every interface is safe under Memory Integrity.
- **Driver blocklists:** incomplete coverage — record whether policy blocks disk write, load, or both, and the active rules version ([[msft-driverblocklist]], [[code-integrity-driverblocklist]]).
- **[[byovd]]:** establish affected driver presence, reachable interface, and required privilege before attributing hostile kernel activity.
- **Acquisition paths:** USB/network-relayed memory capture shares artifacts with legitimate IR — classify initiator vs transport via [[memory-acquisition-path]].

## Related

[[byovd]] · [[hvci]] · [[patchguard]] · [[kernel-callbacks]] · [[kernel-pool-scanning]] · [[etw-threat-intelligence]] · [[driver-communication]] · [[research-rigor]] · [[overviews/windows-kernel]] · [[overviews/anti-cheat]]
