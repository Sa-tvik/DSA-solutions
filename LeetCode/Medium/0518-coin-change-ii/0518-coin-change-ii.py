class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def helper(idx, target):
            if idx == 0:
                if target%coins[idx] == 0:
                    return 1
                return 0
            
            if dp[idx][target] != -1:
                return dp[idx][target]
            
            notTake = helper(idx-1,target)
            take = 0
            if coins[idx]<=target:
                take = helper(idx,target-coins[idx])
            dp[idx][target] = take+notTake

            return dp[idx][target]

        n = len(coins)
        dp = [[-1 for j in range(amount+1)] for i in range(n)]

        return helper(n-1,amount)

