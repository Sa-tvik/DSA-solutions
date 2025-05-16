class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7
        if n%2==0:
            return pow(20,(n/2),mod) 
        elif n == 1:
            return 5
        else: 
            return pow(20,(n//2),mod)*5%mod     