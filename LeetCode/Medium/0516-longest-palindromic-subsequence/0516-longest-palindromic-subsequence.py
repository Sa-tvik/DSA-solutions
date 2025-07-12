class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(ind1, ind2):
            if ind1<0 or ind2<0:
                return 0
             
            if dp[ind1][ind2] !=-1:
                return dp[ind1][ind2]
            
            if s[ind1] == revS[ind2]:
                dp[ind1][ind2] = 1 + helper(ind1-1, ind2-1)
            else:
                dp[ind1][ind2] = max(helper(ind1-1, ind2), helper(ind1,ind2-1))

            return dp[ind1][ind2]
        
        n = len(s)
        revS = "".join(reversed(s))
        dp =[[-1 for j in range(n)] for i in range(n)]
        return helper(n-1,n-1)