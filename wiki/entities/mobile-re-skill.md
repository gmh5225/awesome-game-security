---
title: MobileRE-Skill
kind: entity
topics: [mobile-security, reverse-engineering]
sources:
  - wiki/sources/descriptions/index-login__MobileRE-Skill.md
updated: 2026-08-04
confidence: medium
---

# MobileRE-Skill

AI-driven skill set for mobile reverse engineering and security analysis, structured so LLM agents can map attack surfaces, choose techniques, and run repeatable analysis workflows instead of ad hoc scripting. Core deliverables are agent definitions and decision-tree skill documentation, backed by composable Frida JavaScript modules (passive monitoring and active bypass), Python tools for ARM64 binary analysis, and batch utilities for debugging and injection checks. (source: wiki/sources/descriptions/index-login__MobileRE-Skill.md)

The stack supports layered analysis from Java through JNI, native code, libc, syscalls, and inline SVC instructions, including a six-phase anti-detection pipeline covering root checks, Frida hiding, SO loading, and crash prevention. Integrates with [[jadx]] and Ghidra for decompilation. Aimed at authorized mobile app security testing, anti-tamper research, and reversing hardened Android applications.

Complements agent-facing Android RE MCP tools such as [[delamain]] and [[apktool-mcp-server]] — MobileRE-Skill is the Frida-centric, decision-tree skill layer for mobile dynamic analysis rather than static decompile MCP.

## Links

- Repo: https://github.com/index-login/MobileRE-Skill

## Related

[[overviews/mobile-security]] · [[overviews/reverse-engineering]] · [[frida]] · [[jadx]] · [[delamain]] · [[apktool-mcp-server]]
