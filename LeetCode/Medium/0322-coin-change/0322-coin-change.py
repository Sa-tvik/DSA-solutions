class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        prev = [0] * (amount + 1)  
        cur = [0] * (amount + 1)  


        for i in range(0, 1 + amount):
            if i % coins[0] == 0:
                prev[i] = i // coins[0]
            else:
                prev[i] = int(1e9)

        for ind in range(1, n):
            for target in range(amount + 1):

                not_take = prev[target]
                take = int(1e9)          

                if coins[ind] <= target:
                    take = 1 + cur[target - coins[ind]]   
                cur[target] = min(not_take, take) 
            prev = cur 
        ans = prev[amount]

        if ans >= int(1e9):
            return -1
        return ans