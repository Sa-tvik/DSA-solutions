class Solution(object):
    def minZeroArray(self, nums, queries):
        def isValid(k):
            diff = [0] * (len(nums) + 1)
            for i in range(k):
                l, r, d = queries[i]
                diff[l] += d
                if r + 1 < len(nums):
                    diff[r + 1] -= d
            acc = 0
            for i in range(len(nums)):
                acc += diff[i]
                if nums[i] > acc:
                    return False
            return True

        if all(x == 0 for x in nums):
            return 0

        low, high = 1, len(queries)
        answer = -1
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
