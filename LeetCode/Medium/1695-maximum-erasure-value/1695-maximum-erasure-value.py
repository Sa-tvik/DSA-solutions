class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        l = 0
        pSum = 0
        maxm = 0

        for r in range(len(nums)):
            while nums[r] in dic:
                del dic[nums[l]]
                pSum -= nums[l]
                l += 1
            dic[nums[r]] = r
            pSum += nums[r]
            maxm = max(maxm, pSum)
        return maxm