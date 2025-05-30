class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        heap = []
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            if len(heap)>=k:
                heapq.heappushpop(heap, [value,key])
            else:
                heapq.heappush(heap, [value,key])

        while len(heap)>0:
            res.append(heapq.heappop(heap)[1])
        return res
        


            
            

            
        