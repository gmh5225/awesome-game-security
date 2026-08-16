---
title: Paho MQTT C++
kind: entity
topics: [game-engine, overview]
sources:
  - wiki/sources/descriptions/eclipse__paho.mqtt.cpp.md
updated: 2026-08-16
confidence: medium
---

# Paho MQTT C++

Eclipse Paho MQTT C++ client library with a modern C++ API for MQTT pub/sub messaging. Supports MQTT v3.1, v3.1.1, and v5.0 with QoS 0–2, persistent sessions, TLS encryption, automatic reconnection, and asynchronous delivery. Wraps the Paho C client with RAII-style resource management and callback-based event handling. (source: wiki/sources/descriptions/eclipse__paho.mqtt.cpp.md)

Sits under README `Game Network` / `[mqtt cpp]` as a native C++ client for broker-based game telemetry, IoT-adjacent backends, and embedded systems stacks—complementing [[mqtt-js]] (Node.js/browser) and the [[mqtt]] spec reference when auditing pub/sub channels in C++ server or tooling code rather than as cheat tooling.

## Links

- Repo: https://github.com/eclipse/paho.mqtt.cpp

## Related

[[overviews/game-engine]] · [[overviews/overview]] · [[mqtt]] · [[mqtt-js]] · [[socket-io]] · [[uwebsockets]] · [[kcp]] · [[pitaya]]
