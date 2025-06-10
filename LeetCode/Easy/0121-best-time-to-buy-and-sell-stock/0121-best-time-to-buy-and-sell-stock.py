class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minm = prices[0]
        for i in range(1,len(prices)):
            minm = min(prices[i],minm)
            if prices[i] - minm>maxProfit:
                maxProfit = prices[i]-minm
        return maxProfit



