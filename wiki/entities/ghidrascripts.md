---
title: GhidraScripts
kind: entity
topics: [reverse-engineering, game-hacking]
sources:
  - wiki/sources/descriptions/advanced-threat-research__GhidraScripts.md
updated: 2026-08-19
confidence: medium
---

# GhidraScripts

Maintained collection of Ghidra scripts for extending and automating static analysis workflows inside Ghidra. Primarily Java-based; includes AI-assisted renaming, complexity visualization, Golang support, BSim-based matching, and FunctionID database generation. Integrates external analysis resources such as SHAREM and Malpedia to enrich reverse-engineering context—aimed at malware analysts and reverse engineers who need scalable static analysis automation, including game-security investigations. (source: wiki/sources/descriptions/advanced-threat-research__GhidraScripts.md)

Distinct from the CTF-oriented [[ghidra-scripts]] collection (`ghidragolf/ghidra_scripts`); this repo is a broader maintained automation toolkit from advanced-threat-research. Peers include complexity metrics [[ghidrametrics]], BSim diffing [[ghidriff]], and in-Ghidra LLM assistants [[ghidrassist]] / [[ghidra-openai]]—verify AI-assisted renames against disassembly per [[research-rigor]].

## Links

- Repo: https://github.com/advanced-threat-research/GhidraScripts

## Related

[[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[ghidra]] · [[ghidra-scripts]] · [[ghidrametrics]] · [[ghidriff]] · [[ghidrassist]] · [[research-rigor]]
