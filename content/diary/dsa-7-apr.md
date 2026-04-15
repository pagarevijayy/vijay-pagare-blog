+++
title = "DSA: 1 new, 3 revision (Sliding Window, DP, LL, Graph)"
date = "2026-04-07T23:38:42+05:30"
slug = "dsa-daily-log-2026-04-07"
description = "A daily progress log covering problem-solving insights across Sliding Window, Dynamic Programming, Linked Lists, and Graphs."
tags = ["dsa", "leetcode"]
+++

Today was about strengthening the foundations and reflecting upon the mastery strategy. While the original plan was two new problems daily, the reality of high-level prep is teaching me that **revision and depth** often outweigh raw volume. 

## 🧠 DSA Summary

### 1. Longest Repeating Character Replacement (LC 424)
* **The Pivot:** Shifting from a Brute Force approach (checking every possible substring) to a refined **Sliding Window**.
* **The Insight:** The window is valid as long as the number of replacements needed doesn't exceed `k`.
* **Core Logic:** `Window Length - Max Frequency of a Character <= k`
* **Reflection:** I managed to hack together a partial solution, but the "aha!" moment came from maintaining the character count hash to dynamically expand the right pointer and shrink the left. Though an even better solution with keep count of maxFrequency exists.



### 2. Pacific Atlantic Water Flow (LC 417)
* **The Insight:** Treat the 2D matrix as a graph. The key is defining a solid base condition: boundaries + visited sets + the "main business logic" (water height). Working backward from the oceans often simplifies the flow.

### 3. Remove Nth Node From End of List (LC 19)
* **The Insight:** The "Two-Pointer Gap" strategy. By advancing the first pointer `n` steps ahead and then pointing the second to the head, they can hop together. When the first hits the end, the second points exactly to the node that needs removal. **One pass, `O(n)` efficiency.**

### 4. Maximum Product Subarray (LC 152)
* **The Insight:** Negative numbers are the wildcards—they can turn a minimum into a maximum instantly. 
* **The Fix:** It is vital to track **both** the current min and max. When introducing a new element, consider three cases: 
    1. Starting a new subarray.
    2. Multiplying with the previous max.
    3. Multiplying with the previous min.
* **Note:** Encountering a zero resets the running product.

---

## 🏗️ Strategy Shift: Quality > Quantity

I couldn't accommodate a System Design (SD) question today due to time constraints, which sparked a realization about ROI (Return on Investment). Moving forward, I’m adjusting the daily goal:

| Goal Type | Quantity | Purpose |
| :--- | :--- | :--- |
| **New Problems** | 1 Blind75 | Deep focus and implementation |
| **Revision** | 1-2 Problems | Reinforcement of past concepts |
| **System Design** | 1 Question | High-level architectural breadth |

This feels more sustainable than grinding new problems while letting old ones fade.

---

## ✨ Thought for the Day

> "On days you can't fly, run. On days you can't run, walk. On days you can't walk, crawl. Make progress. Progress is progress – no matter what!"

Overall, a satisfactory day. The **Mastery Vault** is growing, one pointer at a time.
