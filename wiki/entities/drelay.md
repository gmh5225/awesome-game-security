---
title: drelay
kind: entity
topics: [game-hacking, reverse-engineering]
sources:
  - wiki/sources/descriptions/is-fo__drelay.md
updated: 2026-10-16
confidence: medium
---

# drelay

Research toolkit for **Darza's Dominion** that combines wire-level session control with in-process client instrumentation—aimed at reverse engineers and game-security researchers who need live protocol visibility and documented analysis of latency-sensitive in-frame decisions without shipping a modified game install. (source: wiki/sources/descriptions/is-fo__drelay.md)

## Components

**Java TCP relay** — Local proxy binds the game's server addresses on loopback, decodes and logs traffic from reverse-engineered structures, optionally rewrites packets, then forwards to the real server. Ships as a self-updating JAR with operator scripts and protocol documentation.

**In-process hook** — C++ and .NET injection before `Main` detours targets identified by SHA-256 hashes of their IL bytes. Bundles MinHook, a managed bootstrap with dodge/escape solvers, and build-gated verification against a pinned game fingerprint (refuses mismatched client builds).

## Stack

Java (relay/proxy), C++ and C# on Windows (MSVC, .NET SDK), PowerShell build and offline test harnesses.

## Links

- Repo: https://github.com/is-fo/drelay (README: Darza's Dominion Java TCP relay and in-process hook for intercepting, decoding, logging, and modifying client–server packets)

## Related

[[overviews/game-hacking]] · [[overviews/reverse-engineering]] · [[il2cpp]]
