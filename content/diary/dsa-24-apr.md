+++
title = "DSA - 2 Problems - Counting Bits, Trie Design"
date = "2026-04-24"
slug = "2026-04-24-counting-bits-trie-design"
tags = ["dsa", "leetcode"]
+++

---
## 338. Counting Bits

**Insight**: For each i, use bit manipulation — check last bit using &, right shift >>, increment count. Can be written in one line. Use memoization to avoid repeated calculations.

**Comment**: Thought of 2 solutions — bit manipulation and JS inbuilt (string conversion).

---
## 221. Design Add and Search Words Data Structure

**Insight**: Standard Trie. For '.', assume any char → DFS + backtracking.

**Comment**: Logic was clear, almost solved. Hesitated on implementing '.' DFS (passing root vs node), though idea was there.

**Reflection**:
- Overall, a decent day.
- Went through URL shortener video
