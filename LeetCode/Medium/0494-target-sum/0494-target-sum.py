class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        total = sum(abs(x) for x in nums)
        offset = total
        dp = [[-1 for j in range(2*offset+1)] for i in range(n)]

        def helper(idx, curr):
            if idx == 0:
                cnt = 0
                if curr+nums[idx] == target:
                    cnt+=1
                if curr-nums[idx] == target:
                    cnt+=1
                return cnt
            
            if dp[idx][curr + offset] != -1:
                return dp[idx][curr + offset]

            notTaken = helper(idx-1, curr-nums[idx])
            taken = 0
            taken = helper(idx-1, curr+nums[idx])
            dp[idx][curr + offset] = taken+notTaken

            return dp[idx][offset + curr]

        num = helper(n-1,0)
        return num 
        