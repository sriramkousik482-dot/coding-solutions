class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n=len(nums)
        for j in range(n):
            for i in range(1,n):
                if nums[i]<nums[i-1]:
                    nums[i],nums[i-1]=nums[i-1],nums[i]
        print(*nums)
            

        
        