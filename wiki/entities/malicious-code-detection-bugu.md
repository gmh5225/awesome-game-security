---
title: Malicious Code Detection Bugu
kind: entity
topics: [anti-cheat, reverse-engineering]
sources:
  - wiki/sources/descriptions/gmh5225__Malicious-code-detection-bugu.md
updated: 2026-08-11
confidence: medium
---

# Malicious Code Detection Bugu

Go-based **Bugu** malicious-code detection platform built as gRPC microservices. Accepts file uploads, performs hash verification, and runs automated malware analysis through a Protobuf-defined API exposing both gRPC and HTTP endpoints for malware scanning. (source: wiki/sources/descriptions/gmh5225__Malicious-code-detection-bugu.md)

Sits in the **defensive sample-analysis** lane beside static obfuscation pinpointing such as [[obfuscation-detection]] and live in-memory scanners such as [[xmalhunter]]: a service-oriented pipeline for batch file/hash screening rather than in-process hook or CFF heuristics. Useful for AC researchers building malware or cheat-sample triage backends and for studying obfuscated-binary detection workflows under [[overviews/anti-cheat]].

## Links

- Repo: https://github.com/gmh5225/Malicious-code-detection-bugu

## Related

[[overviews/anti-cheat]] · [[overviews/reverse-engineering]] · [[obfuscation-detection]] · [[xmalhunter]] · [[android-unpacker]] · [[mal-unpack-drv]] · [[findyara-ida]]
