class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n=len(nums)
        for i in range(n):
            for j in range(1,n):
                if nums[j]<nums[j-1]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
        print(*nums)
            

        
        