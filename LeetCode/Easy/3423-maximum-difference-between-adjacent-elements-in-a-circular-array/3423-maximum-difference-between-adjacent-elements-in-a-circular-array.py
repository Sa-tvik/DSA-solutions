class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxm = 0
        for i in range(1,len(nums)):
            maxm = max(maxm,abs(nums[i]-nums[i-1]))
        return max(maxm,abs(nums[len(nums)-1]-nums[0]))