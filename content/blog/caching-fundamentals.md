+++
date = '2026-04-17T21:05:00+05:30'
title = 'Caching: Types, Patterns, and Trade-offs'
description = 'A practical guide to caching: types, architectures, eviction policies, common pitfalls, and when to use it in real systems.'
tags = ["systemDesign", "engineering", "performance"]
+++
---

## What is Caching?

Caching is the practice of storing data in temporary storage to enable faster access.

At a systems level, the speed difference is massive:
- Hard disk access: ~1 ms  
- Memory (RAM) access: ~100 ns  

That’s roughly **10,000x faster**.

The entire idea of caching is to avoid expensive operations (disk, DB, network, computation) by serving precomputed or previously fetched data.

---

## Types of Caching

### 1. External Cache  
A separate system acting as a shared cache layer.

- Examples: Redis, Memcached  
- Shared across multiple servers  
- Suitable for distributed systems  
- Involves network overhead  

Use this when you need **scalability and shared state across instances**.

---

### 2. In-Process Cache  
Cache stored within the application process itself.

- Extremely fast (no network calls)  
- Limited by server memory  
- Not shared across instances  

Best for **micro-optimizations and ultra-low latency use cases**.

---

### 3. CDN (Content Delivery Network)  
Optimizes delivery by serving content from geographically closest servers.

- Reduces latency due to network distance  
- Ideal for static/media assets  
- Offloads traffic from core backend  

Commonly used for:
- Images  
- Videos  
- Static files  

---

### 4. Client-Side Cache  
Caching at the browser level.

- LocalStorage / SessionStorage  
- Browser disk caching  
- Least controllable  

Useful for:
- Reducing repeated API calls  
- Improving perceived performance  

---

## Cache Architectures

### 1. Cache-Aside (Lazy Loading)  
- App checks cache first  
- If miss → fetch from DB → update cache  

**Pros:** Simple, widely used  
**Cons:** Cache inconsistency possible  

---

### 2. Write-Through  
- Write goes to cache and DB simultaneously  

**Pros:** Strong consistency  
**Cons:** Higher write latency  

---

### 3. Write-Behind (Write-Back)  
- Write goes to cache first  
- DB updated asynchronously  

**Pros:** Fast writes  
**Cons:** Risk of data loss if cache fails  

---

### 4. Read-Through  
- Cache layer itself fetches from DB on miss  

**Pros:** Cleaner abstraction  
**Cons:** Less control at application level  

---

## Eviction Policies

When cache is full, something must be removed.

### 1. LRU (Least Recently Used)  
Removes items not used recently.

### 2. LFU (Least Frequently Used)  
Removes items with lowest access frequency.

### 3. FIFO (First In First Out)  
Removes oldest entries.

### 4. TTL (Time To Live)  
Entries expire after a fixed time.

Choosing the right policy depends on **access patterns and data lifecycle**.

---

## Common Issues & Deep Dives

### 1. Cache Stampede (Thundering Herd)  
When many requests hit a missing/expired cache simultaneously, all fall back to DB.

**Mitigation:**
- Request coalescing  
- Locking  
- Staggered TTLs  

---

### 2. Cache Consistency  
Cache may serve stale data.

**Tradeoff:**  
- Strong consistency → more complexity  
- Eventual consistency → simpler but stale reads possible  

---

### 3. Hot Keys  
Some keys get disproportionately high traffic.

**Problems:**
- Uneven load  
- Cache node bottlenecks  

**Solutions:**
- Replication  
- Sharding  
- Local caching layer  

---

## NFRs: When Should You Use Caching?

Caching is most beneficial when:

- Read-heavy workloads  
- Expensive queries (joins, aggregations)  
- High database CPU usage  
- Strict latency requirements  

If your system is **write-heavy or requires strict consistency**, caching needs careful consideration.

---

## How to Introduce Caching (Practical Approach)

1. **Identify bottlenecks**  
   - Slow endpoints  
   - High DB load  
   - Repeated queries  

2. **Decide what to cache**  
   - Query results  
   - Computed data  
   - API responses  

3. **Choose cache architecture**  
   - Cache-aside (most common starting point)  

4. **Set an eviction policy**  
   - Based on usage patterns  

5. **Address downsides**  
   - Stampede prevention  
   - Consistency strategy  
   - Monitoring  

---

## Final Thought

Caching is one of the highest leverage optimizations in system design.

But it’s not just about adding Redis.

It’s about:
- Understanding access patterns  
- Designing for consistency vs performance  
- Handling edge cases at scale  

Done right, caching can **transform system performance**. Done poorly, it can **introduce subtle, hard-to-debug issues**.
