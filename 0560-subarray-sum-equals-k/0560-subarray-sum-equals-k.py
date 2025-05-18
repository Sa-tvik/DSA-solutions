class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        pSum = 0
        res = 0
        dic[0] = 1
        for i in range(len(nums)):
            pSum += nums[i]
            if pSum-k in dic:
                temp = dic[pSum-k]
                res += temp
            if pSum in dic:
                temp = dic[pSum]
                dic[pSum] = temp+1
            else:
                dic[pSum] = 1

        return res


            

        