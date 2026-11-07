---
title: VMProtect-LLM-SKILL
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/7777lolonlyyou__VMProtect-LLM-SKILL.md
updated: 2026-11-07
confidence: medium
---

# VMProtect-LLM-SKILL

[7777lolonlyyou/VMProtect-LLM-SKILL](https://github.com/7777lolonlyyou/VMProtect-LLM-SKILL) is a **Markdown agent skill and workflow guide** for **static and dynamic devirtualization** of binaries protected by **VMProtect**, **Themida**, and similar **custom virtual-machine obfuscators**. The focus is **recovering original program semantics** rather than reimplementing the VM protector itself. (source: wiki/sources/descriptions/7777lolonlyyou__VMProtect-LLM-SKILL.md)

## Workflow stack

| Component | Role |
|-----------|------|
| **Miasm** | Primary engine: PE loading, controlled execution, IR lifting, expression analysis |
| **Capstone / Triton / Z3 / IDA** | Auxiliary disassembly, symbolic execution, constraints, and interactive RE |
| **Debuggers** | Dynamic anchoring when static paths disagree with runtime behavior |

Documented stages include locating virtualized regions, anchoring VM context and virtual registers, classifying handlers, **taint and backward slicing**, optional **shadow IR**, symbolic path constraints, **byte-provenance tracking for VMProtect 3.9**, and validation of recovered pseudocode. Dedicated guidance covers how language models should **choose tools**, separate **hypotheses from confirmed facts**, and narrow analysis when results conflict with live execution. (source: wiki/sources/descriptions/7777lolonlyyou__VMProtect-LLM-SKILL.md)

## Audience

Reverse engineers and game or software-protection researchers who need a **repeatable, tool-grounded** approach to unpacking commercial VM-based packers and anti-tamper schemes with LLM-assisted analysis. (source: wiki/sources/descriptions/7777lolonlyyou__VMProtect-LLM-SKILL.md)

## Positioning

Listed under Cheat **Fix VMP** as a **skill/doc workflow** beside automated devirtualizers ([[novmp]], [[vmplift]], [[vmp-devirt]], [[titan]]) and aggregated agent hubs such as [[mcp-reverse]] (VMProtect cookbooks). Complements Themida-oriented tooling ([[themida-unmutate]], [[unthemidator]]) for mixed-protection targets.

## Links

- Repo: https://github.com/7777lolonlyyou/VMProtect-LLM-SKILL

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[vmprotect]] · [[vmp-devirt]] · [[vmplift]] · [[novmp]] · [[titan]] · [[triton]] · [[mcp-reverse]] · [[research-rigor]]
