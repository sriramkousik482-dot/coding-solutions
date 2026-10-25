class Solution:
    def toLowerCase(self, s: str) -> str:
        result=""
        for ch in s:
            if ch.isupper():
                result+=ch.lower()
            else:
                result+=ch
        return result