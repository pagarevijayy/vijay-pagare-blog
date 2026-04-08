+++
date = '2026-04-08T20:40:39+05:30'
draft = true
title = 'Design: Activity Feed'
featured_image = "images/ccc-banner.png"
tags= ["SystemDesign", "Engineering"]
+++


### The Problem
In an activity feed (like LinkedIn or Instagram), we need to track which posts a user has already seen. 
* **The Scale:** Millions of active users.
* **The Volume:** Every scroll generates a "Seen" event. This is a massive write-heavy workload.
* **The Goal:** Ensure we don't show the same post twice to the same user upon refresh.

### 1. The Storage Strategy (The Write Path)
If we use a traditional SQL database, every "seen" event requires the DB to find a specific row and update it. This involves "Random I/O," which is slow. At 100k+ events per second, a standard relational database will struggle with locking and disk contention.

**The Solution:** Use an **LSM-Tree based storage engine** (like Cassandra or ScyllaDB). 
In this model, "Seen" events are treated as "appends." They are written to a log in memory and eventually flushed to disk as sorted files. It’s significantly faster because the system doesn't "search" for anything during the write; it just adds the data to the end of the log.

### 2. The Efficiency Trick: Bloom Filters
When a user refreshes their feed, the system might fetch 50 candidate posts and must check: *"Has the user seen any of these?"*

Querying the database 50 times per refresh is too expensive. Instead, we use a **Bloom Filter**. 
* **What it is:** A space-efficient data structure that tells you if an item is "definitely not" in a set or "probably" in a set.
* **How it helps:** We can store a Bloom Filter in memory. If it says "No," we know the post is new. We only hit the actual database if the filter says "Maybe," drastically reducing our DB load.

### 3. The Architecture Flow
1.  **Ingestion:** User scrolls -> Event is sent to an **Asynchronous Queue** (like Kafka).
2.  **Processing:** A background worker picks up the event and writes it to the **LSM-Tree Database**.
3.  **Filtering:** When the feed is generated, the system checks the **Bloom Filter** to skip seen content instantly.

### Summary
When designing for high-volume status tracking, prioritize **Write Speed** by using append-only storage patterns and protect your **Read Latency** by using probabilistic data structures like Bloom Filters.
