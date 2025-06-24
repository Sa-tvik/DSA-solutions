class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(idx):
            if idx<0:
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]
            
            dp[idx] = max(nums[idx] + helper(idx-2), helper(idx-1))

            return dp[idx]

        dp = [-1]*n
        return helper(n-1)

