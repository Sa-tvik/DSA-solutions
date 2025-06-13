class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation%2 != 0: return False
        target = int(summation/2)
        n = len(nums)
        dp = [False]*(target+1)
        dp[0] = True
        for idx in range(1,n):
            temp = [False]*(target+1)
            temp[0] = True
            for target in range(1,target+1):
                notTaken = dp[target]
                taken = False
                if nums[idx]<=target:
                    taken = dp[target- nums[idx]]

                temp[target] = taken or notTaken
            dp = temp

        return dp[target]

            
            
            