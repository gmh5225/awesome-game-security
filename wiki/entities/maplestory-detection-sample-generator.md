---
title: MapleStory Detection Sample Generator
kind: entity
topics: [game-hacking, anti-cheat]
sources:
  - wiki/sources/descriptions/gmh5225__MapleStoryDetectionSampleGenerator.md
updated: 2026-08-11
confidence: medium
---

# MapleStory Detection Sample Generator

Sample generator for MapleStory cheat-detection testing and anti-cheat development. Creates synthetic detection samples that simulate common MapleStory hacking patterns for training and validating anti-cheat detection algorithms, and exports machine-learning object-detection samples from MapleStory in multiple formats. (source: wiki/sources/descriptions/gmh5225__MapleStoryDetectionSampleGenerator.md)

Sits on the **defensive dataset** side of the MapleStory computer-vision stack: complements offensive YOLO training such as [[maplestory-yolov8-training]] and runtime automation such as [[maplestory-worlds-automation]] by supplying labeled or synthetic samples for detector evaluation rather than live cheat execution. Useful for AC engineers building or benchmarking MapleStory-specific object-detection rules and ML classifiers under [[ai-aimbot-detection]].

## Links

- Repo: https://github.com/gmh5225/MapleStoryDetectionSampleGenerator

## Related

[[overviews/game-hacking]] · [[overviews/anti-cheat]] · [[maplestory-yolov8-training]] · [[maplestory-worlds-automation]] · [[ai-aimbot-detection]] · [[waldo]] · [[aimbot-detection-prototype]]
