class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [[-1 for j in range(amount+1)] for i in range(n)]
        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = float('inf')
        
        for idx in range(1,n):
            for target in range(amount+1):          
                notTaken = dp[idx-1][target]
                taken = float('inf')
                if coins[idx]<=target:
                    taken = 1 + dp[idx][target-coins[idx]]
                dp[idx][target] = min(taken, notTaken)

        num = dp[n-1][amount]
        return num if num != float('inf') else -1