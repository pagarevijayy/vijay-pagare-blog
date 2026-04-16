+++
date = '2026-04-16T21:30:00+05:30'
title = 'DSA - 2 new (Bit Manipulation Fundamentals)'
description = 'Bitwise operators, reverse bits intuition, and counting set bits using shifts'
+++
---

### 190. Reverse Bits  
**Insight**: Requires strong understanding of bitwise operators and shifts; iterate through 32 bits, extract last bit using AND, shift result left, and append  

**Comment**: Couldn’t solve independently; highlighted a gap in bit manipulation fluency, especially combining shifts and bit extraction correctly  

### 191. Number of 1 Bits  
**Insight**: Check last bit using AND with 1, increment count if set, then right shift to process remaining bits  

**Comment**:
After revising bitwise fundamentals, was able to solve comfortably.  

---

**Bitwise Operations:**

| Operator | Name | Description |
|----------|------|-------------|
| & | AND | Sets each bit to 1 if both bits are 1 |
| \| | OR | Sets each bit to 1 if at least one bit is 1 |
| ^ | XOR | Sets each bit to 1 if exactly one bit is 1 |
| ~ | NOT | Inverts all the bits |
| << | Left Shift | Shifts left by pushing zeros from the right |
| >> | Signed Right Shift | Shifts right while preserving the sign bit |
| >>> | Unsigned Right Shift | Shifts right by pushing zeros from the left |

Note — Bitwise operations are not in-place; always assign the result.

### Reflection

Clear signal that bit manipulation needs dedicated practice. These problems are less about patterns and more about comfort with low-level operations. Once the mental model clicks, they become mechanical.

### Progress on Dissertation:

Worked on incorporating examiner feedback — To include input modalities and output scoring + validation logic. Will share the report soon.
