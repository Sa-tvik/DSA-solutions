class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -float('inf')
        result = 0
        for v in nums:
            if v >= prev:
                prev = v
                result += 1
        return result

        