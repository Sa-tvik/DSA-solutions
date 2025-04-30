class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(arr, ans):
            if len(arr) == len(nums):
                ans.append(list(arr))
                return
            for i in range(len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    helper(arr, ans)
                    arr.pop()

        ans = []
        helper([], ans)
        return ans
