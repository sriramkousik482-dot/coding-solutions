# To Lower Case

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, return  *the string after replacing every uppercase letter with the same lowercase letter*.

 

 **Example 1:** 

```
Input: s = "Hello"
Output: "hello"

```

 **Example 2:** 

```
Input: s = "here"
Output: "here"

```

 **Example 3:** 

```
Input: s = "LOVELY"
Output: "lovely"

```

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.1 MB (beats 96.02%)  
**Submitted:** 2026-10-25T07:16:42.344Z  

```py
class Solution:
    def toLowerCase(self, s: str) -> str:
        result=""
        for ch in s:
            if ch.isupper():
                result+=ch.lower()
            else:
                result+=ch
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/to-lower-case/)