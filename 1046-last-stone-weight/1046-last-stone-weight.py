class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            temp1 = heapq.heappop(max_heap)
            temp2 = heapq.heappop(max_heap)
            if temp1!=temp2: 
                heapq.heappush(max_heap, temp1-temp2) 
        
        return -max_heap[0] if len(max_heap)>0 else 0


        