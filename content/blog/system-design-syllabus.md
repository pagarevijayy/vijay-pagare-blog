+++
date = '2026-04-08T20:32:43+05:30'
title = 'Overview: System Design'
featured_image = "images/ccc-banner.png"
tags = ["SystemDesign", "Engineering"]
+++

Shoutout – https://paperdraw.dev (System Design w/ simulations)


System Design ain't about developing features or writing code, it's about managing trade-offs between speed, reliability, and cost. Below is the "index" of topics required to navigate top-tier architecture discussions.

## 1. The Storage Layer: Beyond CRUD
Understanding how data is physically stored determines how your system scales.
* **B-Trees vs. LSM-Trees:** The fundamental trade-off between Read-optimization (SQL) and Write-optimization (NoSQL). 
* **Storage Paradigms:** When to use Relational (ACID compliance), Document (flexible schema), Key-Value (low latency), or Graph (complex relationships).

## 2. Distributed Communication
How services talk to each other defines the user experience and system resilience.
* **Synchronous Patterns:** REST, GraphQL, and gRPC. Knowing when "instant" overhead is acceptable.
* **Asynchronous Patterns:** Message Queues (RabbitMQ) and Pub/Sub (Kafka). Decoupling systems to handle traffic spikes.

## 3. Scalability & Traffic Management
Moving from one server to thousands.
* **Load Balancing:** Layer 4 vs. Layer 7 balancing and health check strategies.
* **Caching Strategies:** Content Delivery Networks (CDN) for the edge, and Distributed Caches (Redis) for the application layer.
* **Database Partitioning:** Vertical vs. Horizontal scaling (Sharding) and the complexity of re-balancing data.

## 4. The Constraints: CAP & Consistency
In a distributed world, you cannot have everything.
* **The CAP Theorem:** Choosing between Consistency, Availability, and Partition Tolerance.
* **Consistency Models:** Strong consistency (Banking) vs. Eventual consistency (Social Media).

## 5. Resilience & Observability
Building systems that can fail gracefully.
* **Redundancy:** Data replication and multi-region deployments.
* **Fault Tolerance:** Circuit breakers and rate limiting to prevent "cascading failures."


Master these.
