class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        maxProfit = 0
        minm = prices[0]
        for i in range(1,len(prices)):
            minm = min(prices[i],minm)
            if prices[i] - minm>maxProfit:
                maxProfit = prices[i]-minm
            else:
                profit+=maxProfit
                maxProfit = 0
                minm = prices[i]            
        profit+=maxProfit
        return profit


        