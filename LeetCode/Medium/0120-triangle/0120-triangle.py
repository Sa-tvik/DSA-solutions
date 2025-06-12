class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0]*n
        dp[0] = triangle[0][0]
        for row in range(1,n):
            temp = [0]*n
            for col in range(row+1):
                up = float('inf')
                left = float('inf')
                if row > col:
                    up = dp[col]
                if col > 0:
                    left = dp[col-1]

                temp[col] = triangle[row][col] + min(left, up)
            dp = temp

        minm = float('inf')
        for idx,val in enumerate(dp):
            minm = min(val,minm) 

        return minm