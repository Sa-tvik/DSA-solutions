class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 0
        temp = 0
        n = len(citations)
        num = [0]*(n+1)
        for i in range(n):
            if citations[i]>=n:
                num[-1]+=1
            else:
                num[citations[i]]+=1


        for i in range(n,-1,-1):
            temp+=num[i]
            if temp>=i:
                return i


