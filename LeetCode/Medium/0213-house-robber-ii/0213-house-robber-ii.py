class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]

            prev2 = arr[0]
            prev = max(arr[0], arr[1])
            curr = 0
            for i in range(2, n):
                curr = max(arr[i] + prev2, prev)
                prev2 = prev
                prev = curr
            return prev 
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        return max(helper(nums[1:n]),helper(nums[:n-1]))