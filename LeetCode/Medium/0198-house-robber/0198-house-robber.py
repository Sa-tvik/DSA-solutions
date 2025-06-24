class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1:
            return nums[0]
        prev2 = nums[0]
        prev = max(nums[1],nums[0])
        for idx in range(2,n):
           curr = max(nums[idx] + prev2, prev)
           prev2 = prev
           prev = curr

        return prev

