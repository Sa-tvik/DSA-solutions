class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0 for j in range(n+1)]
        mod = 10**9 + 7
        dp[0] = 1
        for idx in range(1,n+1):
            temp = [0 for j in range(n+1)]
            temp[0] = 1
            for target in range(1,n+1):            
                notTake = dp[target]
                Take = 0
                if idx**x <= target:
                    Take = dp[target-idx**x]
                temp[target] = Take + notTake
            dp = temp

        return dp[n]%mod