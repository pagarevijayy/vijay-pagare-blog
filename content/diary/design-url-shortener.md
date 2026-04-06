+++
title = "Design: URL Shortener"
date = "2026-04-06T16:27:00+05:30"
slug = "design-url-shortener"
description = "Deep dive into Base62, KGS, and Quorum consistency for a global URL shortening service."
featured_image = "images/url-shortener-banner.png"
tags = ["systemDesign", "study"]
+++

Started learning system design and architecture seriously. I'll be posting daily notes on whatever i learn about the subject going forward. Here's the first one–enjoy!

### 1. The Core: Base62 Encoding
To keep URLs short, we use **Base62 encoding** (`[a-z, A-Z, 0-9]`). 
* A 7-character string gives us **3.5 Trillion combinations**.
* **Why not Base64?** Base64 includes `+` and `/`, which are not URL-safe and can break paths.

### 2. The Coordination Problem: Key Generation Service (KGS)
In a distributed system, we must prevent "collisions" where two servers generate the same ID.
* **The "Bucket" Strategy:** We use **Apache ZooKeeper** to hand out "ranges" of IDs (e.g., Server A gets 1-1000).
* **RAM over Disk:** These IDs are kept in memory. Even if a server crashes and we lose a few IDs, it’s a "safe waste" that allows the system to remain lightning fast.

### 3. High Availability vs. Consistency (CAP Theorem)
* **Read-Heavy Ratio:** 100:1 (Read:Write).
* **The Fix:** NoSQL (Cassandra/DynamoDB) for scaling and **Redis** for caching "Hot URLs."
* **Quorum Math ($W+R>N$):** We ensure consistency by writing to a majority and reading from a majority.

### Thoughts on replicas and waste of resources
In System Design, we often **intentionally waste resources** (like losing a few IDs during a crash) if it removes a bottleneck and makes the entire global system 100x faster.
