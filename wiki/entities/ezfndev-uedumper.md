---
title: EZFNDEV UEDumper
kind: entity
topics: [game-engine, game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/EZFNDEV__UEDumper.md
updated: 2026-08-25
confidence: medium
---

# EZFNDEV UEDumper

**Unreal Engine SDK-style dumper** (EZFNDEV; C++). Generates SDK-style output from running UE-based games via an **injection-based workflow** with **automated offset finding**. Targets object name extraction, offset discovery, and header generation for Unreal reverse engineering and game-security research. The README notes **version limitations** and some **hardcoded or unstable** parts—validate output per title and engine branch before relying on generated headers. Listed under cheat / SDK Dump. (source: wiki/sources/descriptions/EZFNDEV__UEDumper.md)

Slug disambiguated from [[uedumper]] (Spuckwaffel; all-in-one ImGui dumper + live memory editor with the same repo name). Sits in the inject-based Unreal SDK-generation lane beside [[dumper-7]], [[shh0yauedumper]], [[ue4genny]], and [[re-ue4ss]]—all feeding the same [[unreal-object-model]] research surface.

## Links

- Repo: https://github.com/EZFNDEV/UEDumper

## Related

[[overviews/game-engine]] · [[overviews/reverse-engineering]] · [[overviews/game-hacking]] · [[unreal-object-model]] · [[uedumper]] · [[dumper-7]] · [[shh0yauedumper]] · [[ue4genny]] · [[re-ue4ss]] · [[unrealdumper-4-25]] · [[patternsleuth]]
