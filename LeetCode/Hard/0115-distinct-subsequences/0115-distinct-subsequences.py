class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for ind1 in range(1,len(s)+1):
            for ind2 in range(1,len(t)+1):
                if s[ind1-1] == t[ind2-1]:
                    dp[ind1][ind2] = dp[ind1-1][ind2-1] + dp[ind1-1][ind2]
                else:
                    dp[ind1][ind2] = dp[ind1-1][ind2]

        return dp[len(s)][len(t)]