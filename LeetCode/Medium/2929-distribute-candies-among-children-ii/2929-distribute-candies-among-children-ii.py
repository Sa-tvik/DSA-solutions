class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        x = limit + 1
        onechild = 3 * math.comb(n - x+2, 2) if n - x >= 0 else 0
        twochild = 3 * math.comb(n - 2 * x+2, 2) if n - 2 * x >= 0 else 0
        threechild = math.comb(n - 3 * x+2, 2) if n - 3 * x >= 0 else 0
        total = math.comb(n + 2, 2)
        return total - (onechild - twochild + threechild)

            