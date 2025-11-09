class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def findWays(nums, k):
            n = len(nums)
            prev = [0 for i in range(k + 1)]
            prev[0] = 1

            if nums[0] == 0:
                prev[0] = 2
            else:
                prev[0] = 1
                if nums[0]<=k:
                    prev[nums[0]] = 1

            for ind in range(1, n):
                cur = [0 for i in range(k + 1)]
                for target in range(k + 1):
                    notTaken = prev[target]
                    taken = 0
                    if nums[ind] <= target:
                        taken = prev[target - nums[ind]]

                    cur[target] = notTaken + taken
                prev = cur
            return prev[k]

        summ = sum(nums)
        if summ < target: return 0
        if (summ - target)%2 !=0: return 0

        return findWays(nums, (summ-target)//2)

        
        