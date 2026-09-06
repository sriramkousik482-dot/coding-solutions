class Solution:
    def countRotations(self, s: str, k: int) -> int:
        ans=0
        n=len(s)
        for r in range(n):
            r=s[r:]+s[:r]
            count=0
            for i in range(n-1):
                if r[i]==r[i+1]:
                    count+=1
            if count==k:
                ans+=1
        return ans