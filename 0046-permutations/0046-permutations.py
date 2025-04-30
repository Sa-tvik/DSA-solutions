class Solution(object):


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(ind, nums, ans, arr):
            if len(nums) == len(arr):
                ans.append(list(arr))
            else:
                for i in range(len(nums)):
                    if nums[i] not in arr:
                        arr.append(nums[i])
                        helper(i+1, nums, ans, arr)
                        arr.pop()

        ans = []
        helper(0,nums,ans,[])
        return ans
        