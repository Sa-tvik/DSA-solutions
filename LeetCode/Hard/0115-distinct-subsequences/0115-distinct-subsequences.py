class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 for j in range(len(t)+1)]
        dp[0] = 1
        for ind1 in range(1,len(s)+1):
            temp = [0 for j in range(len(t)+1)]
            temp[0] = 1
            for ind2 in range(1,len(t)+1):
                if s[ind1-1] == t[ind2-1]:
                    temp[ind2] = dp[ind2-1] + dp[ind2]
                else:
                    temp[ind2] = dp[ind2]
            dp = temp
        return dp[len(t)]