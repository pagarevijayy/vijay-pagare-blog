+++
title = "DSA - 2 new (sliding window, linked list)"
date = 2026-04-21
slug = "2026-04-21-minimum-window-substring-reverse-linked-list"
tags = ["dsa", "leetcode"]
+++

## 🧠 Today’s Problems

### 76. Minimum Window Substring

**Insight:**  
Use a hashmap to track the frequency of characters in `t`. Expand the window until all required characters are covered. Once valid, try shrinking the window from the left to find the minimum substring.

Key ideas:
- Maintain a frequency map of `t`
- Use a counter to track how many characters are still needed
- Expand right pointer to satisfy condition
- Once valid → shrink from left as much as possible
- Handle edge cases where extra valid characters exist

**Important Learning:**  
When encountering extra characters beyond required frequency, they should NOT affect the valid count. This means:
- Only decrement count when character frequency is still needed
- Only increment count back when removing a *required* character

**Comment:**  
I had ~95% of the logic clear.  
- Missed handling of extra characters correctly  
- Didn’t implement the inner `while` loop for shrinking confidently  
- Knew I had to shrink after valid window but couldn’t translate it into code  
- Took help from Gemini to refine and complete implementation  

---

### 206. Reverse Linked List

**Insight:**  
Classic pointer manipulation problem.

- Use `prev = null`
- Traverse using `curr = head`
- Store next node temporarily
- Reverse current node’s pointer
- Move `prev` and `curr` forward

**Pattern:**
```
next = curr.next
curr.next = prev
prev = curr
curr = next
```


**Comment:**  
Conceptually straightforward, but execution wasn’t as fast as expected.  
Had to pause and think through pointer transitions.

---

## ⚡ Key Takeaways

- Knowing the approach ≠ being able to implement it cleanly. Improve confidence in translating thought → code    
- Sliding window problems often require **nested loops (expand + shrink)** — don’t hesitate  
- Edge cases (especially frequency handling) are where most bugs hide  
- Pointer problems demand **calm, step-by-step thinking**, not speed

---

## 🚀 Good Momentum 

- Recognizing patterns faster  
- Identifying gaps in execution clearly  

Feels like it's really hard NOT to crack FAANG with a year's grind.
