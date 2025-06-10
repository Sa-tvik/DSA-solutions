class Solution:
    def fib(self, n: int) -> int:
        def helper(n, dp):
            if n <= 1:
                return n
            if dp[n] != -1:
                return dp[n]
            dp[n] = helper(n - 1, dp) + helper(n - 2, dp)
            return dp[n]

        dp = [-1] * (n + 1)
        return helper(n, dp)