class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0]*n
        dp[0] = grid[0][0]
        for col in range(1, n):
            dp[col] = dp[col-1] + grid[0][col]

        for row in range(1,m):
            temp = [0]*n
            for col in range(n):
                up = float('inf')
                left = float('inf')
                if row == 0 and col == 0:
                    dp[0] = grid[0][0]
                    continue
                if row > 0:
                    up = dp[col]
                if col > 0:
                    left = temp[col-1]

                temp[col] = grid[row][col] + min(left, up)
            dp = temp
                    
        return dp[n-1]