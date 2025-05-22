class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """

        queries.sort()
        heap = []
        borders = [0] * (len(nums) + 1)
        operations = 0
        q = 0
    
        for index, num in enumerate(nums):
            operations += borders[index]
    
            while q < len(queries) and queries[q][0] == index:
                heappush(heap, -queries[q][1])
                q += 1
    
            while operations < num and heap and -heap[0] >= index:
                operations += 1
                borders[-heappop(heap) + 1] -= 1
    
            if operations < num:
                return -1
    
        return len(heap)