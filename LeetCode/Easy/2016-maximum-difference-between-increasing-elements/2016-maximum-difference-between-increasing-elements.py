class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxm = -1
        l = 0
        for r in range(1,len(nums)):
            if nums[r]>nums[l]:
                maxm = max(maxm,nums[r]-nums[l])
            if nums[l]>nums[r]:
                l = r

        return maxm

