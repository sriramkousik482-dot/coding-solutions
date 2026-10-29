class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        count = 0
        seen = set()
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            count = max(count, j - i + 1)
        return count
