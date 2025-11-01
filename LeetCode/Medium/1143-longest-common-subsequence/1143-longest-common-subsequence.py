class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [0]*(m+1)
        
         
        for ind1 in range(1,n+1):
            temp = [0]*(m+1)
            for ind2 in range(1,m+1):
                if text1[ind1-1] == text2[ind2-1]:
                    dp[ind2] = 1 + dp[ind2-1]
                else:
                    dp[ind2] = max(dp[ind2-1], dp[ind2])

        return dp[m]