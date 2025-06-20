class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        count = 0
        n = len(citations)
        for i in range(n-1,-1,-1):
            if citations[i]>=n-i:
                count = max(n-i,count)
        return count
