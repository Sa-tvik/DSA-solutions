class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(len(nums)):
            if len(heap)>=k:
                heapq.heappushpop(heap,nums[i])
            else:
                heapq.heappush(heap,nums[i])

        return heap[0]
        