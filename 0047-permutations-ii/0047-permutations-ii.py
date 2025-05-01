class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(arr, ans, used):
            if len(arr) == len(nums):
                ans.append(list(arr))
                return
            for i in range(len(nums)):
                if i>0 and nums[i-1]==nums[i] and not used[i-1]: continue
                if not used[i]:
                    used[i] = True
                    arr.append(nums[i])
                    helper(arr, ans, used)
                    arr.pop()
                    used[i] = False

        ans = []
        used = [False]*len(nums)
        nums.sort()
        helper([], ans, used)
        return ans
        