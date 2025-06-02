class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(idx1, idx2,temp, res,n):
            if idx1 == n and idx2 == n:
                res.append(temp)
                
            if idx1<n:
                helper(idx1+1,idx2,temp + "(",res,n)
            if idx1>idx2:
                helper(idx1,idx2+1,temp + ")",res,n)


        res = []
        helper(0,0,"",res,n)
        return res


