class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        revS = "".join(reversed(s))
        dp = [0]*(n+1)

        for ind1 in range(1,n+1):
            temp = [0]*(n+1)
            for ind2 in range(1,n+1):
                if s[ind1-1] == revS[ind2-1]:
                    temp[ind2] = 1 + dp[ind2-1]
                else:
                    temp[ind2] = max(dp[ind2], temp[ind2-1])
            dp = temp
        return len(s) - dp[n]