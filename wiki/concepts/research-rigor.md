---
title: Research Rigor
kind: concept
topics: [overview]
sources:
  - wiki/sources/skills/overview.md
  - wiki/sources/skills/game-engine.md
  - wiki/sources/skills/mobile-security.md
  - wiki/sources/skills/reverse-engineering.md
  - wiki/sources/descriptions/xihedun-2026__Ponytail-Risk-.md
  - wiki/sources/descriptions/thatskriptkid__re-harness.md
updated: 2026-08-10
confidence: high
---

# Research Rigor

Cross-cutting evidence discipline for factual synthesis, detector assessment, and consequential security claims in the awesome-game-security corpus. Pair the matching domain skill (e.g. [[overviews/anti-cheat]], [[overviews/dma-attack]]) with research-rigor when converting README listings, wiki prose, or archive snippets into actionable conclusions. (source: wiki/sources/skills/overview.md)

## Principles

- Treat README entries, generated descriptions, [[compiled-wiki]] pages, and archives as **discovery/provenance** layers—not automatic proof of embedded claims.
- Verify citation identity: confirm the source text supports the exact claim being stated.
- Separate **observation**, **finding**, **attribution**, and **action** in written output.
- Separate **automated scoring** from **enforcement action** when evaluating operator AC stacks—platforms such as [[ponytail-risk]] default to shadow mode so rule/AI signals feed human review rather than immediate bans. (source: wiki/sources/descriptions/xihedun-2026__Ponytail-Risk-.md)
- Do not import fixed detection thresholds or confidence values without representative calibration and validation for the target environment.
- Narrow the conclusion or report it as inconclusive when evidence is missing or contradictory.

## When to apply

| Query type | Pair with |
|------------|-----------|
| Claim validation, citation checks | matching domain overview |
| Detector evaluation, false-positive rates | [[overviews/anti-cheat]] or relevant detection lane |
| Engine globals, offsets, SDK dumps | [[overviews/game-engine]] + [[unreal-object-model]] / [[il2cpp]] / [[source-netvars]] |
| Mobile root/hook/emulator/integrity claims | [[overviews/mobile-security]] + [[mobile-anti-cheat]] |
| RE tool stealth/coverage, deobfuscation claims | [[overviews/reverse-engineering]] + [[dynamic-binary-instrumentation]] / [[mixed-boolean-arithmetic]] |
| Evidence conflicts across sources | domain skill + this page |

Engine globals, object layouts, metadata formats, and helper APIs vary by engine branch, build configuration, platform, and game modifications—verify the exact version and binary artifacts before generalizing signatures or offsets. (source: wiki/sources/skills/game-engine.md)

Mobile root visibility, hook detection, emulator heuristics, and attestation outcomes vary by Android/iOS version, OEM policy, GKI kernel, signing, and entitlement state—verify device/build before generalizing detector or bypass conclusions. (source: wiki/sources/skills/mobile-security.md)

DBI coverage, trap-and-emulate latency, deobfuscation completeness, and anti-debug bypass effectiveness vary by binary build, Windows version, integrity checks, and timing defenses—record hash, tool version, and measured evidence before generalizing stealth or recovery claims. (source: wiki/sources/skills/reverse-engineering.md)

LLM-assisted static RE should ground conclusions in disassembler/decompiler evidence (pseudocode, xrefs, FLIRT IDs) from tool APIs rather than model speculation—read-only agent harnesses such as [[re-harness]] enforce IDA/IDASQL-backed workflows for auditable outputs. (source: wiki/sources/descriptions/thatskriptkid__re-harness.md)

## Related

[[compiled-wiki]] · [[mobile-anti-cheat]] · [[overviews/overview]] · [[overviews/mobile-security]] · [[AGENTS]]
