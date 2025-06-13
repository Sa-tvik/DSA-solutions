class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [-1 for j in range(amount+1)]
        for i in range(amount+1):
            if i%coins[0] == 0:
                dp[i] = i//coins[0]
            else:
                dp[i] = float('inf')
        
        for idx in range(1,n):
            temp = [-1]*(amount+1)
            for target in range(amount+1):          
                notTaken = dp[target]
                taken = float('inf')
                if coins[idx]<=target:
                    taken = 1 + temp[target-coins[idx]]
                temp[target] = min(taken, notTaken)
            dp = temp
        num = dp[amount]
        return num if num != float('inf') else -1