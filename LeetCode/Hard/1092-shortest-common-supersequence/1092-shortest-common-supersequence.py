class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        dp = [[0 for j in range(m+1)] for i in range(n+1)]
    
        for ind1 in range(1,n+1):
            for ind2 in range(1,m+1):
                if str1[ind1-1] == str2[ind2-1]:
                    dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2] = max(dp[ind1][ind2-1], dp[ind1-1][ind2])

        res = []
        i,j = n,m
        while i>0 and j>0:
            if str1[i-1] == str2[j-1]:
                res.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j] >  dp[i][j-1]:
                res.append(str1[i-1])
                i-=1
            else:
                res.append(str2[j-1])
                j-=1

        while i > 0:
            res.append(str1[i-1])
            i -= 1
    
        while j > 0:
            res.append(str2[j-1])
            j -= 1
        
        return ''.join(res[::-1]) 