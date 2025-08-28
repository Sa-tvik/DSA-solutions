class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        minm = nums[0]
        maxm = nums[0]
        summ = 0
        for r in range(len(nums)):
            summ+=nums[r]
            currMax = max(currMax + nums[r], nums[r])
            currMin = min(currMin + nums[r], nums[r])
            maxm = max(currMax, maxm)
            minm = min(currMin, minm)

        return max(maxm, summ - minm) if maxm > 0 else maxm
            