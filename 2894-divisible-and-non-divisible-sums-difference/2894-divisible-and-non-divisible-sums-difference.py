class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return n*(n+1)//2-m*(n//m)*(n//m+1)
        