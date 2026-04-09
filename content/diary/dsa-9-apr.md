+++
date = '2026-04-09T20:18:55+05:30'
title = 'DSA - 1 new, 3 revision (Matrix Math, DFS, Sliding Window, Binary Search)'
featured_image = "images/ccc-banner.png"
tags = ["leetcode", "dsa"]
+++

Tackled a mix of new challenges and critical revisions, focusing on the philosophy that core patterns—Arrays, Strings, and DFS—must become second nature.

---
### 48. Rotate Image (Medium)
#### Approach
  1. **Transpose matrix** → swap `(i, j)` with `(j, i)`
  2. **Reverse each row**

#### Reflection
- Came up with a **half-baked approach**
- Missed the **transpose + reverse pattern**
- Made **silly mistakes**:
  - Incorrect transpose logic (didn't limit swaps correctly)
  - Reverse logic not optimized (can use 2-pointer technique → O(n))
- Need to **slow down and think clearly before coding**

---

## Revisions

### 297. Serialize and Deserialize Binary Tree (Hard)

#### Approach
- Use **DFS traversal**
- Serialize:
  - Store values using delimiter `","`
  - Use `"N"` for null nodes
- Deserialize:
  - Rebuild using DFS
  - Maintain pointer/index across recursion

#### Reflection
  - Solved in **<25 mins**
  - Minor confusion:
    - Pointer increment in deserialization
    - Must pass pointer **by reference**
    - Avoid loops; rely purely on DFS flow

---

### 3. Longest Substring Without Repeating Characters (Medium)

#### Approach
- **Sliding Window + Two Pointers**
  - Expand window when valid
  - Shrink when duplicate found
- Use **Set / HashMap** for tracking characters

#### Reflection
- Felt **easy this time**
- Stayed calm and executed step-by-step
- No unnecessary panic → big improvement

---

### 33. Search in Rotated Sorted Array (Medium)

#### Approach
- Modified **Binary Search**
- Identify **sorted half** and move accordingly

#### Reflection
- Took time to internalize **edge/else cases**
- Once understood → logic felt clear
- Key idea: *always move towards the sorted side*

---

## 🧩 Insights / Learnings

- Core topics must become **muscle memory**:
  - Array
  - String
  - Binary Search
  - Sorting
  - DFS / BFS  

- No excuses for:
  - Array manipulation mistakes
  - Basic data handling errors  

- Think like learning math as a kid:
  - Repetition → clarity → speed  

-  Core methodologies should feel **almost memorized**

- Data manipulation (arrays, hashmaps, strings):
  - Should be **second nature**
  - No struggle during implementation  

---

## 🎯 Closing Thought

> "Know your tools so well that thinking becomes optional and execution becomes automatic."
