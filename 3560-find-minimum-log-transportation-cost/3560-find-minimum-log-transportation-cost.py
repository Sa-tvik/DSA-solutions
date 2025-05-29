class Solution(object):
    def minCuttingCost(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        if n<=k and m<=k: return 0

        if n<=k:
            n,m = m,n
        
        cost = 0
        if n > k and m <= k:
            cost += (n - k) * k
        
        return cost

        



        
        