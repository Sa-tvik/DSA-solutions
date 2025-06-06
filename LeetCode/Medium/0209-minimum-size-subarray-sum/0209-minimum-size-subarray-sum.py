class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minm = float('inf')
        temp = 0
        for r in range(len(nums)):
            temp += nums[r]
            while temp>=target:
                minm = min(minm,r-l+1)
                temp-=nums[l]
                l+=1
        return minm if minm != float('inf') else 0
            