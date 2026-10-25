class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pari={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in pari:
                if not stack or stack[-1]!=pari[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0
            
                
        
