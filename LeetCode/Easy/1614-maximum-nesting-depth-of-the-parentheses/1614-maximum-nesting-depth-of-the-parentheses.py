class Solution:
    def maxDepth(self, s: str) -> int:
        maxm = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth+=1
            elif s[i] == ')':
                depth -= 1
            else: continue
            maxm = max(maxm, depth)
        return maxm