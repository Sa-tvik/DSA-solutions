class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*n
        dp[0] = 1
        for row in range(m):
            temp = [0]*n
            temp[0] = 1
            for col in range(1,n):
                left = temp[col-1] 
                right = 0
                if row>0:
                    right = dp[col]
                temp[col] = left+right
            dp = temp
        return dp[n-1]
