class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m): 
            if text1[i] == text2[0]: 
                dp[i][0] = 1 
            else: 
                dp[i][0] = dp[i-1][0]

        for i in range(1,n):
            if text1[0] == text2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = dp[0][i-1]

        for ind1 in range(1, m):
            for ind2 in range(1,n):
                if text1[ind1] == text2[ind2]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = max(dp[ind1-1][ind2], dp[ind1][ind2-1])

        return dp[m-1][n-1]
        
            