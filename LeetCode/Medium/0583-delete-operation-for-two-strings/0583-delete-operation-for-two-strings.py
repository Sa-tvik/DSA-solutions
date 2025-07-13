class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [0]*(m+1)
        
        for ind1 in range(1,n+1):
            temp = [0]*(m+1)
            for ind2 in range(1,m+1):
                if word1[ind1-1] == word2[ind2-1]:
                    temp[ind2] = 1 + dp[ind2-1]
                else:
                    temp[ind2] = max(temp[ind2-1], dp[ind2])
            dp = temp
        return n-dp[m] + m-dp[m]