---
title: "DSA - 1 new - House Robber (DP)"
date: 2026-04-19
slug: "2026-04-19-house-robber-dp-take-skip"
tags: ["dsa", "leetcode"]
---
---
## 🧠 Problem: 198. House Robber

### 💡 Insight  
Either:
- Select current house → move to `i + 2`  
- Skip current house → move to `i + 1`  

Take the maximum of both choices.

Recurrence:
dp[i] = max(nums[i] + dp[i+2], dp[i+1])

---

### 🧩 Comment  
Had to think harder than expected. Derived using recursion + memoization, but initially missed the **skip case edge condition**, so the formulation wasn’t clean at first.

---

### ⚡ Key Learning  
Whenever:
1. You are making a choice at each step  
2. Choices are mutually exclusive (take vs skip)  
3. You want to maximize/minimize something  

→ Think **DP on decisions (take / skip pattern)**

---

### 🧘 Note  
Lower volume day due to family commitments — still showed up. Consistency matters more than intensity.
