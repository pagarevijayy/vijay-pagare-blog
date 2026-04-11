+++
date = '2026-04-11T23:24:56+05:30'
title = 'DSA - 2 new, 1 revision (Greedy, Kadane, Linked List)'
description = 'Non-overlapping intervals, Maximum subarray, Merge K sorted lists + reflection on strategy'
featured_image = "images/ccc-banner.png"
tags = ["leetcode", "dsa"]

+++

###  New Problems

**435. Non-overlapping Intervals**  
- **Concept:** Greedy  
- **Insight:**  
  Sort intervals based on start. Iterate and compare adjacent intervals while maintaining `prevEnd`.  
  - If no overlap → update `prevEnd`  
  - If overlap → increment count and update `prevEnd = min(prevEnd, currEnd)`  
- **Comment:**  
  Solved partial conditions independently. Needed a hint to unlock the core greedy idea, then implemented successfully.

---

**53. Maximum Subarray**  
- **Concept:** Kadane’s Algorithm  
- **Insight:**  
  At each step, track max of:
  - current element  
  - sum till now + current  
  Maintain a global maximum.  
- **Comment:**  
  Recognized the pattern after hint. Execution was straightforward once direction was clear.

---

### Revision

**23. Merge K Sorted Lists**  
- **Concept:** Linked List, Divide & Conquer (Iterative merge)  
- **Approach:**  
  Repeatedly merge 2 sorted lists and pass the result forward.  
- **Comment:**  
  Reinforced the idea that breaking K into pairs simplifies complexity mentally and implementation-wise.

---

### 🧘 Reflection

The optimal LeetCode strategy is becoming clearer:

- Phase 1:  
  **2 new problems/day for ~10–12 days** → build exposure

- Phase 2:  
  **1 new + multiple revisions** → solidify patterns

True ROI doesn’t come from solving new problems alone —  
it comes from **revisiting and internalizing patterns through spaced repetition**.

LeetCode mastery is less about intelligence, more about **memory + pattern recall under pressure**.

At least for mid-level grinders — this is the game.
