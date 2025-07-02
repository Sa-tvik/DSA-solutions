class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        k = target
        total = sum(abs(x) for x in nums)
        offset = total
        if target>total:
            return 0
        if n == 1:
            if (nums[0] == target or -nums[0] == target):
                if nums[0] == 0:
                    return 2
                return 1
            return 0
        
        dp = [0 for j in range(2*offset+1)]
        
        dp[nums[0] + offset] += 1
        dp[-nums[0] + offset] += 1

        for idx in range(1,n):
            temp = [0]*(2*offset+1)
            for t in range(-total,total+1):
                if dp[t+offset]>0:
                    temp[t+offset+nums[idx]] += dp[t+offset]
                    temp[t+offset-nums[idx]] += dp[t+offset]
            dp = temp

        return dp[target+offset]