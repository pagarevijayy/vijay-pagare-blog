+++
date = '2026-04-15T20:55:26+05:30'
title = 'DSA - 2 new (DFS Pattern, Recursion to DP Insight)'
description = 'Subtree matching using DFS serialization and recursive exploration for grid paths; key DP learning gap identified.'
tags = ["leetcode", "dsa"]
+++
---


## 572. Subtree of Another Tree 
**Insight** — DFS (preorder) serialization: if subRoot traversal string is a substring of root traversal string, then it is a subtree (ensure null markers like "N" + delimiters for exact match). 

**Comment** - Could solve. Core idea understood, but implementation still not smooth. Edge cases and clean serialization need more practice.

## 62. Unique Paths 

**Insight** — brute force = DFS on grid (only right & down), total paths = paths(right) + paths(down); then optimise using DP (memoization / tabulation) 

**Comment** - Could not solve. Hesitated to explore full recursion tree. Pattern was known but not applied. Need to reinforce habit: recursion → memoization → tabulation (Aditya Verma DP approach).
